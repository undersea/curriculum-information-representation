import urllib2

import vertex
import edge

import programme.html.parser as parser

import re

class Tree(object):
    def __init__(self, programme):
        self.paperquery_url = 'http://www.massey.ac.nz/massey/learning/programme-course-paper/paper.cfm?paper_code=%s'
        papers = parser.get_function(programme)()
        codestr = '\d{3}\.\d{3}'
        code = re.compile(codestr)
        code_link_pattern = '<a href="\?paper_code=%s" title="%s">%s</a>'%(codestr, codestr, codestr)
        restricted = re.compile('<li><b>Restriction\(s\):</b> (%s)*</li>'% (code_link_pattern))
        prereq = re.compile('<li><b>Prerequisite\(s\):</b> (%s)* (or %s)\?(%s)*</li>'%(code_link_pattern,code_link_pattern,code_link_pattern))
        coreq = re.compile('<li><b>Corequisite(s):</b> (%s)* (or %s)\?(%s)*</li>')
        self.tree = set()
        for paper in papers:
            node = vertex.Vertex(paper)
            self.tree.add(node)
            htmlstr = urllib2.urlopen(self.paperquery_url%(paper)).read()
            result = restricted.search(htmlstr)
            if result:
                for restrict in set(code.findall(result.group(0))):
                    #just straight string code of paper
                    node.add_restriction(restrict)
            result = prereq.search(htmlstr)
            if result:
                for pre in (code.findall(result.group(0))):
                    #make a vertex and add it to node prereq
                    vert = vertex.Vertex(pre)
                    node.add_prereq(vert)
            result = coreq.search(htmlstr)
            if result:
                for co in (code.findall(result.group(0))):
                    #make a vertex and add it to node prereq
                    vert = vertex.Vertex(co)
                    node.add_coreq(vert)
        
    
            
