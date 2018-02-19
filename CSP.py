"""Sandbox for implementing classic CSP algorithms"""

class constraint():
    """simple constraint that takes 4 operators which are:
    [ =, !=, <, > ]"""

    def __init__(self,origin,tip,operator):
        self.origin=origin
        self.tip=tip
        self.operator=operator

class CSP():
    """A constraint satisfaction problem. Variables and values
    are encoded in a dictionary containing variable names as keys,
    and possible values in a list.

    Constraints between variables can be expressed in "constraints"
    as a directed graph expressed using a list of simple constraint
    elements.

    Discrete variables, finite domains, hard constraints.

    On this simple example, the values are literals."""

    def __init__(self,varsVals,constraints):
        self.varsVals=varsVals
        self.constaints=constraints

    def consistency_check(self,variable,value,assignment):
        """Returns True if "value" for "variable" is consistent
        with "assignment" given self.constraints"""
        pass


class backtrack_search():
    """A backtrack search algorithm"""

    def __init__ (self,csp):
        self.csp=csp
        self.assignment={}
        self.remaining_legal_values={} # for forward checking

    def next_variable(self):
        """Returns next variable to examine, considering
        the variables in the assignment as the explored
        variables, using First Fail (Minimum Remaining
        Values), breaking ties for the variable with most
        constraints"""
        pass

    def next_value(self,variable,values_explored):
        """Returns next value given the current variable
        being explored, and the values explored for that
        variable"""
        pass


if __name__ == "__main__":
    varsVals = {"bucket1":[1,2,5,10],
                "bucket2":[0,1,3,20],
                "bucket3":[1,3,100]
                }
    constaints=[]
    csp = CSP()
    app = backtrack_search(csp)
    app.search()