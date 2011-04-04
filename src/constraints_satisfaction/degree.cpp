#include "degree.hpp"
#include "propagator.hpp"

#ifdef __cplusplus
extern "C" {
  void run(int *papers, 
           int length,
           int *degrees,
           int dlength,
           void (caller)(int, int *, int))/*,
           void *(is_valid)(int, int *))*/
  {
    try {
      std::cout << "Number of papers is " << length << std::endl;
      std::cout << "creating Degree" << std::endl;
      Degree::Degree *degree = new Degree::Degree(papers, length, degrees, dlength);
      std::cout << "created Degree" << std::endl;
      BAB<Degree::Degree> bab(degree);
      std::cout << "Added to BAB" << std::endl;
      delete degree;
      
      int count = 0;
      std::cout << "searching for solution" << std::endl;
      while(Degree::Degree *d = bab.next()) {
        std::cout << "Count " << count++ << std::endl;
        /*int paper_set[24];
        for(int i = 0; i < 2; i++) {
          paper_set[i] = d->get_paper(i);
          }*/
        /* callback function which should be a 
         * python function allowing solution to 
         * be accesed by python code.
         */
        /*caller(0, paper_set, 24);*/
        d->print();
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

  int deg_cost(IntVarArray p, std::vector<int> papers)
  {
    int result = 0;
    for(int i = 0; i < p.size(); i++) {
      if(p[i].assigned()) {
        for(unsigned j = 0; j < papers.size(); j++) {
          if(p[i].val() == papers[j]) {
            result++;
          }
        }
      }
    }
    return result;
  }


  Degree::Degree(int *papers, 
                 int length,
                 int *deg_papers,
                 int dplength)
    : cost_value(*this, 0, 100),
      degree_papers(*this, 24, IntSet(deg_papers, dplength)),
      paper_list(dplength),
      ar_papers(length)
      
  {
    std::cout << "In constructor with paper length of " << dplength << std::endl;
    
    for(int i = 0; i < dplength; i++) {
      paper_list[i] = deg_papers[i];
    }

    
    for(int i = 0; i < length; i++) {
      ar_papers[i] = papers[i];
      
    }


    
    for(int i = 0; i < 24; i++) {
      rel(*this, degree_papers[i] != 0);
      
          
    }
    
    //at_least_one(*this, ar_papers, degree_papers);
    
  

    //rel(*this, degree == is_valid(degree.assigned() ? degree.val() : -1, NULL, -1, -1));
    //distinct(*this, degree_papers);
    rel(*this, cost_value == deg_cost(degree_papers, ar_papers));

    branch(*this, degree_papers, INT_VAR_NONE, INT_VAL_RND);
    //branch(*this, degree, INT_VAR_SIZE_MIN, INT_VAL_RND);
  }




  Degree::Degree(bool share, Degree &d)
    : MinimiseSpace(share, d),
      paper_list(d.paper_list)
  {
    cost_value.update(*this, share, d.cost_value);
    degree_papers.update(*this, share, d.degree_papers);
    
  }




  Degree::~Degree(void)
  {
    //std::cout << "deleted Degree" << std::endl;
  }




  Space *Degree::copy(bool share)
  {
    return new Degree(share, *this);
  }




  IntVar Degree::cost(void) const
  {
    std::cout << degree_papers << std::endl;
    return cost_value;
  }


  int Degree::get_paper(int pos) const
  {
    //needs to check if is assigned or not
    if(pos > 0 && pos <= 24) {
      return degree_papers[pos].assigned() ? degree_papers[pos].val() : 0;
    }

    return 0;
  }


  void Degree::print(void) const
  {
    std::cout << degree_papers << std::endl;
  }


  int Degree::get_degree(void) const
  {
    return -1;
  }
} // Degree
