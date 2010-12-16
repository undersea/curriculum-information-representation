#include "one_of_propagator.hpp"


OneOf::OneOf(Home home, ViewArray<Int::IntView> &degree, Int::IntView paper)
  : MixNaryOnePropagator<Int::IntView, Int::PC_INT_BND>(home, degree, paper)
{
}


static ExecStatus OneOf::post(Home home,
                              ViewArray<Int::IntView> &degree,
                              Int::IntView paper)
{

}

OneOf::OneOf(Space &home, bool share, OneOf &p)
  : MixNaryOneProagator<Int::IntView, Int::PC_INT_BND>(home, share, p)
{
}

virtual Propagator* OneOf::copy(Space& home, bool share)
{

}

virtual ExecStatus OneOf::propagate(Space& home, const ModEventDelta&)
{

}

void oneof(Home home, ViewArray<Int::IntView> &degree, Int::IntView paper)
{

}
