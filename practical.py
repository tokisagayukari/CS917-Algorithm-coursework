import itertools

morsedict = {'.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e',
             '..-.': 'f', '--.': 'g', '....': 'h', '..': 'i', '.---': 'j', '-.-': 'k',
             '.-..': 'l', '--': 'm', '-.': 'n', '---': 'o', '.--.': 'p', '--.-': 'q',
             '.-.': 'r', '...': 's', '-': 't', '..-': 'u', '...-': 'v', '.--': 'w',
             '-..-': 'x', '-.--': 'y', '--..': 'z',
             '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6',
             '--...': '7', '---..': '8', '----.': '9', '-----': '0'}


def morseDecode(inputStringList):
    """
    This method should take a list of strings as input. Each string is equivalent to one letter
    (i.e. one morse code string). The entire list of strings represents a word.

    This method should convert the strings from morse code into english, and return the word as a string.

    """
    # Please complete this method to perform the above described function
    decipher = ''
    # decrypt the morse code
    for i in inputStringList:
        # check if it is meaningful code
        if i in morsedict.keys():
            # add represent letter to the result
            decipher += morsedict[i]
        else:
            decipher += ''

    return decipher


def morsePartialDecode(inputStringList):
    """
    This method should take a list of strings as input. Each string is equivalent to one letter
    (i.e. one morse code string). The entire list of strings represents a word.

    However, the first character of every morse code string is unknown (represented by an 'x' (lowercase))
    For example, if the word was originally TEST, then the morse code list string would normally be:
    ['-','.','...','-']

    However, with the first characters missing, I would receive:
    ['x','x','x..','x']

    With the x unknown, this word could be TEST, but it could also be EESE or ETSE or ETST or EEDT or other permutations.

    We define a valid words as one that exists within the dictionary file provided on the website, dictionary.txt
    When using this file, please always use the location './dictionary.txt' and place it in the same directory as
    the python script.

    This function should find and return a list of strings of all possible VALID words.
    """

    dictionaryFileLoc = './dictionary.txt'
    # Please complete this method to perform the above described function
    # convert txt file to list
    CheckList = []
    f = open(dictionaryFileLoc, 'r')
    for line in f.readlines():
        line = line.replace('\n', '')
        CheckList.append(line)

    strlist = []
    resultlist = []

    # first item in the resulting combination which helps product
    combination = ['']
    for i in range(len(inputStringList)):
        # initialize the list
        strlist.clear()

        # two possibility of x
        str1 = inputStringList[i].replace('x', '.', 1)
        str2 = inputStringList[i].replace('x', '-', 1)
        if str1 in morsedict.keys():
            strlist.append(morsedict[str1])
        if str2 in morsedict.keys():
            strlist.append(morsedict[str2])
        # all the possible combination of letters
        combination = list(itertools.product(combination, strlist))

    result = ''
    for j in combination:
        # recursion
        result = GetLetter(j)
        # check if in the dictionary provided
        if result in CheckList:
            resultlist.append(result)
    return resultlist


# recursion to get the letters from tuples
def GetLetter(newtuple):
    result = ''
    # base case: if the first element is '', it means all the letters has been added to the result
    if newtuple[0] == '':
        letter = newtuple[1]
        result += letter
        return result
    # recursion case
    else:
        letter = newtuple[1]
        result += letter
        return GetLetter(newtuple[0]) + result


class Maze:
    def __init__(self):
        """
        Constructor - You may modify this, but please do not add any extra parameters
        """
        # Using two-dimensional array to store the status of current coordinate
        # blocktype[y][x] = 0 or blocktype[y][x] = 1
        self.blocktype, list = [], []
        # record the width and height of the maze
        self.x = 0
        self.y = 0

    def addCoordinate(self, x, y, blockType):
        """
        Add information about a coordinate on the maze grid
        x is the x coordinate
        y is the y coordinate
        blockType should be 0 (for an open space) of 1 (for a wall)
        """

        # Please complete this method to perform the above described function
        # update the length and width
        self.x = max(x, self.x)
        self.y = max(y, self.y)
        # check if a new coordinate would be added
        if self.y >= len(self.blocktype) or self.x >= len(self.blocktype[0]):
            # enlarge the array and initialize the value with 1(which is a wall),
            # here we automatically add those which are walls not mentioned in the main function
            newarray = [[1 for m in range(self.x + 1)] for n in range(self.y + 1)]
            # copy the old array
            for i in range(len(self.blocktype)):
                for j in range(len(self.blocktype[i])):
                    newarray[i][j] = self.blocktype[i][j]
            # update the array list
            self.blocktype = newarray
        self.blocktype[y][x] = blockType

    def printMaze(self):
        """
        Print out an ascii representation of the maze.
        A * indicates a wall and a empty space indicates an open space in the maze
        """

        # Please complete this method to perform the above described function
        height = self.y + 1
        width = self.x + 1
        for i in range(height):
            for j in range(width):
                if self.blocktype[i][j] == 0:
                    print(" ", end="")
                else:
                    print("*", end="")
            print("")
        pass

    def findRoute(self, x1, y1, x2, y2):
        """
        This method should find a route, traversing open spaces, from the coordinates (x1,y1) to (x2,y2)
        It should return the list of traversed coordinates followed along this route as a list of tuples (x,y),
        in the order in which the coordinates must be followed
        If no route is found, return an empty list
        """

        # initialize the maze with only start point is 1, others 0
        maze = [[0 for m in range(self.x + 1)] for n in range(self.y + 1)]
        maze[y1][x1] = 1
        k = 0
        # BFS to search all the possible paths with marking the order the points reached
        while maze[y2][x2] == 0:
            k += 1
            for i in range(len(maze)):
                for j in range(len(maze[i])):
                    if maze[i][j] == k:
                        if i > 0 and maze[i-1][j] == 0 and self.blocktype[i-1][j] == 0:
                            maze[i-1][j] = k + 1
                        if j > 0 and maze[i][j-1] == 0 and self.blocktype[i][j-1] == 0:
                            maze[i][j-1] = k + 1
                        if i < len(maze) - 1 and maze[i+1][j] == 0 and self.blocktype[i+1][j] == 0:
                            maze[i+1][j] = k + 1
                        if j < len(maze[i]) - 1 and maze[i][j+1] == 0 and self.blocktype[i][j+1] == 0:
                            maze[i][j+1] = k + 1

        height = self.y + 1
        width = self.x + 1
        for i in range(height):
            for j in range(width):
                print(maze[i][j], end=" ")
            print("")

        # Find the path
        num = maze[y2][x2]
        route = [(x2, y2)]
        empty = []
        x, y = x2, y2
        # find the neighbour point
        while num > 1:
            #  go left
            if x > 0 and maze[y][x-1] == num - 1:
                x, y = x - 1, y
                route.insert(0, (x, y))
                num -= 1
            #  go right
            elif x < len(maze[y]) - 1 and maze[y][x+1] == num - 1:
                x, y = x + 1, y
                route.insert(0, (x, y))
                num -= 1
            #  go up
            elif y > 0 and maze[y-1][x] == num - 1:
                x, y = x, y - 1
                route.insert(0, (x, y))
                num -= 1
            #  go down
            elif y < len(maze) - 1 and maze[y+1][x] == num - 1:
                x, y = x, y + 1
                route.insert(0, (x, y))
                num -= 1
            #  no path
            else:
                print(empty)
        print(route)
        pass


def morseCodeTest():
    """
    This test program passes the morse code as a list of strings for the word
    HELLO to the decode method. It should receive a string "HELLO" in return.
    This is provided as a simple test example, but by no means covers all possibilities, and you should
    fulfill the methods as described in their comments.
    """

    hello = ['....', '.', '.-..', '.-..', '---']
    print(morseDecode(hello))


def partialMorseCodeTest():
    """
    This test program passes the partial morse code as a list of strings 
    to the morsePartialDecode method. This is provided as a simple test example, but by
    no means covers all possibilities, and you should fulfill the methods as described in their comments.
    """

    # This is a partial representation of the word TEST, amongst other possible combinations
    test = ['x', 'x', 'x..', 'x']
    print(morsePartialDecode(test))

    # This is a partial representation of the word DANCE, amongst other possible combinations
    dance = ['x..', 'x-', 'x.', 'x.-.', 'x']
    print(morsePartialDecode(dance))


def mazeTest():
    """
    This sets the open space coordinates for the example
    maze in the assignment.
    The remainder of coordinates within the max bounds of these specified coordinates
    are assumed to be walls
    """
    myMaze = Maze()
    myMaze.addCoordinate(1, 0, 0)  # Start index
    myMaze.addCoordinate(1, 1, 0)
    myMaze.addCoordinate(1, 3, 0)
    myMaze.addCoordinate(1, 4, 0)
    myMaze.addCoordinate(1, 5, 0)
    myMaze.addCoordinate(1, 6, 0)
    myMaze.addCoordinate(1, 7, 0)

    myMaze.addCoordinate(2, 1, 0)
    myMaze.addCoordinate(2, 2, 0)
    myMaze.addCoordinate(2, 3, 0)
    myMaze.addCoordinate(2, 6, 0)

    myMaze.addCoordinate(3, 1, 0)
    myMaze.addCoordinate(3, 3, 0)
    myMaze.addCoordinate(3, 4, 0)
    myMaze.addCoordinate(3, 5, 0)
    myMaze.addCoordinate(3, 7, 0)
    myMaze.addCoordinate(3, 8, 0)  # End index

    myMaze.addCoordinate(4, 1, 0)
    myMaze.addCoordinate(4, 5, 0)
    myMaze.addCoordinate(4, 7, 0)

    myMaze.addCoordinate(5, 1, 0)
    myMaze.addCoordinate(5, 2, 0)
    myMaze.addCoordinate(5, 3, 0)
    myMaze.addCoordinate(5, 5, 0)
    myMaze.addCoordinate(5, 6, 0)
    myMaze.addCoordinate(5, 7, 0)

    myMaze.addCoordinate(6, 3, 0)
    myMaze.addCoordinate(6, 5, 0)
    myMaze.addCoordinate(6, 7, 0)

    myMaze.addCoordinate(7, 1, 0)
    myMaze.addCoordinate(7, 2, 0)
    myMaze.addCoordinate(7, 3, 0)
    myMaze.addCoordinate(7, 5, 0)
    myMaze.addCoordinate(7, 7, 0)

    myMaze.addCoordinate(8, 0, 1)

    # TODO: Test your findRoute method
    myMaze.printMaze()
    myMaze.findRoute(1, 0, 3, 8)


def main():
    morseCodeTest()
    partialMorseCodeTest()
    mazeTest()


if __name__ == "__main__":
    main()
