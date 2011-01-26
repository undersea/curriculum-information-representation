import re
from ctypes import *
import urllib2

class Paper(object):
    def __init__(self):
        self.paperquery_url = 'http://www.massey.ac.nz/massey/learning/programme-course-paper/paper.cfm?paper_code=%s'
        self.codestr = '\d{3}\.\d{1}\w{2}'
        self.code = re.compile(self.codestr)
        self.code_link_pattern = '<a href="\?paper_code=%s" title="%s">%s</a>'%(self.codestr, self.codestr, self.codestr)
        self.code_meta_specific_pattern = '\w*\s*\d{3}.\w{3}\s*paper'
        #<li><b>Prerequisite(s):</b> <a href="?paper_code=159.101" title="159.101">159.101</a>, <a href="?paper_code=159.102" title="159.102">159.102</a> (or <a href="?paper_code=159.101" title="159.101">159.101</a> taken prior to 2003)</li>
        self.pattern = '\(s\):</b>\s*(%s[\s,]*|%s[\s,]*)*(\s*or\s*(%s[\s,]*|%s[\s,]*))*\s*(\(\s*or\s*%s\s*taken\s*prior\s*to\s*\d{4}\))*</li>'%(self.code_link_pattern, self.code_meta_specific_pattern, self.code_link_pattern, self.code_meta_specific_pattern, self.code_link_pattern)
        self.pattern2 = '\(s\):</b>.*\d{3}\.\d{1}[xyz]{2}.*</li><li><b>Restriction\(s\):'
        
        self.restricted = re.compile('<li><b>Restriction(%s)'% (self.pattern))
        self.prereq = re.compile('<li><b>Prerequisite((%s)|(%s))'%(self.pattern, self.pattern2))
        self.coreq = re.compile('<li><b>Corequisite%s'%(self.pattern))
        self.or_pattern = re.compile('(%s\s*or\s*)+(%s)*'%(self.code_link_pattern,self.code_link_pattern))

        self.prereq_set = set()
        self.coreq_set = set()
        self.restriction_set = set()


    def __call__(self, paper):
        self.paper = paper #so the paper code can be retrieved
        htmlstr = urllib2.urlopen(self.paperquery_url%(paper)).read()
        result = self.prereq.search(htmlstr)
        if result:
            for pre in (self.code.findall(result.group())):
                #add it to prereq
                self.prereq_set.add(pre)
            self.prereq_array = (c_int * len(self.prereq_set))()
            for pos in range(self.prereq_set):
                self.prereq_array[pos] = self.prereq_set[pos]
            self.prerequites = self.prereq_array
            self.prereq_len = len(self.prereq_array)
                
        result = self.restricted.search(htmlstr)
        if result:
            for restrict in set(self.code.findall(result.group(0))):
                #just straight string code of paper
                self.restriction_set.add(restrict)
            self.restrict_array = (c_int * len(self.restriction_set))()
            for pos in range(self.restriction_set):
                self.restrict_array[pos] = self.restriction_set[pos]
            self.restrictions = self.restrict_array
            self.restrict_len = len(self.restrict_array)
        
        result = self.coreq.search(htmlstr)
        if result:
            for co in (self.code.findall(result.group(0))):
                #add it to coreq
                self.coreq_set.add(co)
            self.coreq_array = (c_int * len(self.coreq_set))()
            for pos in range(self.coreq_set):
                self.coreq_array[pos] = self.coreq_set[pos]
            self.corequisites = self.coreq_array
            self.coreq_len = len(self.coreq_array)

        return pointer(self)


