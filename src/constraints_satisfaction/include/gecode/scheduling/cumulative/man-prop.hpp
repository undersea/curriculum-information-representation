/* -*- mode: C++; c-basic-offset: 2; indent-tabs-mode: nil -*- */
/*
 *  Main authors:
 *     Christian Schulte <schulte@gecode.org>
 *
 *  Copyright:
 *     Christian Schulte, 2009
 *
 *  Last modified:
 *     $Date: 2010-07-15 12:39:29 +0200 (Thu, 15 Jul 2010) $ by $Author: tack $
 *     $Revision: 11199 $
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

namespace Gecode { namespace Scheduling { namespace Cumulative {
  
  template<class ManTask>
  forceinline
  ManProp<ManTask>::ManProp(Home home, int c0, TaskArray<ManTask>& t)
    : TaskProp<ManTask,Int::PC_INT_DOM>(home,t), c(c0) {}

  template<class ManTask>
  forceinline
  ManProp<ManTask>::ManProp(Space& home, bool shared, 
                            ManProp<ManTask>& p) 
    : TaskProp<ManTask,Int::PC_INT_DOM>(home,shared,p), c(p.c) {}

  template<class ManTask>
  forceinline ExecStatus 
  ManProp<ManTask>::post(Home home, int c, TaskArray<ManTask>& t) {
    // Check that tasks do not overload resource
    for (int i=t.size(); i--; )
      if (t[i].c() > c)
        return ES_FAILED;
    if (t.size() > 1)
      (void) new (home) ManProp<ManTask>(home,c,t);
    return ES_OK;
  }

  template<class ManTask>
  Actor* 
  ManProp<ManTask>::copy(Space& home, bool share) {
    return new (home) ManProp<ManTask>(home,share,*this);
  }

  template<class ManTask>  
  forceinline size_t 
  ManProp<ManTask>::dispose(Space& home) {
    (void) TaskProp<ManTask,Int::PC_INT_DOM>::dispose(home);
    return sizeof(*this);
  }

  template<class ManTask>
  ExecStatus 
  ManProp<ManTask>::propagate(Space& home, const ModEventDelta& med) {
    // Only bounds changes?
    if (Int::IntView::me(med) != Int::ME_INT_DOM)
      GECODE_ES_CHECK(overload(home,c,t));
    GECODE_ES_CHECK(edgefinding(home,c,t));
    return basic(home,*this,c,t);
  }

}}}

// STATISTICS: scheduling-prop
