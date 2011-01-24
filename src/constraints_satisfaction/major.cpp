#include "major.hpp"

#include <algorithm>

inline void run_search(std::map<int, std::vector<int> > majors,
                std::vector<int> papers)
{
  Programme::Major *major = new Programme::Major(majors, papers);
  DFS<Programme::Major> e(major);
  delete major;
  major = NULL;

  while(Programme::Major *m = e.next()) {
    m->print();
    delete m;
    m = NULL;
  }
}

extern "C" {
  void run(int *majors, int mdsize[2],
           int *papers, int size)
  {
    std::map<int, std::vector<int> > majors_map;
    for(int i = 0; i < mdsize[0]; i++) {
      std::vector<int> paper_list(mdsize[1]);
      for(int j = 0; j < mdsize[1]; j++) {
        paper_list[j] = majors[(i*mdsize[0]) + j];
        std::printf("%6d\n", majors[(i*mdsize[0]) + j]);
      }
      majors_map[i] = paper_list;
    }
    
    std::vector<int> paper_list(size);
    for(int i = 0; i < size; i++) {
      paper_list[i] = papers[i];
    }

    run_search(majors_map, paper_list);
  }
}


namespace Programme
{
  Major::Major(std::map<int, std::vector<int> > majors0,
               std::vector<int> paper_record0)
    : majors(*this, majors0.size(), 0, 1000),
      m(*this, 0, paper_record.size()),
      paper_record(paper_record0)
  {
    //set up database
    std::map<int, std::vector<int> >::iterator it;
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
      BoolVarArray papers(*this, paper_record.size(), 0, 1);
      //for each paper in record see if it is in the major schedule
      for(int j = 0; j < papers.size(); j++) {
        std::vector<int>::iterator it = std::find(major_papers[i].begin(), major_papers[i].end(), paper_record[j]);
        rel(*this, papers[j] == (it != major_papers[i].end()));
      }
            
      //sum up the number of major schedule papers that have been done
      rel(*this, majors[i] == sum(papers));
    }

    //rel(*this, m == max(majors));
  }


  Major::Major(bool share, Major::Major &m)
    : Space(share, m),
      name_to_pos(m.name_to_pos),
      pos_to_name(m.pos_to_name),
      major_papers(m.major_papers),
      paper_record(m.paper_record)
  {
    this->m.update(*this, share, m.m);
    majors.update(*this, share, m.majors);
  }


  Space *Major::copy(bool share)
  {
    return new Major::Major(share, *this);
  }

  /*
   * For the moment this is redundant, as the search space is determined 
   * at the start and doesn't change.  If a degree var was added and 
   * majors changed accordingly then this would be useful.
   * The only problem is that the number of majors are different with
   * each degree.
   */
  void Major::constrain(const Space &_major)
  {
    const Major& major = static_cast<const Major&>(_major);
    
    rel(*this, sum(majors) > sum(major.majors));
  }



  void Major::print(void) const
  {
    std::cout << "Major Values\n";
    std::cout << majors << std::endl;
  }
} // namespace Programme

