#ifndef _DEGREE_HPP_
#define _DEGREE_HPP_

#include "Python.h"

#include <gecode/int.hh>
#include <gecode/search.hh>
#include <gecode/minimodel.hh>


#include <set>

using namespace Gecode;


typedef MaximizeSpace MaximiseSpace;


namespace Degree
{
  class Degree : public MaximiseSpace
  {
  public:
    Degree(int *papers, int length);
    Degree(bool share, Degree &degree);
    ~Degree(void);

    virtual Space *copy(bool share);
    

    //cost function needed for MaximiseSpace
    virtual IntVar cost(void) const;
    
    int get_paper(int pos);
    
  protected:
    IntVar cost_value;
    IntVarArray degree_papers;
    std::set<int> paper_list;

  private:
    
  };
} //namespace Degree


#ifdef __cplusplus
extern "C" {
  void run(int *papers, int length, void (caller)(int *, int));
  int get_paper(Degree::Degree &degree, int &pos);
}
#endif //  __cplusplus


#endif // _DEGREE_HPP_
