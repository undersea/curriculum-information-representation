#ifndef ONE_OF_PROPAGATOR_HPP
#define ONE_OF_PROPAGATOR_HPP

#include <gecode/int.hh>

using namespace Gecode;


class OneOf : MixNaryOnePropagator<Int::IntView, Int::PC_INT_BND>
{
public:
  OneOf(Home home, ViewArray<Int::IntView> &degree, Int::IntView paper);
  static ExecStatus post(Home home,
                         ViewArray<Int::IntView> &degree,
                         Int::IntView paper);
  OneOf(Space &home, bool share, OneOf &p);
  virtual Propagator* copy(Space& home, bool share);
  virtual ExecStatus propagate(Space& home, const ModEventDelta&);
  
protected:
private:
};


void oneof(Home home, ViewArray<Int::IntView> &degree, Int::IntView paper);


#endif //ONE_OF_PROPAGATOR_HPP
