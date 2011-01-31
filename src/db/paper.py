import re
import urllib2
from lxml import etree
from cStringIO import StringIO
from scheduleparser import fix_html

#use xpath it's a lot less messy

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
        self.pattern3 = '\(s\):</b>.*\d{3}\.\d{3}.*</li>.*<li><b>'
        
        self.restricted = re.compile('<li><b>Restriction(%s)'% (self.pattern))
        self.prereq = re.compile('<li><b>Prerequisite((%s)|(%s)|(%s))'%(self.pattern, self.pattern2, self.pattern3))
        self.coreq = re.compile('<li><b>Corequisite%s'%(self.pattern))
        self.or_pattern = re.compile('(%s\s*or\s*)+(%s)*'%(self.code_link_pattern,self.code_link_pattern))

        self.prereq_set = set()
        self.coreq_set = set()
        self.restriction_set = set()


    def __call__(self, paper):
        self.paper = paper #so the paper code can be retrieved

        sock = urllib2.urlopen(self.paperquery_url%(paper))
        htmlstr = fix_html(sock.read())
        sock.close()

        f = StringIO(htmlstr)
        tree = etree.parse(f)
        #prereqs, coreqs and restrictions are kept 
        #in li tags in the div with id of 'maincontent'
        tmp = tree.getroot().xpath('//xhtml:div[@id="maincontent"]//xhtml:li',  namespaces={'xhtml':'http://www.w3.org/1999/xhtml'})
        result = self.prereq.search(htmlstr)
        if result:
            for pre in (self.code.findall(result.group())):
                #add it to prereq
                self.prereq_set.add(pre)
                
        result = self.restricted.search(htmlstr)
        if result:
            for restrict in set(self.code.findall(result.group(0))):
                #just straight string code of paper
                self.restriction_set.add(restrict)
        
        result = self.coreq.search(htmlstr)
        if result:
            for co in (self.code.findall(result.group(0))):
                #add it to coreq
                self.coreq_set.add(co)





