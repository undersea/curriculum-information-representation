from MySQLdb import connect


conn = connect(host='localhost',
               user='workload',
               passwd='workload',
               db='programme_planner')
cursor = conn.cursor()
cursor.execute('SELECT * FROM paper_prereq')
row = cursor.fetchone()
while row != None:
    print row
    row = cursor.fetchone()
"""
create table paper_prereq
(
  id integer not null auto_increment,
  code integer not null,
  combo_id integer,
  prereq integer
);
GRANT ALL PRIVILEGES ON programme_planner.* TO workload @'%';
"""
