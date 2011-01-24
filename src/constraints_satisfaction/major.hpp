#ifndef __MAJOR_HPP__
#define __MAJOR_HPP__

#include <gecode/int.hh>
#include <gecode/search.hh>
#include <gecode/minimodel.hh>


#include <map>
#include <vector>
#include <string>

using namespace Gecode;

//typedef MinimizeSpace MaximiseSpace

namespace Programme
{
  
  class Major : public Space
  {
  public:
    Major(std::map<std::string, std::vector<int> > majors0,
          std::vector<int> paper_record0);
    Major(bool share, Major &m);
    virtual Space *copy(bool share);
    virtual void constrain(const Space &_b);
  protected:

  private:
    IntVarArray majors;
    std::map<std::string, int> name_to_pos;
    std::map<int, std::string> pos_to_name;
    std::map<int, std::vector<int>> major_papers;
    std::vector<int> paper_record;
  };


} // Programme

#endif // __MAJOR_HPP__
