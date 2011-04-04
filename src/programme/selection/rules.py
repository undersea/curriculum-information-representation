from programme import *

def find_relevant_degree(papers):
    global degrees
    for key in degrees:
        degrees[key](papers)



find_relevant_degree([159101, 159102, 160101, 160102, 192101, 158100, 161101])
for key in degrees:
    print key, degrees[key].value
