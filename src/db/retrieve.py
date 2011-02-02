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

    planner.close()
    
    return papers


def paper_to_int(paper):
    if isinstance(paper, str):
        if '.' in paper:
            if not paper.lower().endswith('xx'):
                return False
            return int(float(paper)*1000)
        return int(paper)
    elif isinstance(paper, float):
        return int(paper * 1000)
    elif isinstance(paper, int):
        return paper



def leadsto(paper, record):
    if isinstance(record, list):
        record = set(record)
    paper = paper_to_int(paper)        
    sql = "SELECT code FROM paper_prereq WHERE prereq LIKE '%s' or prereq LIKE '%s%%';" % (paper, '%d.%dxx' % (paper/1000, paper%1000/100)) #damn floating point errors
    planner = connect(host='localhost',
                      user='workload',
                      passwd='workload',
                      db='programme_planner')
    planner_cursor = planner.cursor()
    planner_cursor.execute(sql)
    
    row = planner_cursor.fetchone()
    tree = dict()
    while row != None:
        try:
            tmp = paper_to_int(row[0])
            if tmp != paper and tmp not in record:
                tree.update({tmp:leadsto(tmp, record)})
            
        except Exception, e:
            print e
        row = planner_cursor.fetchone()

    
    planner.close()

    return tree
    



def create_leadsto_set(academic_record):
    if len(academic_record) == 0:
        return set()
    record = ['%s.%sxx' % (x/1000, x%1000/100) for x in academic_record]
    pset = dict()
    for paper in academic_record:
        paper = paper_to_int(paper)
        pset.update({paper:leadsto(paper, academic_record)})

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



def print_tree(tree, level=0):
    for key in tree:
        for x in range(level):
            print '    ',
        print '+', key
        print_tree(tree[key], level+1)

    


if __name__ == '__main__':
    record = [159101, 159102, 161101, 160101, 160102, 158100, 123101, 119177]
    print_tree(create_leadsto_set(record))
    #print get_no_prereq_papers()
    
