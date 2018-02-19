"""Sandbox for implementing classic CSP algorithms"""

from numpy.random import choice as rand_choice

class constr():
    """simple constraint that takes 3 operators which are:
    [ !=, <, > ]"""

    def __init__(self,origin,tip,operator):
        self.origin=origin
        self.tip=tip
        self.oper=operator

class CSP():
    """A constraint satisfaction problem. Variables and values
    are encoded in a dictionary containing variable names as keys,
    and possible values in a list.

    Constraints between variables can be expressed in "constraints"
    as a directed graph expressed using a list of simple constraint
    elements. Constraints in this list are combined with an "AND" operator.

    Discrete variables, finite domains, hard constraints.

    On this simple example, the values are literals."""

    def __init__(self,varsVals,constrs):
        self.varsVals=varsVals
        self.constrs=constrs

    def consistency_check(self,variable,value,assignment):
        """Returns True if "value" for "variable" is consistent
        with "assignment" given self.constraints"""
        pass


class backtrack_search():
    """A backtrack search algorithm"""

    def __init__ (self,csp,maxConstrs=10000):
        self.csp=csp
        self.assignments=[] #list of dictionaries
        self.remaining_legal_values=self.csp.varsVals # for forward checking
        self.maxConstrs=maxConstrs
        self.createConstraintHist()

    def createConstraintHist(self):
        """Returns a dictionary with the number of constraints
        associated to each variable"""
        self.constraintHistogram={}
        for constr in self.csp.constrs:
            try:
                self.constraintHistogram[constr.origin]
                self.constraintHistogram[constr.origin]=self.constraintHistogram[constr.origin]+1
            except: #key does not exist, create
                self.constraintHistogram[constr.origin]=1
            try:
                self.constraintHistogram[constr.tip]
                self.constraintHistogram[constr.tip]=self.constraintHistogram[constr.tip]+1
            except: #key does not exist, create
                self.constraintHistogram[constr.tip]=1
        #now complete the list
        for variable in csp.varsVals:
            try:
                self.constraintHistogram[variable]
            except:
                #does not exist in constraints, so create and add 0
                self.constraintHistogram[variable]=0
        independenceCornerCase=sum(self.constraintHistogram.values())

        assert independenceCornerCase > 0, "No constraints for variables in CSP! Stopping."



    def next_variable(self):
        """Returns next variable to examine, considering
        the variables in the assignment as the explored
        variables, using First Fail (Minimum Remaining
        Values), breaking ties for the variable with most
        constraints"""

        winners=[]
        for variable in self.remaining_legal_values:
            if len(winners)==0:
                winners.append(variable)
                winnersize=len(self.remaining_legal_values[variable])
                continue

            currsize=len(self.remaining_legal_values[variable])

            if currsize > winnersize:
                continue

            if currsize < winnersize:
                del winners[:]
                winnersize=currsize
                winners.append(variable)
                continue

            if currsize == winnersize:
                winners.append(variable)

        #do we have more than one winner?
        if len(winners)==1:
            return winners[0]

        #break ties: return variable with most constraints
        #if all variables have equal constraints, return first.
        winnersize=0
        for element in winners:
            if self.constraintHistogram[element]>winnersize:
                winnersize=self.constraintHistogram[element]
                winner=element
        try:
            return winner
        except Exception as whydidthishappened:
            print ("For some reason we failed to have a winner. "
                   "this should not have happened. {}".format(whydidthishappened.message))


    def next_value(self,variable):
        """Returns next value given the current variable
        being explored, and the values explored for that
        variable"""
        #for now, let's try just a random value, we'll change that
        return rand_choice(self.remaining_legal_values[variable])

    def search(self):
        #TODO: Actually doing the search...
        nextVar=self.next_variable()
        nextVal=self.next_value(nextVar)
        print (nextVar,nextVal)


if __name__ == "__main__":
    varsVals = {"bucket1":[1,2,5,10],
                "bucket2":[0,1,3,20],
                "bucket3":[1,3,100]
                }
    #remember: Constraints in this list are combined with an "AND" operator.
    constrs=[constr("bucket1","bucket2",">"),
             constr("bucket1", "bucket3", ">")]
    csp = CSP(varsVals,constrs)
    app = backtrack_search(csp)
    app.search()