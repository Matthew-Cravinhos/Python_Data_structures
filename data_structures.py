# Tuple version
def legalAges():
    lifeEvent = (
        16,
        18,
        21,
        65
    )

    print("The legal driving age is " + str(lifeEvent[0]) + ".")
    print("The legal voting age is " + str(lifeEvent[1]) + ".")
    print("The legal drinking age is " + str(lifeEvent[2]) + ".")
    print("The legal retirement age is " + str(lifeEvent[3]) + ".")

# Dictionary Version
def legalAgesDict():
    lifeEvent = {
        "drivingAge": 16,
        "votingAge": 18,
        "drinkingAge": 21,
        "retirementAge": 65
    }

    print("The legal driving age is " + str(lifeEvent["drivingAge"]) + ".")
    print("The legal voting age is " + str(lifeEvent["votingAge"]) + ".")
    print("The legal drinking age is " + str(lifeEvent["drinkingAge"]) + ".")
    print("The legal retirement age is " + str(lifeEvent["retirementAge"]) + ".")
    


legalAges()
legalAgesDict()