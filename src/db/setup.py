from MySQLdb import connect
from paper import Paper
from degreeparser import extract_papers, get_data


"""
This all assumes that the database has been created along with all its tables
"""
def setup():
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
#    sql = 'delete from paper_prereq;'
#    print sql
#    planner_cursor.execute(sql)

    for paper in papers:
        try:
            dep = Paper()
            #this tests to see if paper is actually offered, at same time if it exists parses the doc and extracts prereqs.
            if dep(paper) == False:
                continue
            if len(dep.combo_prereq_list) > 0:
                for combo in dep.combo_prereq_list:
                    combo_id += 1
                    for item in combo:
                        sql = "INSERT INTO paper_prereq VALUES(0, '%s', '%s', '%s');" % (str(paper), str(combo_id), item)
                        print sql
                        planner_cursor.execute(sql)
            if len(dep.prereq_set) > 0:
                for inst in dep.prereq_set:
                    try:
                        inst = str(int(float(inst)*1000))
                    except:
                        inst = str(inst)
            
                        
                    
                    sql = "INSERT INTO paper_prereq VALUES(0, '%s', NULL, '%s');" % (str(paper), inst)
                    print sql
                    planner_cursor.execute(sql)
            elif len(dep.combo_prereq_list) == 0:
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
