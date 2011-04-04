#include "degree.hpp"


namespace Programme
{
  Degree::Degree(std::map<int, std::map<int, std::vector<int> > > &degrees0,
                 std::vector<int> &paper_record0)
    : degrees(degrees0),
      paper_record(paper_record0),
      degree(*this, 0, degrees0.size()),
      major(*this, 0, 1000),
      degree_weights(*this, degrees0.size(), 0, 100)
  {
    process_degrees();
    IntVar max_value(*this, 0, 100);
    rel(*this, max_value == max(degree_weights));

    for(int i = 0; i < degree_weights.size(); i++) {
      
    }
    
  }
} // Programme
