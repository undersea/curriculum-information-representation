import tidy #to normalise the html to a valid xml document format
import urllib2
from page_finder import urls
import libxml2
import re


class Parser(object):
    def __init__(self, *args, **options):
        """
The parser used to extract the curriculum information on a programme of study from the relavent web page.
Parameters:
 options - a list of tidy flags to use for normalising the html input so it can be parsed by the xml parser.  They default to (output_xhtml=1, add_xml_decl=1, indent=1, tidy_mark=0).  They will always contain output_xhtml=1, numeric_entities=1 and tidy_mark=0. Please consult the tidy documentation for more information on these options.
"""
        if options:
            self.options = dict(options)
            self.options['output_xhtml'] = 1
            self.options['tidy_mark'] = 0
            self.options['numeric_entities'] = 1
        else:
            self.options = dict(output_xhtml=1, add_xml_decl=1, indent=1, tidy_mark=0, numeric_entities=1)
        
     

   
    def parse(self, programme):
        """
Parses the programmes web page and using a relavent function extracts the information needed to construct a curriculum for this paper.
Parameters:
 programme - the programme of study to extract and create a list of papers for
 """
        try:
            url = urls[programme]
            self.htmlstr = urllib2.urlopen(url).read()
            self.xmlstr = str(tidy.parseString(self.htmlstr, **self.options))
            self.data = libxml2.parseDoc(self.xmlstr)
        except Exception, e:
            print e
            self.data = None
            self.xmlstr=''
        
