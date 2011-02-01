import re
import urllib2
from lxml import etree
from cStringIO import StringIO
from scheduleparser import fix_html

#use xpath it's a lot less messy


def replace_hrefs(htmlstr):
    tmp = '<a\s*href=\s*"\?paper_code=\d{3}\.\d{3}"\s*title="\d{3}\.\d{3}">'
    return re.sub(tmp, "", htmlstr).replace('\n', '')

class Paper(object):
    def __init__(self):
        self.paperquery_url = 'http://www.massey.ac.nz/massey/learning/programme-course-paper/paper.cfm?paper_code=%s'
        self.paper = None
        self.prereq_set = set()
        self.coreq_set = set()
        self.restriction_set = set()


    def __call__(self, paper):
        self.paper = paper #so the paper code can be retrieved

        #get and fix the html containing the data
        sock = urllib2.urlopen(self.paperquery_url%(paper))
        htmlstr = fix_html(replace_hrefs(sock.read()))
        sock.close()

        #parse this into a DOM
        f = StringIO(htmlstr)
        tree = etree.parse(f)

        #make sure it is still offered
        if len(tree.getroot().xpath('//xhtml:p/xhtml:b[starts-with(text(), "This paper is not offered in")]', namespaces={'xhtml':'http://www.w3.org/1999/xhtml'})) > 0:
            return False

        #prereqs, coreqs and restrictions are kept 
        #in li tags in the div with id of 'maincontent'
        ul = tree.getroot().xpath('//xhtml:div[@id="maincontent"]//xhtml:li/xhtml:b',  namespaces={'xhtml':'http://www.w3.org/1999/xhtml'})

        
        pattern = re.compile('\d{3}\.\w{3}')
        for i in ul:
            constraint = str(i.text).strip().lower()
            papers = str(i.tail).strip()
            if constraint == 'prerequisite(s):':
                for p in pattern.findall(papers):
                    self.prereq_set.add(p)
            elif constraint == "restriction(s):":
                for p in pattern.findall(papers):
                    self.restriction_set.add(p)
            elif constraint == 'corequisite(s):':
                for p in pattern.findall(papers):
                    self.coreq_set.add(p)
    return True


if __name__ == '__main__':
    paper = Paper()
    paper(152319)
    print paper.prereq_set
    print paper.coreq_set
    print paper.restriction_set
