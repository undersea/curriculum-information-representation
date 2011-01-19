#ifndef _PROPAGATOR_HPP_
#define _PROPAGATOR_HPP_

#include <gecode/int.hh>

using namespace Gecode;

namespace Degree
{
  class ValidPaper : public Propagator
  {
  public:
    ValidPaper(Space &home, Int::IntView degree0, Int::IntView paper0);
    ValidPaper(Space& home, bool share, ValidPaper &p);
    virtual ~ValidPaper(void);

    static ExecStatus post(Space& home, 
                           Int::IntView degree0, Int::IntView paper0){
      (void) new (home) ValidPaper(home, degree0, paper0);
      return ES_OK;
    }
    virtual size_t dispose(Space& home);
    virtual Propagator* copy(Space& home, bool share);
    virtual PropCost cost(const Space&, const ModEventDelta&) const;
    virtual ExecStatus propagate(Space& home, const ModEventDelta&);
  protected:
    Int::IntView degree, paper;
  private:
  };


  void valid_paper(Space& home, IntVar degree0, IntVar paper0);
} // namespace Degree

extern "C" {
  
  void set_in_degree_function(int (has)(int, int));
}
#endif // _PROPAGATOR_HPP_
