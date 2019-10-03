
class Actor:    

    # giving the facility that the Actor constructor can be called with out without movieList
    def __init__(self, actorName, movieList):
        self.actorName = actorName
		
        if movieList is None:
            self.movieList = []
        else:			
            self.movieList = movieList
    
    # This method provides facility to add movies to list
    def add_movie(self,movieName):
        self.movieList.append(movieName)    
		
def mainFn():
    a01 = Actor("Will Smith",["Men In Black", "Independence Day"])
    print(a01.actorName+" ",a01.movieList)
    
    a02 = Actor("Jim Carry",["Liar Liar", "The Mask", "Yes Man"])
    print(a02.actorName+" ",a02.movieList)

    a03 = Actor("Tom Cruise",None)
    a03.add_movie("Mission Impossible")
    a03.add_movie("The Rain man")
    a03.add_movie("American Made")	
    print(a03.actorName+" ",a03.movieList)	
	
mainFn()
