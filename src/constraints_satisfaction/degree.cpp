#include "degree.hpp"

#ifdef __cplusplus
extern "C" {
  void test(DegreePapers *ptr)
  {
    std::cout << ptr->papers << std::endl;
  }

  void run(int *papers, 
           int length,
           int *degrees,
           int dlength,
           void (caller)(int, int *, int),
           int *(is_valid)(int, int *))
  {
    try {
      std::cout << "Number of papers is " << length << std::endl;
      std::cout << "creating Degree" << std::endl;
      Degree::Degree *degree = new Degree::Degree(papers, length, degrees, dlength, is_valid);
      std::cout << "created Degree" << std::endl;
      BAB<Degree::Degree> bab(degree);
      delete degree;
      
      int count = 0;
      std::cout << "searching for solution" << std::endl;
      while(Degree::Degree *d = bab.next()) {
        std::cout << "Count " << count++ << std::endl;
        int paper_set[24];
        for(int i = 0; i < 24; i++) {
          paper_set[i] = d->get_paper(i);
        }
        /* callback function which should be a 
         * python function allowing solution to 
         * be accesed by python code.
         */
        caller(d->get_degree(), paper_set, 24);
        delete d; // free pointer up for next iteration
        d = NULL; // always set pointers to NULL after freeing
      }
    } catch(Exception e) {
      std::cerr << "Gecode failure: " << e.what() << std::endl;
    }
  }
}
#endif //  __cplusplus

namespace Degree
{

  Degree::Degree(int *papers, 
                 int length,
                 int *degrees,
                 int dlength,
                 int *(valid_papers)(int degree, int *length))
    : cost_value(*this, 0, 100),
      degree_papers(*this, 24, 100100, 999999),
      degree(*this, 0, 100000)
  {
    for(int i = 0; i < dlength; i++) {
      rel(*this, degree == degrees[i]);
    }
    std::cout << "In constructor with paper length of " << length << std::endl;
    int j = 0;
    for(int i = 0; i < length; i++) {
      paper_list.insert(papers[i]);
      rel(*this, degree_papers[j++] == papers[i]);
    }


    for(int i = j; i < 24; i++) {
      if(degree.assigned()) {
        int *papers = NULL;
        int len = 1;
        papers = valid_papers(degree.val(), &len);
        std::cout << len << std::endl;
        for(int i = 0; i < len; i++) {
          std::cout << papers[0] << std::endl;
        }
      }
    }

    //rel(*this, degree == is_valid(degree.assigned() ? degree.val() : -1, NULL, -1, -1));
    distinct(*this, degree_papers);
    rel(*this, cost_value == 10);

    branch(*this, degree_papers, INT_VAR_SIZE_MAX, INT_VAL_RND);
  }




  Degree::Degree(bool share, Degree &d)
    : MaximiseSpace(share, d),
      paper_list(d.paper_list)
  {
    cost_value.update(*this, share, d.cost_value);
    degree_papers.update(*this, share, d.degree_papers);
    degree.update(*this, share, d.degree);
  }




  Degree::~Degree(void)
  {
    std::cout << "deleted Degree" << std::endl;
  }




  Space *Degree::copy(bool share)
  {
    return new Degree(share, *this);
  }




  IntVar Degree::cost(void) const
  {
    return cost_value;
  }


  int Degree::get_paper(int pos) const
  {
    //needs to check if is assigned or not
    return degree_papers[pos].assigned() ? degree_papers[pos].val() : 0;
  }


  int Degree::get_degree(void) const
  {
    return degree.assigned() ? degree.val() : 0;
  }
} // Degree
