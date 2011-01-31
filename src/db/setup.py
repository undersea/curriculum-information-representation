from MySQLdb import connect
from paper import Paper
from degreeparser import extract_papers, get_data


"""
This all assumes that the database has been created along with all its tables
"""
def setup():
#    workload = connect(host='localhost',
#                       user='workload',
#                       passwd='workload',
#                       db='workload')
#    workload_cursor = workload.cursor()

#    papers = list()
#
#    workload_cursor.execute("SELECT code FROM db_paper")
#    row = workload_cursor.fetchone()
#    while row != None:
#        papers.append(row[0])
#        row = workload_cursor.fetchone()

    url = 'http://www.massey.ac.nz/massey/about-massey/calendar/degree-diploma-and-certificate-regulations/college-of-sciences/en/bachelor-of-science.cfm'
    papers = [int(float(x)*1000) for x in extract_papers(get_data(url))]
    url2 = 'http://www.massey.ac.nz/massey/about-massey/calendar/degree-diploma-and-certificate-regulations/college-of-sciences/en/bachelor-of-information-sciences.cfm'
    papers2 = [int(float(x)*1000) for x in extract_papers(get_data(url2))]

    papers = list(set(papers + papers2))


    planner = connect(host='localhost',
                      user='workload',
                      passwd='workload',
                      db='programme_planner')
    planner_cursor = planner.cursor()

    sql = "DROP TABLE IF EXISTS paper_prereq;"
    print sql
    planner_cursor.execute(sql)

    sql = """CREATE TABLE paper_prereq
             (
                   id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
                   code VARCHAR(8) NOT NULL,
                   combo_id INTEGER,
                   prereq VARCHAR(8)
             );
          """
    print sql
    planner_cursor.execute(sql)

    combo_id = 0
    sql = 'delete from paper_prereq;'
    print sql
    planner_cursor.execute(sql)

    for paper in papers:
        try:
            dep = Paper()
            dep(paper)
            if len(dep.prereq_set) > 0:
                if len(dep.prereq_set) > 1:
                    combo_id += 1
                for inst in dep.prereq_set:
                    try:
                        inst = str(int(float(inst)*1000))
                    except:
                        inst = str(inst)
                    if len(dep.prereq_set) > 1:
                        sql = "INSERT INTO paper_prereq VALUES(0, '%s', %d, '%s');" % (str(paper), combo_id, inst)
                        print sql
                        planner_cursor.execute(sql)
                    else:
                        sql = "INSERT INTO paper_prereq VALUES(0, '%s', NULL, '%s');" % (str(paper), inst)
                        print sql
                        planner_cursor.execute(sql)
            else:
                sql = "INSERT INTO paper_prereq VALUES(0, '%s', NULL, NULL);" % (str(paper))
                print sql
                planner_cursor.execute(sql)
        except Exception, e:
            print e

"""
create database programme_planner;
use programme_planner;
create table paper_prereq
(
  id integer not null auto_increment primary key,
  code integer not null,
  combo_id integer,
  prereq integer
);
GRANT ALL PRIVILEGES ON programme_planner.* TO workload @'%';
"""
if __name__ == "__main__":
    setup()
