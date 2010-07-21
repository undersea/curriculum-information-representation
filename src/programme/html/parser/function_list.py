
import libxml2


functions = {}

def get_function(programme):
    try:
        return functions[programme]
    except:
        return None


