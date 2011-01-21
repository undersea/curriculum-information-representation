#ifndef __MAJOR_HPP__
#define __MAJOR_HPP__

#include <gecode/int.hh>
#include <gecode/minimodel.hh>


#include <map>
#include <vector>

using namespace Gecode;

typedef MinimizeSpace MaximiseSpace

namespace Programme
{
  
  class Major : public MaximiseSpace
  {
  public:
    Major(std::map<string, std::vector<int> > majors);
  protected:

  private:
    BoolVarArray majors;
    std::map<string, int> names_to_pos;
    std::map<int, string> pos_to_names;
    std::map<int, std::vector<int>> major_papers;
  };


} // Programme

#endif // __MAJOR_HPP__
