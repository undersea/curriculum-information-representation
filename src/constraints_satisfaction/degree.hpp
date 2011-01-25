#ifndef __DEGREE_HPP__
#define __DEGREE_HPP__

#include "major.hpp"


namespace Programme
{
  class Degree : public Space
  {
  public:
    Degree(std::map<int, std::map<int, std::vector<int> > > &degrees0,
           std::vector<int> &paper_record0);
    Degree(bool share, Degree &d);
    virtual Space *copy(bool share);
    virtual void constrain(const Space &_b);
    void print(void) const;
    int *get(void) const;
  protected:
    std::map<int, std::map<int, std::vector<int> > > degrees;
    std::vector<int> paper_record;
    IntVar degree;
  private:
  };
} // namespace Programme


#endif // __DEGREE_HPP__
