import urllib2

import vertex
import edge

import programme.html.parser as parser

import re

class Tree(object):
    def __init__(self):
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
        self.tree = set()
        self.tmp = None
        
    
    def add_paper(self, paper):
        node = vertex.Vertex(paper)
        self.tree.add(node)
        htmlstr = urllib2.urlopen(self.paperquery_url%(paper)).read()
        result = self.prereq.search(htmlstr)
        if result:
            for pre in (self.code.findall(result.group(0))):
                #make a vertex and add it to node prereq
                vert = self.add_paper(pre)
                node.add_prereq(vert)
        result = self.restricted.search(htmlstr)
        if result:
            for restrict in set(self.code.findall(result.group(0))):
                #just straight string code of paper
                node.add_restriction(restrict)
        
        result = self.coreq.search(htmlstr)
        if result:
            for co in (self.code.findall(result.group(0))):
                #make a vertex and add it to node prereq
                vert = self.add_paper(co)
                node.add_coreq(vert)
        
        return node


    def add_programme(self, programme):
        try:
            papers = parser.get_function(programme)()
        except:
            pass
        else:
            for paper in papers:
                node = self.add_paper(paper)
                self.tree.add(node)

    

    def pprint(self):
        tmp = list(self.tree)
        tmp.sort()
        for paper in tmp:
            inc = (int(paper.id[paper.id.find('.')+1:]) / 100) - 1
            for tab in range(inc):
                print '\t',
            print paper.id



if __name__ == "__main__":
    tree = Tree()
    paper = tree.add_paper('159.302')
    tree.pprint()
