import urllib2

import vertex
import edge

import programme.html.parser as parser

import re

class Tree(object):
    def __init__(self, programme):
        self.paperquery_url = 'http://www.massey.ac.nz/massey/learning/programme-course-paper/paper.cfm?paper_code=%s'
        papers = parser.get_function(programme)()
        code = re.compile('\d{3}\.\d{3}')
        restricted = re.compile('<li><b>Restriction\(s\):</b> (<a href="\?paper_code=\d{3}\.\d{3}" title="\d{3}\.\d{3}">\d{3}\.\d{3}</a>)*</li>')
        self.tree = set()
        for paper in papers:
            vertex = vertex.Vertex(paper)
            self.tree.add(vertex)
            htmlstr = urllib2.urlopen(self.paperquery_url%(paper)).read()
            result = restricted.search(htmlstr)
            if result:
                for restricted in set(code.findall(result.group(0))):
                    vertex.add_restriction(restricted)

            
