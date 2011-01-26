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
