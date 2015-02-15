class Location(object):


    """
    Abstract class of a general location selling Kannah Beer.
    """

    def __initi__(self, name, areaCode, city, state, website):

        """"
        Initialize a Location instance, saves all parameters as
        attributes of the instance.

        areaCode: integer, 5 didgits
        city: string
        website: string
        hasKannah: boolean
        hasKannahSpecialty: boolean
        
        """
        self.name = name
        self.areaCode = areaCode
        self.city = city
        self.state = state
        self.website = website
        self.info = name, website


    def getAreaCode(self):
        return self.areaCode

    def getCity(self):
        return self.city

    def getState(self):
        return self.state

    def updateWebsite(self, website):
        self.website = website 
    
    def getWebsite(self):
        return self.website

    def updateHasKannah(self, status):
        self.hasKannah = status

    def hasKannah(self):
        return self.hasKannah

    def updateHasKannahSpecialty(self, status):
        self.hasKannahSpecialty = status

    def hasKannahSpecialty(self):
        return self.hasKannahSpecialty

    def __lt__(self, other):
        return self.name < other.name                              

    def __str__(self):
        return self.info


class Bar(Location):

    """
    Add in a variable for draght beer and bottle beer.

    draught: boolean
    bottle: boolean
    
    """
    def __init__(self, name, areaCode, city, state, website, locationType):
        Locations.__init__(self, name, areaCode, city, state, website)
        self.locationType = locationType
        self.info = name, website, locationType

    def updateDraught(self, status):
        self.draught = status

    def hasDraught(self):
        return self.draught

    def updateBottle(self, status):
        self.bottle = status

    def hasBottle(self):
        return self.bottle

    def __str__(self):
        return self.info


class Restaurant(Location):

    """
    Add in a variable for draght beer and bottle beer.

    draught: boolean
    bottle: boolean
    
    """
     def __init__(self, name, areaCode, city, state, website, locationType):
        Locations.__init__(self, name, areaCode, city, state, website)
        self.locationType = locationType
        self.info = name, website, locationType

    
    def updateDraught(self, status):
        self.draught = status

    def hasDraught(self):
        return self.draught

    def updateBottle(self, status):
        self.bottle = status

    def hasBottle(self):
        return self.bottle

class LiquorStore(Location):
    pass

class LocationsList(object):

    """
    A list of location instances that have Kannah beer now
    or did in the past (therefore may have again).

    Methods to update list, remove from list.

    Sorts the list only if it is unsorted.
    """

    def __init__(self):

        self.locations = []
        self.isSorted = True

    def addLocation(self, location):
        if location in self.locations:
            raise ValueError('Duplicate Location')
        self.locations.append(location)
        self.isSorted = False

    def allLocations(self):
        if not self.isSorted:
            self.locations.sort()
        return self.locations[:]


def findKannahBeer(LocationsList):

    """
    LocationList: instance of the class LocationsList, is list
    of location instances.

    Takes in user input of an area code (type int), and
    returns a list of locations within areaCode that
    have Kannah beer. Offers specific details of store's name,
    website, what kind of store, draught and/or tap, and if they carry
    Kannah specialty beers.
    """

    results = []

    while True:

        userArea = raw_input('Area Code: ')

        if userArea != int and len(userArea) != 5:
            return "Sorry, but we need a proper area code."

        for location in LocationsList:
            if location.areaCode == userArea and location.hasKannah():
                results.append(location)

        return results
    
    

