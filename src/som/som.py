
from unsupervised.som import som

class SOM(som):
    def __init__(self, *args, **kwargs):
        try:
            #super class 'som' must be a newstyle class inheriting from object
            #for the following super() statment to work
            super(SOM, self).__init__(*args, **kwargs)
        except:
            som.__init__(self, *args, **kwargs)
