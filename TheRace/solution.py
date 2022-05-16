

from copy import deepcopy
from pprint import pprint


class Developer():
    def __init__(self, company, bonus, nSkills, skills ):
        self.companyName = company
        self.bonusPotential = bonus
        self.skillCount = nSkills
        self.skillsList = skills

        self.coordinate = None
        self.isDeveloper = True

        self.benefits = dict()

class Manager():
    def __init__(self, company, bonus):
        self.companyName = company
        self.bonusPotential = bonus

        self.coordinate = None
        self.isDeveloper = False

        self.benefits = dict()

def totalPotential(firstTechie, secondTechie):
    totalPotential = 0
    #working potential
    if firstTechie.isDeveloper and secondTechie.isDeveloper:
        commonSkills = set(firstTechie.skillsList) & set(secondTechie.skillsList)
        allSkills = set(firstTechie.skillsList + secondTechie.skillsList)

        totalPotential += len(commonSkills) * (len(allSkills) - len(commonSkills))

    #bonus point 
    if firstTechie.companyName == secondTechie.companyName:
        totalPotential += firstTechie.bonusPotential+ secondTechie.bonusPotential
    
    return totalPotential


def potentialOfGrid(grid):
    sumPotential = 0
    for row in grid:
        for i in range(1,len(row)):   
            firstTechie, secondTechie = row[i], row[i-1] 
            print(firstTechie, secondTechie)
            if isinstance(firstTechie, str)  or    isinstance(secondTechie, str):
                continue
            sumPotential += totalPotential(firstTechie, secondTechie)

    for i in range(len(grid)):
        for j in range(len(grid[0])-1): 
            firstTechie, secondTechie = grid[i][j], grid[i][j+1]
            if isinstance(firstTechie, str) or    isinstance(secondTechie, str):
                continue
            sumPotential += totalPotential(firstTechie, secondTechie)
    return sumPotential


def generateAllGrids(developerList, managerList, grid):
    gridCopy = deepcopy(grid)
    for techie in developerList + managerList:
        for row in range(len(gridCopy)):
            
            for col in range(len(gridCopy[0])):
                char  = gridCopy[row][col]
                if char == "#": continue
                if char == '_' and techie.isDeveloper:
                    gridCopy[row][col] = techie
                elif char == 'M' and not techie.isDeveloper:
                    gridCopy[row][col] = techie
                
                
                yield gridCopy 
               # yield from generateAllGrids(developerList, managerList, gridCopy)



def assignTechieBenefits(developerList, managerList):

    for techie in developerList + managerList:
        for otherTechie in developerList + managerList:
            if otherTechie == techie:
                continue
            techie.benefits[otherTechie] = totalPotential(techie, otherTechie)
        

    return (developerList, managerList)


def solveGrid(developerList, managerList, grid):
    bestGrid = grid
    totalPotential = 0
    for grid in generateAllGrids(developerList, managerList, grid):
        if potentialOfGrid(grid) > totalPotential:
            bestGrid = grid 
    
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            item = bestGrid[row][col]
            if not isinstance(item, str):
                item.coordinate = (row, col)
            
    return developerList, managerList



#testing the program

if __name__ == "__main__":

    #dev: cname, bpoint, [skills]
    #man: cname, bpoint

    developerList = []
    managerList = []
    with open('input.txt', 'r') as inputFile:
        gridWidth, gridHeight = list(map(int, inputFile.readline().split()))
        grid = [list(inputFile.readline().strip().rstrip()) for _ in range(gridHeight)]
        developerCount = int(inputFile.readline().strip().rstrip())

        for _ in range(developerCount):
            _lineIn = inputFile.readline().split()
            #company_name, bonus potential, number_of_skills, [skills]
            developerList.append(
                Developer(
                    _lineIn[0],
                    int(_lineIn[1]),
                    int(_lineIn[2]),
                    _lineIn[3:]
                )
                )

        managerCount = int(inputFile.readline().strip().rstrip())
        for _ in range(managerCount):
            _lineIn = inputFile.readline().split()
            #company_name, bonus potential
            managerList.append(Manager(
                _lineIn[0],
                int(_lineIn[1])
            ))

    #ouput
    
    print("\n[Writing] Writing output to file....\n")
    finalDevList, finalManagerList = solveGrid(developerList, managerList, grid)

    with open('output.txt', 'w') as outputFile:
        for developer in finalDevList:
            if developer.coordinate:
                outputFile.write("%d %d\n"%(developer.coordinate))
            else:
                outputFile.write("X\n")

        for manager in finalManagerList:
            if manager.coordinate:
                outputFile.write("%d %d\n"%(manager.coordinate))
            else:
                outputFile.write("X\n")

    print("[Completed] Solution written to file....\n")