#include "degree.hpp"

#ifdef __cplusplus
extern "C" {
  void test(DegreePapers *ptr)
  {
    std::cout << ptr->papers << std::endl;
  }

  void run(int *papers, 
           int length,
           void (caller)(int *, int),
           DegreePapers *schedule)
  {
    try {
      Degree::Degree *degree = new Degree::Degree(papers, length, schedule);
      BAB<Degree::Degree> bab(degree);
      delete degree;
      int count = 0;
      while(Degree::Degree *d = bab.next()) {
        std::cout << count++ << std::endl;
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
      std::cerr << e.what() << std::endl;
    }
  }
}
#endif //  __cplusplus

namespace Degree
{

  Degree::Degree(int *papers, 
                 int length,
                 int ()
    : cost_value(*this, 0, 100),
      degree_papers(*this, 24, 100100, 999999),
      degree(*this, 0, 100000)
  {
    for(int i = 0, j = 0; i < length; i++) {
      paper_list.insert(papers[i]);
      if(is_valid(0, papers[i])) {
        rel(*this, degree_papers[j++] == papers[i]);
      }
    }


    rel(*this, degree == is_valid(degree.assigned() ? degree.val() : -1, 0));
    distinct(*this, degree_papers);
    rel(*this, cost_value == 100);

    branch(*this, degree_papers, INT_VAR_SIZE_MAX, INT_VAL_MAX);
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
    return degree_papers[pos].val();
  }


  int Degree::get_degree(void) const
  {
    return degree.val();
  }
} // Degree
