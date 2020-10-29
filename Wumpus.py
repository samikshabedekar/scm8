class cell:
    def __init__(self, value = 0):
        self.values ={"Agent":value,"Wumpus":value,"Pit":value, "Stench": value, "Breeze": value,"Glitter":value}
    def updateCell(self,key):
        self.values[key] = 1
    def getValues(self):
        return self.values
    def isSafe(self):
        f = 0
        values = self.values
        if(values["Wumpus"] == 1):
            f = -1
        if(values["Pit"] == 1):
            f = 1
        return f
    def isGold(self):
        return self.values["Glitter"]
class board:
    def __init__(self, n,value = 0):
        self.size = n
        cells = [[cell(value) for i in range(0,n)] for j in range(0,n)]
        self.cells = cells
    def addCell(self,i,j,cell):
        self.cells[i][j] = cell
    def getCell(self,i,j):
        return self.cells[i][j]
    def displayCells(self,agent_i,agent_j):
        cells = self.cells
        n = self.size
        for i in range(0,n):
            for j in range(0,n):
                o = []
                if ((i == agent_i) and (j== agent_j)):
                    o.append("A")
                else:
                    o.append(" ")
                cell = self.getCell(i,j)
                values = cell.values
                for key in values:
                    if (values[key] == 1 and key!="Agent"):
                        o.append(list(key)[0])
                    else:
                        o.append("_")
                print("".join(o), end ="|") 
            print()
        
def checkForPit(i,j,kb):
        n = kb.size
        p1 = -2
        p2= -2
        p3 = -2
        p4 = -2
        if (i-1>=0):
            p1 = kb.getCell(i-1,j).values["Breeze"]
        else:
            p1 = 1
        if(i+1<n):
            p2 =kb.getCell(i+1,j).values["Breeze"]
        else:
            p2 = 1
        if  (j-1>=0):
            p3 = kb.getCell(i,j-1).values["Breeze"]
        else:
            p3 = 1
        if(j+1<n):
            p4 =kb.getCell(i,j+1).values["Breeze"]
        else:
            p4 = 1
        if(p1 == 1 and p2 == 1 and p3 == 1 and p4 == 1):
            return -1
        if(p1*p2*p3*p4 == 0):
            return 1
        return 0
def checkForWumpus(i,j,kb):
        n = kb.size
        p1 = -2
        p2= -2
        p3 = -2
        p4 = -2
        if (i-1>=0):
            p1 = kb.getCell(i-1,j).values["Stench"]
        else:
            p1 = 1
        if (i+1<n):
            p2 =kb.getCell(i+1,j).values["Stench"]
        if(j-1>=0):
            p3 = kb.getCell(i,j-1).values["Stench"]
        else:
            p3 = 1
        if (j+1<n):
            p4 =kb.getCell(i,j+1).values["Stench"]
        else:
            p4 = 1
        if (p1 == 1 and p2 == 1 and p3 == 1 and p4 == 1):
            return -1
        if  (p1*p2*p3*p4 == 0):
            return 1
        return 0
def explore(i,j,kb,board):
        kb.addCell(i,j,board.getCell(i,j))
def addToOpen(i,j,n, openList,visitedList):
        if(i-1>=0):
            if((i-1,j) not in openList) and ((i-1,j) not in visitedList):
                openList.append((i-1,j))
        if(i+1<n):
            if((i+1,j) not in openList) and ((i+1,j) not in visitedList):
                openList.append((i+1,j))
        if(j-1>=0):
            if((i,j-1) not in openList) and ((i,j-1) not in visitedList):
                openList.append((i,j-1))
        if(j+1<n):
            if((i,j+1) not in openList) and ((i,j+1) not in visitedList):
                openList.append((i,j+1))
        return openList
def checkPath(path):
        f = 0
        for i in range(0,len(path) - 1):
            x1,y1 = path[len(path) - 1-i][0],path[len(path) - 1- i][1]
            x2,y2 = path[len(path) - 1-(i+1)][0],path[len(path) - 1- (i+1)][1]
            if(abs(x1-x2) + abs(y1-y2) >=2):
                f = 1
                break
        if (f == 0):
            return False
        else:
            return True
def getPath(path):
        f = -1
        while checkPath(path) and len(path)>1:
            if(-1*f>=len(path)):
                break
        x1,y1 = path[f][0],path[f][1]
        x2,y2 = path[f-1][0],path[f-1][1]
        if(abs(x1-x2) + abs(y1-y2) >=2):
            path.remove(path[f-1])
            f = -1
        else:
            f = f-1
        return path
def wumpusWorld(board, kb, n,start_i,start_j):
        visitedList = []
        visitedList.append((start_i,start_j))
        openList = []
        openList = addToOpen(start_i,start_j, n, openList, visitedList)
        i = 0
        path = []
        path.append((start_i,start_j))
        while len(openList)>0:
            ij = openList[0]

            if(board.cells[ij[0]][ij[1]].isGold() ==1):
                path.append(ij)
                print()
                kb.displayCells(ij[0],ij[1])
                print("Agent moved to ",ij[0]+1," ",ij[1]+1," ..")
                print("Gold found at ",ij[0]+1," ",ij[1]+1)
                break
            if (checkForPit(ij[0],ij[1],kb)== 1 and checkForWumpus(ij[0],ij[1],kb)== 1):
                    openList.remove(ij)
                    print()
                    kb.displayCells(ij[0],ij[1])
                    print("Agent moved to",ij[0]+1," ",ij[1]+1," ..")
                    explore(ij[0],ij[1],kb,board)
                    openList = addToOpen(ij[0],ij[1], n, openList, visitedList)
                    if (ij not in visitedList):
                        visitedList.append(ij)
                        path.append(ij)
                    else:
                        while(path[-1]!=ij):
                            path.remove(path[-1])
            else:
                    openList.remove(ij)
            i = i+1
        path = getPath(path)
        print("Path: ")
        i = 0
        for i in range(0,len(path)-1):
            print(path[i],end = "->")
            print(path[i+1])
n = int(input("Enter Cave Size: "))
cave = board(n)
for i in range(0,n):
    for j in range(0,n):
        c = cell()
        s = "Enter Cell " +str(i)+" , "+str(j)+ " Values: "
        values = input(s).split()
        for value in values:
            c.updateCell(value)
            cave.addCell(i,j,c)
kb = board(n,-1)
start = input("Enter Agent Location:").split()
c =cave.getCell(int(start[0]),int(start[1]))
c.updateCell("Agent")
kb.addCell(int(start[0]),int(start[1]),c)
wumpusWorld(cave,kb,n,int(start[0]),int(start[1]))
