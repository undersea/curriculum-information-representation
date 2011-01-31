from lxml import etree
import urllib2
from cStringIO import StringIO
import tidy #to normalise the html to a valid xml document format

def extract_major(htmlstr, major):
    f = StringIO(htmlstr)
    tree = etree.parse(f)
    tmp = tree.getroot().xpath('//xhtml:h4[text()="%s"]/following-sibling::xhtml:table[1]/xhtml:tbody/xhtml:tr/xhtml:td[1]/text()' % (major), namespaces={'xhtml':'http://www.w3.org/1999/xhtml'})
    tmp = [x for x in tmp if len(x) > 1]
    if len(tmp) == 0:
        tmp = tree.getroot().xpath('//xhtml:h4[text()="%s"]/../../..//xhtml:tr/xhtml:td[1]/text()' % (major), namespaces={'xhtml':'http://www.w3.org/1999/xhtml'})
        tmp = [x for x in tmp if len(x) > 1]
        if len(tmp) == 0:
            return False

    return major, set(tmp)
            

def extract_major_names(htmlstr):
    f = StringIO(htmlstr)
    tree = etree.parse(f)
    tmp = tree.getroot().xpath('//xhtml:h4/text()', namespaces={'xhtml':'http://www.w3.org/1999/xhtml'})
    remove = list()
    for x in tmp:
        expression = '//xhtml:h4[text()="%s"]' % (x)
        
        tmp2 = tree.getroot().xpath(expression, namespaces={'xhtml':'http://www.w3.org/1999/xhtml'})
        
        # note don't remove elements of a list you are iterating 
        # over in the loop as it puts the iteration out of sync
        for y in tmp2:
            if (y != None and y.getnext() != None and 
                y.getnext().text != None and
                (y.getnext().text.startswith("No new"))):
        
                remove.append(x)
        else:
            if len(tmp2) == 0:
                remove.append(x)


    tmp = [x for x in tmp if len(x) > 1 and not x.startswith('Part') and not (x in remove)]

    return tmp


def fix_html(htmlstr):
    options = dict()
    options['output_xhtml'] = 1
    options['tidy_mark'] = 0
    options['numeric_entities'] = 1

    return str(tidy.parseString(htmlstr, **options))

if __name__ == '__main__':
    sock = urllib2.urlopen('http://www.massey.ac.nz/massey/about-massey/calendar/degree-diploma-and-certificate-regulations/college-of-sciences/en/bachelor-of-science.cfm')
    data = fix_html(sock.read())
    sock.close()
    for x in extract_major_names(data):
        print extract_major(data, x)

    

