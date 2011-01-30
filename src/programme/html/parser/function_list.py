
import libxml2 as xml
from lxml import etree
import page_finder as finder
import parser
import re

class ProgrammeFunction(parser.Parser):
    def __init__(self):
        super(ProgrammeFunction, self).__init__()

    def __call__(self):
        try:
            items = re.findall('\d{3}\.\d{3}', self.htmlstr)
            return set(items)
        except:
            return False



class AccountancyFunction(ProgrammeFunction):
    def __init__(self):
        super(AccountancyFunction, self).__init__()
        




class BSc(ProgrammeFunction):
    def __init__(self, major):
        super(BSc, self).__init__()

    def __call__(self):
        f = StringIO(self.htmlstr)
        tree = etree.parse(f)
        tmp = tree.getroot().xpath('//xhtml:h4[text()="%s"]/following-sibling::xhtml:table[1]/xhtml:tbody/xhtml:tr/xhtml:td[1]/text()', namespaces={'xhtml':'http://www.w3.org/1999/xhtml' % (major)})
        tmp = [x for x in tmp if len(x) > 1]
        if len(tmp) == 0:
            tmp = tree.getroot().xpath('//xhtml:h4[text()="Computer Science"]/../../..//xhtml:tr/xhtml:td[1]/text()', namespaces={'xhtml':'http://www.w3.org/1999/xhtml'})

            if len(tmp) == 0:
                return False

        return set(tmp)


functions = {'':ProgrammeFunction(), 'Bachelor of Accountancy (BAcc)': AccountancyFunction(),'Bachelor of AgriScience (Agriculture)':ProgrammeFunction(), 'Bachelor of Science (Animal Science)':BSc('Animal Science')}

def get_function(programme):
    try:
        parser = functions[programme]
        parser.parse(programme)

        return parser
    except:
        def nullfunction():
            return set()
        return nullfunction

