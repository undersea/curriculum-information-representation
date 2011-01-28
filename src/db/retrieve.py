from MySQLdb import connect
from graph.vertex import Vertex
from graph.edge import Edge

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

    return papers


def leadsto(paper):
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
        papers.add(row[0])
        row = planner_cursor.fetchone()

    return papers
    
def create_leadsto_set(academic_record):
    record = ['%s.%sxx' % (x/1000, x%1000/100) for x in academic_record]
    pset = set()
    for paper in academic_record:
        papers = leadsto(paper)
        have = False
        for p in papers:
            have = int(p) in academic_record or p in record
            if not have:
                pset.add(int(p))
        
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
