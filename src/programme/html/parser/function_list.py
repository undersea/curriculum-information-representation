
import libxml2 as xml
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
        





functions = {'':ProgrammeFunction(), 'Bachelor of Accountancy (BAcc)': AccountancyFunction(),}

def get_function(programme):
    try:
        parser = functions[programme]
        parser.parse(programme)

        return parser
    except:
        def nullfunction():
            return False
        return nullfunction

