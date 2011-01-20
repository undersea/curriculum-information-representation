#ifndef _PROPAGATOR_HPP_
#define _PROPAGATOR_HPP_

#include <gecode/int.hh>


#include <set>


using namespace Gecode;

namespace Degree
{
  class ValidPaper : public Propagator
  {
  public:
    ValidPaper(Space &home, std::vector<int> papers0, Int::IntView paper0);
    ValidPaper(Space& home, bool share, ValidPaper &p);
    virtual ~ValidPaper(void);

    static ExecStatus post(Space& home, 
                           std::vector<int> papers0, Int::IntView paper0){
      (void) new (home) ValidPaper(home, papers0, paper0);
      return ES_OK;
    }
    virtual size_t dispose(Space& home);
    virtual Propagator* copy(Space& home, bool share);
    virtual PropCost cost(const Space&, const ModEventDelta&) const;
    virtual ExecStatus propagate(Space& home, const ModEventDelta&);

    //static void *(*degrees)(int *);
  protected:
    std::vector<int> papers;
    Int::IntView paper;
  private:
  };


  void valid_paper(Space& home, std::vector<int> papers0, IntVar paper0);


  class AtLeastOne : public Propagator
  {
  public:
    AtLeastOne(Space &home, std::vector<int> papers0, 
               ViewArray<Int::IntView> paper0);
    AtLeastOne(Space& home, bool share, AtLeastOne &p);
    //virtual ~AtLeastOne(void);

    static ExecStatus post(Space& home, 
                           std::vector<int> papers0, 
                           ViewArray<Int::IntView> paper0){
      std::printf("post at least one\n");
      (void) new (home) AtLeastOne(home, papers0, paper0);
      return ES_OK;
    }
    virtual size_t dispose(Space& home);
    virtual Propagator* copy(Space& home, bool share);
    virtual PropCost cost(const Space&, const ModEventDelta&) const;
    virtual ExecStatus propagate(Space& home, const ModEventDelta&);

  protected:
    std::vector<int> papers;
    ViewArray<Int::IntView> paper_selection;
  private:
  };



  void at_least_one(Space& home, std::vector<int> papers0, IntVarArray paper0);
} // namespace Degree

extern "C" {
  
  void set_in_degree_function(int (has)(int, int));
}
#endif // _PROPAGATOR_HPP_
