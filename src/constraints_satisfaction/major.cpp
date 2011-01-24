#include "major.hpp"

#include <algorithm>


extern "C" {
  void run(void);
}


namespace Programme
{
  bool papers_equal(int p1, int p2)
  {
    return p1 == p2;
  }

  Major::Major(std::map<std::string, std::vector<int> > majors0,
               std::vector<int> paper_record0)
    : majors(*this, majors0.size(), 0, 1000),
      paper_record(paper_record0)
  {
    //set up database
    std::map<std::string, std::vector<int> >::iterator it;
    int i = 0;
    for(it = majors0.begin();
        it != majors0.end();
        i++, it++) {
      name_to_pos[it->first] = i;
      pos_to_name[i] = it->first;
      major_papers[i] = it->second;
    }


    //specify the constraints
    for(i = 0; i < majors.size(); i++) {
      BoolArgs papers(paper_record.size());
      for(int j = 0; j < papers.size(); j++) {
        std::vector<int>::iterator it = std::find(major_papers[i].begin(), major_papers[i].end(), paper_record[i]);
        rel(*this, papers[j] == (it != major_papers[i].end()));
      }
      rel(*this, majors[i] == sum(papers));
    }
  }

  void Major::constrain(const Space &_major)
  {
    const Major& major = static_cast<const Major&>(_major);
    
    rel(*this, sum(majors) > sum(major.majors));
  }

} // namespace Programme

