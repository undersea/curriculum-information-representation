import unittest

import page_finder as pf
import parser
import libxml2

class ParserTest(unittest.TestCase):
    def test_url_find(self):
        self.assertEquals(pf.urls['Bachelor of Accountancy (BAcc)'],'http://study.massey.ac.nz/massey/learning/programme-course-paper/programme.cfm?prog_id=93313&major_code=&tab=plan')
    
    def test_xslt_works(self):
        html = libxml2.parseDoc("""
<html>
<body>
<div class="progSectionText">
hello
</div>
<div>
goodbye
</div>
</body>
</html>
""")
        print parser.xslt.applyStylesheet(html, None)
