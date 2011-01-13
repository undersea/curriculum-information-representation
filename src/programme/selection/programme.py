"""
Forms the base class for all degree and major combinations which defines a common method to retrieve the value of that degree for when initially selecting them
"""

degrees = dict()

class Programme(object):
    def __init__(self, name):
        global degrees
        degrees[name] = self
        self.papers = set()
        self.major = set();
        self.value = 0
        pass

    def value(self):
        return self.value;

    def __call__(self, papers):
        #assume each entry in papers is a integer
        #first a straight match
        matches = set([x for x in papers if x in self.papers])
        #remove any matching paper from papers list
        papers = [x for x in papers if x not in matches]
        #now union it with a match based on subject
        matches |= set([x for x in papers if x/1000 in self.papers])
        #now use this to give the degree a rating
        self.value = len(matches)
            
            


class BInfSci_CS(Programme):
    def __init__(self):
        Programme.__init__(self, 'BInfSci CS')
        self.papers.add(119177)
        self.papers.add(158)
        self.papers.add(159)
        self.papers.add(160)
        self.papers.add(161)
        self.major.add(159)
        self.major.add(158359)
        self.major.add(161326)

BInfSci_CS()

class BSc_CS(Programme):
    def __init__(self):
        Programme.__init__(self, 'BSc CS')
        self.papers = self.papers.union([117, 119, 120, 121, 122, 123, 124, 142, 143, 145, 151, 157, 158, 159, 160, 161, 162, 171, 175, 188, 189, 194, 196, 199, 202, 203, 214, 233, 234, 236, 247])
        self.major.add(159)
        self.major.add(158359)
        self.major.add(161326)

BSc_CS()

class BSc_Maths(Programme):
    def __init__(self):
        Programme.__init__(self, 'BSc Maths')
        self.papers = self.papers.union([117, 119, 120, 121, 122, 123, 124, 142, 143, 145, 151, 157, 158, 159, 160, 161, 162, 171, 175, 188, 189, 194, 196, 199, 202, 203, 214, 233, 234, 236, 247])
        self.major.add(160)
        self.major.add(161200)

BSc_Maths()

class BA_English(Programme):
    def __init__(self):
        Programme.__init__(self, 'BA English')
        self.papers = self.papers.union([ 164 , 150 , 152 , 155 , 135 , 147 , 178 , 190 , 192102, 192101 , 115 , 132 , 131 , 275 , 179 , 134 , 176 , 175 , 230100 , 139 , 254 , 170 , 256 , 172 , 267 , 186 , 187 , 219 , 250 , 166 , 201 , 200 , 145 , 148 , 149 , 263 , 121 , 244 , 146 , 243 , 242 , 154 , 279 , 269 , 167 , 249 , 161 , 133 , 114 , 258 , 160101 , 241 , 245 , ])
        self.major.add(139)
        self.major.add(154108)
        self.major.add(154308)

BA_English()





