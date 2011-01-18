#ifndef _DEGREE_HPP_
#define _DEGREE_HPP_

#include "Python.h"

#include <gecode/int.hh>
#include <gecode/search.hh>
#include <gecode/minimodel.hh>


#include <set>

using namespace Gecode;


typedef MaximizeSpace MaximiseSpace;

typedef struct
{
  int paper;
  int *prerequites;
  int prereq_len;
  int *corequisites;
  int coreq_len;
  int *restrictions;
  int restrict_len;
} Dependencies;


typedef struct
{
  int *papers;
  int plength;
  int *major;
  int mlength;
} DegreePapers;


namespace Degree
{
  class Degree : public MaximiseSpace
  {
  public:
    Degree(int *papers, 
           int length,
           int *degrees,
           int dlength,
           void *(valid_papers)(int, int*));
    Degree(bool share, Degree &degree);
    ~Degree(void);

    virtual Space *copy(bool share);
    

    //cost function needed for MaximiseSpace
    virtual IntVar cost(void) const;
    
    int get_paper(int pos) const;
    int get_degree(void) const;
  protected:
    IntVar cost_value;
    IntVarArray degree_papers;
    IntVar degree;

    std::set<int> paper_list;
    DegreePapers *degree_schedule;

  private:
    
  };
} //namespace Degree


#ifdef __cplusplus
extern "C" {
  void run(int *papers,
           int length,
           int *degrees,
           int dlength,
           void (caller)(int, int *, int), 
           void *(is_valid)(int, int *));
  //int get_paper(Degree::Degree &degree, int &pos);
}
#endif //  __cplusplus


#endif // _DEGREE_HPP_
