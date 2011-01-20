#include "propagator.hpp"

namespace Degree
{
  ValidPaper::ValidPaper(Space &home, std::vector<int> papers0, Int::IntView paper0)
    : Propagator(home),
      papers(papers0),
      paper(paper0)
      
  {
    paper.subscribe(home, *this, Int::PC_INT_VAL);
  }


  ValidPaper::ValidPaper(Space &home, bool share, ValidPaper &p)
    : Propagator(home, share, p),
      papers(p.papers)
  {
    //papers.update(home, share, p.papers);
    paper.update(home, share, p.paper);
  }

  ValidPaper::~ValidPaper(void)
  {

  }


  size_t ValidPaper::dispose(Space& home)
  {
    //papers.cancel(home,*this,Int::PC_INT_VAL);
    paper.cancel(home,*this,Int::PC_INT_VAL);
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
    bool d_valid = false;
    for(unsigned i = 0; i < papers.size(); i++) {
      if(paper.eq(home, papers[i]) != Int::ME_INT_FAILED) {
        d_valid = true;
        break;
      }
    }
    if(!d_valid) {
    
      return ES_FAILED;
    }
  
    if(paper.assigned()) {
      //unsigned pos = -1;
    
      return home.ES_SUBSUMED(*this);
    }
    
      
    

    return ES_NOFIX;
  }


  void valid_paper(Space& home, std::vector<int> papers0, IntVar paper0)
  {
    Int::IntView paper(paper0);
    if (ValidPaper::post(home,papers0,paper) != ES_OK)
      home.fail();
    
  }




  AtLeastOne::AtLeastOne(Space &home, std::vector<int> papers0, 
                         ViewArray<Int::IntView> paper0)
    : Propagator(home),
      papers(papers0),
      paper_selection(paper0)
  {
    paper_selection.subscribe(home, *this, Int::PC_INT_DOM);

  }


  AtLeastOne::AtLeastOne(Space& home, bool share, AtLeastOne &p)
    : Propagator(home, share, p),
      papers(p.papers)
  {
    paper_selection.update(home, share, p.paper_selection);
  }


  /*AtLeastOne::~AtLeastOne(void)
  {

  }*/




  size_t AtLeastOne::dispose(Space& home)
  {
    paper_selection.cancel(home,*this,Int::PC_INT_VAL);
    (void) Propagator::dispose(home);

    return sizeof(*this);
  }




  Propagator* AtLeastOne::copy(Space& home, bool share)
  {
    return new (home) AtLeastOne(home,share,*this);
  }




  PropCost AtLeastOne::cost(const Space&, const ModEventDelta&) const
  {
    return PropCost::linear(PropCost::HI, 24);
  }




  ExecStatus AtLeastOne::propagate(Space& home, const ModEventDelta&)
  {
    bool d_valid = false;
    for(unsigned i = 0; i < papers.size(); i++) {
      for(int j = 0; j < paper_selection.size(); i++) {
        if(paper_selection[j].lq(home, papers[i]) != Int::ME_INT_FAILED && 
           paper_selection[j].gq(home, papers[i]) != Int::ME_INT_FAILED) {
          d_valid = true;
          break;
        }
      }

      if(d_valid) {
        break;
      }
    }

    if(!d_valid) {
      return ES_FAILED;
    }


    d_valid = true;
    for(int i = 0; i < paper_selection.size(); i++) {
      if(!paper_selection[i].assigned()) {
        d_valid = false;
      } else {
        /* 
         * reduce the search space by requiring 
         * the papers to be in order of their level
         *
         */
        if(i > 0 && paper_selection[i-1].assigned() &&
           (paper_selection[i].val() % 1000) < 
          (paper_selection[i-1].val() % 1000)) {
        return ES_FAILED;
      }
    }
  }

  if(d_valid) {
    return home.ES_SUBSUMED(*this);
  }


    

  return ES_NOFIX;
}




  void at_least_one(Space& home, std::vector<int> papers0, IntVarArray paper0)
  {
    ViewArray<Int::IntView> paper(home, IntVarArgs(paper0));
    std::printf("at_least_one\n");
    if (AtLeastOne::post(home,papers0,paper) != ES_OK)
      home.fail();
  }
} // namespace Degree
