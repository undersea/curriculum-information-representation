from lxml import etree
import urllib2
from cStringIO import StringIO
import tidy #to normalise the html to a valid xml document format


from scheduleparser import fix_html


def extract_papers(htmlstr):
    f = StringIO(htmlstr)
    tree = etree.parse(f)

    tmp = tree.getroot().xpath('//xhtml:table/xhtml:tbody/xhtml:tr/xhtml:td[1]/text()', namespaces={'xhtml':'http://www.w3.org/1999/xhtml'})

    tmp = [x for x in tmp if len(x) > 1]

    return tmp



def get_data(url):
    sock = urllib2.urlopen(url)
    data = fix_html(sock.read())
    sock.close()
    return data


if __name__ == '__main__':
    sock = urllib2.urlopen('http://www.massey.ac.nz/massey/about-massey/calendar/degree-diploma-and-certificate-regulations/college-of-sciences/en/bachelor-of-science.cfm')
    data = fix_html(sock.read())
    sock.close()
    print extract_papers(data)
