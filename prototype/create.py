#!/usr/bin/env python

import re, string

def degree_constraint(degree, papers):
    papers = string.join(papers, ' ')
    def filter_papers(it, papers=papers):
        if re.match(it, papers):
            return True
        return False
    tmp = map(filter_papers, degree)
    print (tmp)
    return sum(tmp)/float(len(tmp))




def major_constraint(major, papers):
    papers = string.join(papers, ' ')
    def filter_papers(it, papers=papers):
        if re.match(it, papers):
            return True
        return False

    tmp = map(filter_papers, major)
    print (tmp)
    return sum(tmp)/float(len(tmp))




if __name__ == "__main__":
    degree = ['.*1591\d{2}', '.*1611\d{2}', '.*1601\d{2}', '.*1581\d{2}']
    major = ['.*159101', '.*159102', '.*159201', '.*159202']
    papers = ['159101', '134123','159202']
    print ((degree_constraint(degree, papers)+major_constraint(major, papers))/2.0)
else:
    print ("Can't be run as a module")
