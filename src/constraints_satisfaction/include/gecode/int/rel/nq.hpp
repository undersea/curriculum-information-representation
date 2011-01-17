/* -*- mode: C++; c-basic-offset: 2; indent-tabs-mode: nil -*- */
/*
 *  Main authors:
 *     Christian Schulte <schulte@gecode.org>
 *
 *  Copyright:
 *     Christian Schulte, 2004
 *
 *  Last modified:
 *     $Date: 2010-03-03 17:32:21 +0100 (Wed, 03 Mar 2010) $ by $Author: schulte $
 *     $Revision: 10364 $
 *
 *  This file is part of Gecode, the generic constraint
 *  development environment:
 *     http://www.gecode.org
 *
 *  Permission is hereby granted, free of charge, to any person obtaining
 *  a copy of this software and associated documentation files (the
 *  "Software"), to deal in the Software without restriction, including
 *  without limitation the rights to use, copy, modify, merge, publish,
 *  distribute, sublicense, and/or sell copies of the Software, and to
 *  permit persons to whom the Software is furnished to do so, subject to
 *  the following conditions:
 *
 *  The above copyright notice and this permission notice shall be
 *  included in all copies or substantial portions of the Software.
 *
 *  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
 *  EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
 *  MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
 *  NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
 *  LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
 *  OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
 *  WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
 *
 */

namespace Gecode { namespace Int { namespace Rel {

  /*
   * Disequality
   *
   */
  template<class View>
  forceinline
  Nq<View>::Nq(Home home, View x0, View x1)
    : BinaryPropagator<View,PC_INT_VAL>(home,x0,x1) {}

  template<class View>
  ExecStatus
  Nq<View>::post(Home home, View x0, View x1){
    if (x0.assigned()) {
      GECODE_ME_CHECK(x1.nq(home,x0.val()));
    } else if (x1.assigned()) {
      GECODE_ME_CHECK(x0.nq(home,x1.val()));
    } else if (same(x0,x1)) {
      return ES_FAILED;
    } else {
      (void) new (home) Nq<View>(home,x0,x1);
    }
    return ES_OK;
  }

  template<class View>
  forceinline
  Nq<View>::Nq(Space& home, bool share, Nq<View>& p)
    : BinaryPropagator<View,PC_INT_VAL>(home,share,p) {}

  template<class View>
  Actor*
  Nq<View>::copy(Space& home, bool share) {
    return new (home) Nq<View>(home,share,*this);
  }

  template<class View>
  PropCost
  Nq<View>::cost(const Space&, const ModEventDelta&) const {
    return PropCost::unary(PropCost::LO);
  }

  template<class View>
  ExecStatus
  Nq<View>::propagate(Space& home, const ModEventDelta&) {
    if (x0.assigned()) {
      GECODE_ME_CHECK(x1.nq(home,x0.val()));
    } else {
      GECODE_ME_CHECK(x0.nq(home,x1.val()));
    }
    return home.ES_SUBSUMED(*this);
  }

}}}

// STATISTICS: int-prop
