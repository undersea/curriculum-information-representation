#include "degree.hpp"

#ifdef __cplusplus
extern "C" {
  void run(int *papers, int length, void (caller)(int *, int))
  {
    try {
      Degree::Degree *degree = new Degree::Degree(papers, length);
      BAB<Degree::Degree> bab(degree);
      delete degree;
      int count = 0;
      while(Degree::Degree *d = bab.next()) {
        std::cout << count++ << std::endl;
        int paper_set[24];
        for(int i = 0; i < 24; i++) {
          paper_set[i] = d->get_paper(i);
        }
        caller(paper_set, 24);
        delete d;
        d = NULL;
      }
    } catch(Exception e) {
      std::cerr << e.what() << std::endl;
    }
  }
}
#endif //  __cplusplus

namespace Degree
{

  Degree::Degree(int *papers, int length)
    : cost_value(*this, 0, 100),
      degree_papers(*this, 24, 100100, 999999)
  {
    for(int i = 0; i < length; i++) {
      paper_list.insert(papers[i]);
    }

    

    distinct(*this, degree_papers);
    rel(*this, cost_value == 100);

    branch(*this, degree_papers, INT_VAR_SIZE_MAX, INT_VAL_MAX);
  }




  Degree::Degree(bool share, Degree &degree)
    : MaximiseSpace(share, degree),
      paper_list(degree.paper_list)
  {
    cost_value.update(*this, share, degree.cost_value);
    degree_papers.update(*this, share, degree.degree_papers);
    
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


  int Degree::get_paper(int pos)
  {
    //needs to check if is assigned or not
    return degree_papers[pos].val();
  }
} // Degree
