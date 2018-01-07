 # -*- coding: utf-8 -*-
import math

# Konstanter

# Bar weights.
maleBarWeight = 20
femaleBarWeight = 15

# Distances from origo ( centre of bar) to where weight are loaded.
distanceToWeightMale = 0.70
distanceToWeightFemale = 0.685

# 1.25 kg is the minumum increment
minumumIncrement = 1.25

# width in m of different weights 1.25kg, 2.5kg, 5kg, 10kg, 15kg, 20kg
widthOfIncrement = 0.02
twoFiveW = 0.023
fiveW = 0.045
tenW = 0.06
fifteen = 0.09
twenty = 0.115

# Lists

# List containing load in Kg that one side of the bar is loaded with.
oneSideLoadList =[
2.5,
5,
7.5,
10,
12.5,
15,
17.5,
20,
22.5,
25,
27.5,
30,
32.5,
35,
37.5,
40
]

# List contaning total width for weights in oneSideLoadList.
allWeightW = [
twoFiveW,
fiveW,
fiveW+twoFiveW,
tenW,
tenW+twoFiveW,
fifteen,
twoFiveW+fifteen,
twenty,
twenty+twoFiveW,
twenty+fiveW,
twenty+fiveW+twoFiveW,
twenty+tenW,
twenty+tenW+twoFiveW,
twenty+tenW+fiveW,
twenty+tenW+fiveW+twoFiveW,
twenty+twenty
]


# For debugging purposes. Ensures that both lists are of equalt lenght.
for index, width in enumerate(allWeightW):
    print width, oneSideLoadList[index]


# Herrstång
print "Herrstång. kompensation för olika vikter"
print

for index,m in enumerate(oneSideLoadList):
    leftSideWeight = oneSideLoadList[index]
    rightSideWeight = leftSideWeight+minumumIncrement
    totalWeight = leftSideWeight+rightSideWeight + maleBarWeight
    distanceToMinumumIncrement = distanceToWeightMale + allWeightW[index]
    result = (distanceToMinumumIncrement+(widthOfIncrement/2))*minumumIncrement /(totalWeight)
    print "Herrstång:tot",totalWeight, "kg, vänster", leftSideWeight, "kg, höger", rightSideWeight, "kg. Kompensation", round(result*100,4), "(cm) åt höger"

print
print "Damstång. kompensation för olika vikter"
print

# Damstång
for index,m in enumerate(oneSideLoadList):
    leftSideWeight = oneSideLoadList[index]
    rightSideWeight = leftSideWeight+minumumIncrement
    totalWeight = leftSideWeight+rightSideWeight + femaleBarWeight
    distanceToMinumumIncrement = distanceToWeightFemale + allWeightW[index]
    result = (distanceToMinumumIncrement+(widthOfIncrement/2))*minumumIncrement /(totalWeight)
    print "Damstång:tot",totalWeight, "kg, vänster", leftSideWeight, "kg, höger", rightSideWeight, "kg. Kompensation", round(result*100,4), "(cm) åt höger"
