#include "propagator.hpp"

extern "C" {
  int (*in_degree)(int degree, int paper);
  void set_in_degree_function(int (has)(int, int))
  {
    in_degree = has;
  }
}

namespace Degree
{
  ValidPaper::ValidPaper(Space &home, Int::IntView degree0, Int::IntView paper0)
    : Propagator(home),
      degree(degree0),
      paper(paper0)
  {
    std::cout << "ValidPaper constructor\n";
    degree.subscribe(home, *this, Int::PC_INT_DOM);
    paper.subscribe(home, *this, Int::PC_INT_DOM);
  }

  ValidPaper::ValidPaper(Space &home, bool share, ValidPaper &p)
    : Propagator(home, share, p)
  {
    degree.update(home, share, p.degree);
    paper.update(home, share, p.paper);
  }

  ValidPaper::~ValidPaper(void)
  {

  }


  size_t ValidPaper::dispose(Space& home)
  {
    degree.cancel(home,*this,Int::PC_INT_DOM);
    paper.cancel(home,*this,Int::PC_INT_DOM);
    (void) Propagator::dispose(home);

    return sizeof(*this);
  }


  Propagator* ValidPaper::copy(Space& home, bool share)
  {
    return new (home) ValidPaper(home,share,*this);
  }



  PropCost ValidPaper::cost(const Space&, const ModEventDelta&) const {
    return PropCost::linear(PropCost::HI, 24);
  }


  ExecStatus ValidPaper::propagate(Space& home, const ModEventDelta&)  {
    if (degree.assigned() && paper.assigned())
      if(in_degree != NULL) {
        std::cout << "In degree not NULL\n";
        if(in_degree(degree.val(), paper.val())) {
          return home.ES_SUBSUMED(*this); 
        } else {
          return ES_FAILED;
        }
      }

    return ES_NOFIX;
  }


  void valid_paper(Space& home, IntVar degree0, IntVar paper0)
  {
    Int::IntView degree(degree0), paper(paper0);
    if (ValidPaper::post(home,degree,paper) != ES_OK)
      home.fail();
  }
} // namespace Degree
