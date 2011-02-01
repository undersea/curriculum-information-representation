from MySQLdb import connect
#from graph.vertex import Vertex
#from graph.edge import Edge

class PaperNode(object):
    def __init__(self, name, papers):
        self.name = name
        self.leadsto = set(papers)
        

    def __repr__(self):
        return str([self.name, str(self.leadsto)])

def get(paper):
    sql = "SELECT prereq FROM paper_prereq WHERE code LIKE'%s%%';" % (paper)
    planner = connect(host='localhost',
                      user='workload',
                      passwd='workload',
                      db='programme_planner')
    planner_cursor = planner.cursor()
    planner_cursor.execute(sql)
    row = planner_cursor.fetchone()
    papers = set()
    while row != None:
        papers.add(row[0])
        row = planner_cursor.fetchone()
        continue
    
    return papers







def leadsto(paper):
    try:
        paper = int(paper)
    except:
        paper = int(float(paper)*1000)
        
    sql = "SELECT code FROM paper_prereq WHERE prereq LIKE'%s%%' or prereq LIKE '%s%%';" % (paper, '%d.%dxx' % (paper/1000, paper%1000/100)) #damn floating point errors
    planner = connect(host='localhost',
                  user='workload',
                  passwd='workload',
                  db='programme_planner')
    planner_cursor = planner.cursor()
    planner_cursor.execute(sql)
    row = planner_cursor.fetchone()
    papers = set()
    while row != None:
        try:
            papers.add(row[0])
            
        except:
            pass
        row = planner_cursor.fetchone()

    planner.close()
    

    return PaperNode(paper, papers)
    



def create_leadsto_set(academic_record):
    record = ['%s.%sxx' % (x/1000, x%1000/100) for x in academic_record]
    pset = set()
    for paper in academic_record:
        papers = leadsto(paper)
        have = False
        remove = list()
        for p in papers.leadsto:
            have = int(p.name) in academic_record or p in record
            if not have:
                remove.append(p)
        papers.leadsto = set([x for x in papers.leadsto if x in remove])
        pset.add(papers)

    return pset
            




def get_possibles(paper_pattern):
    sql = "SELECT code FROM paper_prereq WHERE code LIKE '%s%%';" % (paper, '%d.%dxx' % (paper/1000, paper%1000/100)) #damn floating point errors
    planner = connect(host='localhost',
                  user='workload',
                  passwd='workload',
                  db='programme_planner')
    planner_cursor = planner.cursor()
    planner_cursor.execute(sql)
    row = planner_cursor.fetchone()
    papers = set()
    while row != None:
        papers.add(row[0])
        row = planner_cursor.fetchone()

    return papers


def get_no_prereq_papers():
    sql = "SELECT code FROM paper_prereq WHERE prereq IS NULL;" #damn floating point errors
    planner = connect(host='localhost',
                  user='workload',
                  passwd='workload',
                  db='programme_planner')
    planner_cursor = planner.cursor()
    planner_cursor.execute(sql)
    row = planner_cursor.fetchone()
    papers = set()
    while row != None:
        papers.add(row[0])
        row = planner_cursor.fetchone()

    return papers


if __name__ == '__main__':
    record = [159101, 159102, 161101, 160101, 160102, 158100, 123101, 119177]
    print create_leadsto_set(record)
    print get_no_prereq_papers()
    
