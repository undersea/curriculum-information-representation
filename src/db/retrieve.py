from MySQLdb import connect
import sys
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



<<<<<<< HEAD
def leadsto(paper, planner):
    paper = paper_to_int(paper)
    if paper % 1000 /100 == 3:
        return dict()
    tree = dict()
    sql = "SELECT code FROM paper_prereq WHERE prereq LIKE '%s' or prereq LIKE '%s%%';" % (paper, '%d.%dxx' % (paper/1000, paper%1000/100)) #damn floating point errors
    planner_cursor = planner.cursor()
    try:
        planner_cursor.execute(str(sql))
    except Exception, e:
        print >>sys.stderr, paper, e
        return dict()
    else:
        row = planner_cursor.fetchone()
    
    while row != None:
        try:
            if paper_to_int(row[0]) != paper:
                tree.update({paper_to_int(row[0]):leadsto(row[0], planner)})
        except Exception, e:
            print >>sys.stderr, row, e
        row = planner_cursor.fetchone()

    
=======
def leadsto_dict(paper, record):
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
                tree.update({tmp:leadsto_dict(tmp, record)})
            
        except Exception, e:
            print e
        row = planner_cursor.fetchone()

>>>>>>> bebd23f1df4f65797484ed70e5d8e9c4532bbf1f
    
    planner.close()

    return tree
    



<<<<<<< HEAD
def create_leadsto_set(academic_record):
    planner = connect(host='localhost',
                      user='workload',
                      passwd='workload',
                      db='programme_planner')
=======
def create_leadsto_dict(academic_record):
>>>>>>> bebd23f1df4f65797484ed70e5d8e9c4532bbf1f
    if len(academic_record) == 0:
        return dict()
    record = ['%s.%sxx' % (x/1000, x%1000/100) for x in academic_record]
    pset = dict()
    for paper in academic_record:
<<<<<<< HEAD
        #try:
        papers = leadsto(paper, planner)
        pset.update({paper:papers})
        #except Exception, e:
        #    print >>sys.stderr, paper, e
    planner.close()
=======
        paper = paper_to_int(paper)
        pset.update({paper:leadsto_dict(paper, academic_record)})
>>>>>>> bebd23f1df4f65797484ed70e5d8e9c4532bbf1f

    return pset
            




def get_no_prereq_papers():
    sql = "SELECT code FROM paper_prereq WHERE prereq IS NULL;"
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

    

#turns a dictionary tree into a graph
def tree_to_graph(tree):
    pass


"""
Still need a way of telling if prereq needs to be combined with another before you can do a paper.  Posible using the combo_id column to indicate this. Also either needs to be manually done or the regular expression needs to pick this up from web page.  The problem is that the web page format may be different ot another one, with the english meaning the same thing, but using different words to explain it.  They are not consistent.
"""


if __name__ == '__main__':
<<<<<<< HEAD
    limit = sys.getrecursionlimit()
    #sys.setrecursionlimit(limit*20)
    print sys.getrecursionlimit()
    record = [159101, 159102, 161101, 160102, 158100, 123101, 119177]
    record = [159101, 159102, 161101, 161102, 158100, 119177, 123101]
    print create_leadsto_set(record)
    print get_no_prereq_papers()
=======
    record = [159101, 159102, 161101, 160101, 160102, 158100, 123101, 119177]
    tree = create_leadsto_dict(record)
    print_tree(tree)
    #print get_no_prereq_papers()
>>>>>>> bebd23f1df4f65797484ed70e5d8e9c4532bbf1f
    
