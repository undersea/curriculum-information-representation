"""
Forms the base class for all degree and major combinations which defines a common method to retrieve the value of that degree for when initially selecting them
"""

class Programme(object):
    def __init__(self):
        self.papers = set()
        self.major = set();
        self.value = 0
        pass

    def value(self):
        return self.value;


class BInfSci_CS(Programme):
    def __init__(self):
        Programme.__init__(self)
        self.papers.add(119177)
        self.papers.add(158)
        self.papers.add(159)
        self.papers.add(160)
        self.papers.add(161)
        self.major.add(159)
        self.major.add(158359)
        self.major.add(161326)


class BSc_CS(Programme):
    def __init__(self):
        Programme.__init__(self)
        self.papers.union([117, 119, 120, 121, 122, 123, 124, 142, 143, 145, 151, 157, 158, 159, 160, 161, 162, 171, 175, 188, 189, 194, 196, 199, 202, 203, 214, 233, 234, 236, 247])
        self.major.add(159)
        self.major.add(158359)
        self.major.add(161326)


class Bsc_Maths(Programme):
    def __init__(self):
        Programme.__init__(self)
        self.papers.union([117, 119, 120, 121, 122, 123, 124, 142, 143, 145, 151, 157, 158, 159, 160, 161, 162, 171, 175, 188, 189, 194, 196, 199, 202, 203, 214, 233, 234, 236, 247])
        self.major.add(160)
        self.major.add(161200)


class BA_English(Programme):
    def __init__(self):
        Programme.__init__(self)
        
