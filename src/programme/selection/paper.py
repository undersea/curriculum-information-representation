import re

class Paper(object):
    def __init__(self, code):
        self.paper = code
        self.paperquery_url = 'http://www.massey.ac.nz/massey/learning/programme-course-paper/paper.cfm?paper_code=%s'
        self.codestr = '\d{3}\.\d{3}'
        self.code = re.compile(self.codestr)
        self.code_link_pattern = '<a href="\?paper_code=%s" title="%s">%s</a>'%(self.codestr, self.codestr, self.codestr)
        self.code_meta_specific_pattern = '\w*\s*\d{3}.\w{3}\s*paper'
        #<li><b>Prerequisite(s):</b> <a href="?paper_code=159.101" title="159.101">159.101</a>, <a href="?paper_code=159.102" title="159.102">159.102</a> (or <a href="?paper_code=159.101" title="159.101">159.101</a> taken prior to 2003)</li>
        self.pattern = '\(s\):</b>\s*(%s[\s,]*|%s[\s,]*)*(\s*or\s*(%s[\s,]*|%s[\s,]*))*\s*(\(\s*or\s*%s\s*taken\s*prior\s*to\s*\d{4}\))*</li>'%(self.code_link_pattern, self.code_meta_specific_pattern, self.code_link_pattern, self.code_meta_specific_pattern, self.code_link_pattern)
        
        self.restricted = re.compile('<li><b>Restriction%s'% (self.pattern))
        self.prereq = re.compile('<li><b>Prerequisite%s'%(self.pattern))
        self.coreq = re.compile('<li><b>Corequisite%s'%(self.pattern))
        self.or_pattern = re.compile('(%s\s*or\s*)+(%s)*'%(self.code_link_pattern,self.code_link_pattern))

        self.prereq_set = set()
        self.coreq_set = set()
        self.restriction_set = set()


    def __call__(self):
        htmlstr = urllib2.urlopen(self.paperquery_url%(self.paper)).read()
        result = self.prereq.search(htmlstr)
        if result:
            for pre in (self.code.findall(result.group(0))):
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
                node.coreq_set.add(co)



p = Paper(159201)
p()
print p.prereq_set, p.coreq_set, p.restriction_set
