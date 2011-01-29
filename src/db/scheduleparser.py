from html.parser import HTMLParser


class ScheduleExtracter(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.h4 = False
        self.major = False
        self.table = False

    def handle_starttag(self, tag, attrs):
        if tag == 'h4':
            self.h4 = True
            
            print('Start tag: ', tag)
            
        else:
            if self.major and tag == 'table':
                print('start of major schedule table')
                self.table = True
            if self.major and self.table:
                print('"<%s>"'% (tag), end=' ')
            
    
    def handle_endtag(self, tag):
        if tag == 'h4':
            self.h4 = False

            print('End tag: ', tag)

                
        else:
            if self.major and self.table:
                
                print('"</%s>"'% (tag), end=' ')
                
            if self.major and self.table and tag == 'table':
                
                print('end of table', tag)
                
                self.major = False
                self.table = False

    def handle_data(self, data):
        if self.h4:
            print("'%s' %s" % (data, len(data)))
            if str(data) == 'Agricultural Science':
                self.major = True
            


if __name__ == '__main__':
    import urllib.request, urllib.error, urllib.parse
    sock = urllib.request.urlopen('http://www.massey.ac.nz/massey/about-massey/calendar/degree-diploma-and-certificate-regulations/college-of-sciences/en/bachelor-of-science.cfm')
    data = sock.read()
    print(type(data))
    p = ScheduleExtracter()
    p.feed(str(data))

