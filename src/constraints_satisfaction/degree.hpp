#ifndef _DEGREE_HPP_
#define _DEGREE_HPP_

#include "Python.h"

#include <gecode/int.hh>
#include <gecode/search.hh>
#include <gecode/minimodel.hh>


#include <vector>

using namespace Gecode;


typedef MaximizeSpace MaximiseSpace;
typedef MinimizeSpace MinimiseSpace;

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
  class Degree : public MinimiseSpace
  {
  public:
    Degree(int *papers, 
           int length,
           int *deg_papers,
           int dplength);
    Degree(bool share, Degree &degree);
    ~Degree(void);

    virtual Space *copy(bool share);
    

    //cost function needed for MaximiseSpace
    virtual IntVar cost(void) const;

    void print(void) const;    

    int get_paper(int pos) const;
    int get_degree(void) const;
  protected:
    IntVar cost_value;
    IntVarArray degree_papers;
    //IntVar degree;

    std::vector<int> paper_list;
    //DegreePapers *degree_schedule;
    std::vector<int> ar_papers;
  private:
    
  };
} //namespace Degree


#ifdef __cplusplus
extern "C" {
  void run(int *papers,
           int length,
           int *degrees,
           int dlength,
           void (caller)(int, int *, int))/*, 
           void *(is_valid)(int, int *))*/;
  //int get_paper(Degree::Degree &degree, int &pos);
}
#endif //  __cplusplus


#endif // _DEGREE_HPP_
