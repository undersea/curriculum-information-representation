#ifndef __PAPERS_HPP__
#define __PAPERS_HPP__

#include "major.hpp"


namespace Programme
{
  class Papers : public Space
  {
  public:
    Papers(std::map<int, std::vector<int> > &majors0,
           std::vector<int> &paper_record0);
    Papers(bool share, Papers &p);
    virtual Space *copy(bool share);
    virtual void constrain(const Space &_p);
    void print(void) const;
    int *get(void) const;
  private:
    std::map<int, std::vector<int>> major_papers;
    std::vector<int> paper_record;
  protected:
  };
} // Programme


#endif // __PAPERS_HPP__
