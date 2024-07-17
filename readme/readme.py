import aetherdb
from limedev import readme
#=======================================================================
def main(pyproject: readme.PyprojectType):
    """This gets called by the limedev."""
    name = pyproject['tool']['limedev']['full_name']
    semi_description = f'''
        {name} is a graph database program to allow mixed file type data
        in a database.
        Far from ready to be used.'''
    return readme.make(aetherdb,
                       semi_description,
                       name = name,
                       abbreviation = 'ae')
#=======================================================================
