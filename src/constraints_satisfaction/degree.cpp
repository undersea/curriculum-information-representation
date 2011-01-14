#include "degree.hpp"

#ifdef __cplusplus
extern "C" {
void run(int *papers, int length, void (caller)(int *, int))
{
  std::cout << "before" << std::endl;
  Degree::Degree *degree = new Degree::Degree(papers, length);
  std::cout << "after" << std::endl;
  BAB<Degree::Degree> bab(degree);
  std::cout << "after 2" << std::endl;
  delete degree;
  while(Degree::Degree *d = bab.next()) {
    int paper_set[24];
    for(int i = 0; i < 24; i++) {
      paper_set[i] = d->get_paper(i);
    }
    caller(paper_set, 24);
  }
}
}
#endif //  __cplusplus

namespace Degree
{

  Degree::Degree(int *papers, int length)
    : cost_value(*this, 0, 100),
      degree_papers(*this, 24, 100000, 999999)
  {
    for(int i = 0; i < length; i++) {
      paper_list.insert(papers[i]);
    }
    distinct(*this, degree_papers);
    rel(*this, cost_value == 10);

    branch(*this, degree_papers, INT_VAR_RND, INT_VALUES_MIN);
  }




  Degree::Degree(bool share, Degree &degree)
    : MaximiseSpace(share, degree),
      paper_list(degree.paper_list)
  {
    //cost_value.update(*this, share, degree.cost_value);
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
