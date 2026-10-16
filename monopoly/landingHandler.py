from viewProperty import viewProperty
from propertyLanding import propertyLanding
from utilityLanding import utilityLanding
from chanceLanding import chanceLanding
from chestLanding import chestLanding
from freeParkingLanding import freeParkingLanding
from goLanding import goLanding
from goToJailLanding import goToJailLanding
from jailLanding import jailLanding
from stationLanding import stationLanding
from taxLanding import taxLanding

def landingHandler(propertyType, players, i, playerAmount, property, card):
    
    if propertyType == "property":
        return propertyLanding(players, property, i, playerAmount)
    elif propertyType == "chance":
        return chanceLanding(players, card, i, playerAmount)
    elif propertyType == "community_chest":
        return chestLanding(players, card, i, playerAmount)
    elif propertyType == "free_parking":
        return freeParkingLanding()
    elif propertyType == "go":
        return goLanding(players, property, i, playerAmount)
    elif propertyType == "go_to_jail":
        return goToJailLanding(players, property, i, playerAmount)
    elif propertyType == "jail":
        return jailLanding(players, property, i, playerAmount)
    elif propertyType == "station":
        return stationLanding(players, property, i, playerAmount)
    elif propertyType == "tax":
        return taxLanding(players, property, i, playerAmount)
    elif propertyType == "utility":
        return utilityLanding(players, property, i, playerAmount)