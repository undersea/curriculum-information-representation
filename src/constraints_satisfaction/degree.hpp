#ifndef _DEGREE_HPP_
#define _DEGREE_HPP_

#include "Python.h"

#include <gecode/int.hh>
#include <gecode/search.hh>
#include <gecode/minimodel.hh>

using namespace Gecode;


typedef MaximizeSpace MaximiseSpace


extern "C" {
  void *create_paper_set(void)
  {
    return new std::set<unsigned>();
  }
}


namespace Degree
{
  class Degree : public MaximiseSpace
  {
    Degree(std::set<unsigned> papers, 
  };
} //namespace Degree

#endif // _DEGREE_HPP_
