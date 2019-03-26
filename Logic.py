from Pieces import *
import random
from Stack import *
import math

Ends = {'Left' : ['4B', 'LBB', 'LBTB', 'LRB', 'LRBB', 'LRTB', 'LTB', 'LB'],
        'Right' : ['4B', 'LRB', 'LRBB', 'LRTB', 'RB', 'RBB', 'RBTB',  'RTB'],
        'Top' : ['4B', 'LBTB', 'LRTB', 'LTB', 'RBTB', 'RTB', 'TB', 'TBB'],
        'Bottom' : ['BB', '4B', 'LBB', 'LBTB', 'LRBB', 'RBB', 'RBTB', 'TBB']}
Paths = {'Left' : ['LRBC','LRTC','LTBC','4C', 'H', 'LBC', 'LTC'],
         'Right' : ['LRBC','LRTC','RTBC','4C', 'H', 'RBC', 'RTC'],
         'Top' : ['LRTC','LTBC', 'RTBC','4C', 'V', 'LTC', 'RTC'],
         'Bottom' : ['LRBC','LTBC','RTBC','4C', 'V', 'RBC', 'LBC']}
directions = ['Top', 'Bottom', 'Left', 'Right']
grid_movements = [(-1, 0), (1, 0), (0, -1), (0, 1)]
grid_movements_point = {(-1, 0) : "Top", (1, 0) : "Bottom", (0, -1) : "Left", (0, 1) : "Right"}
grid_movements_direction = {"Top": (-1, 0), "Bottom": (1, 0), "Left": (0, -1), "Right": (0, 1)}
direction_opposites = {"Top": "Bottom", "Bottom": "Top", "Left": "Right", "Right": "Left"}

'''
def Generate_Path(grid, point, direction_from, path_reached, piece_size, size, screen):
    x, y = point
    xMove, yMove = random.choice(grid_movements)
    while grid_movements_point[(xMove, yMove)] == direction_from or x + xMove == size or y + yMove == size or x + xMove == -1 or y + yMove == -1:
        xMove, yMove = random.choice(grid_movements)
    if grid[x + xMove][y + yMove] != 0 :
        #if grid[x + xMove][y + yMove].get_end() or path_reached:
        required, prohibated = get_required_prohibated(grid, (x, y))
        name = match_piece(prohibated, required, True)
        next = make_piece(name)
        grid[x][y] = next
        while not check_valid(grid, (x, y)):
            name = match_piece(prohibated, required, True)
            next = make_piece(name)
            grid[x][y] = next
        return 1
    else:
        x += xMove
        y += yMove
        if grid[x][y] == 0:
            count = 1 + Generate_Path(grid, (x, y), grid_movements_point[(xMove, yMove)], True, piece_size, size, screen)
            link_all(grid, (x,y))
            update_locations(grid, size)
            grid[x][y].render(screen)
            pygame.display.flip()
    return count
'''
'''
def Generate_Path(grid, point, stack):
    head = stack
    head.set_location(point)
    x, y = point
    next = myStack(head)
    path_reached = False
    while head.get_last_frame() != 0:
        print(grid)
        x, y = head.get_location()
        direction = head.choose_direction()
        if direction == 0:
            head = head.get_last_frame()
            head.set_next_frame(0)
            direction = head.choose_direction()
        xMove, yMove  = grid_movements_direction[direction]
        while not valid_coordinates(len(grid), (x+xMove, y+yMove)):
            direction = head.choose_direction()
            if direction == 0:
                print("dead end")
                head = head.get_last_frame()
                head.set_next_frame(0)
            else:
                xMove, yMove = grid_movements_direction[direction]
        if grid[x+xMove][y+yMove] != 0:
            if grid[x+xMove][y+yMove].get_end():
                print("found end")
                path_reached = True
                required, prohibated = get_required_prohibated(grid, (x,y))
                name = match_piece(prohibated, required, path_reached)
                nextPiece = make_piece(name)
                grid[x][y] = nextPiece
                while not check_valid(grid, (x, y)):
                    name = match_piece(prohibated, required, path_reached)
                    nextPiece = make_piece(name)
                    grid[x][y] = nextPiece
                link_all(grid, (x,y))
                head.set_data(nextPiece)
                head.set_completed()
                head.set_next_frame(0)
                while next.get_last_frame() != 0:
                    print("back tracking")
                    next = next.get_last_frame()
                    if next != 0:
                        if not next.get_completed():
                            required, prohibated = get_required_prohibated(grid, (x, y))
                            name = match_piece(prohibated, required, path_reached)
                            nextPiece = make_piece(name)
                            regressedx, regressedy = next.get_location()
                            grid[regressedx][regressedy] = nextPiece
                            while not check_valid(grid, (regressedx, regressedy)):
                                name = match_piece(prohibated, required, path_reached)
                                nextPiece = make_piece(name)
                                grid[regressedx][regressedy] = nextPiece
                            link_all(grid, (regressedx, regressedy))
                            next.set_data(nextPiece)
                            next.set_completed()
            elif path_reached:
                print("path reached")
                required, prohibated = get_required_prohibated(grid, (x, y))
                name = match_piece(prohibated, required, path_reached)
                nextPiece = make_piece(name)
                head.set_completed()
                head.set_next_frame(0)
                grid[x][y] = nextPiece
                while not check_valid(grid, (x, y)):
                    name = match_piece(prohibated, required, path_reached)
                    nextPiece = make_piece(name)
                    grid[x][y] = nextPiece
                link_all(grid, (x,y))
                head.set_data(nextPiece)

            else:
                print("dead end")
                head = head.get_last_frame()
                head.set_next_frame(0)
        else:
            print("moving on")
            next = myStack(head)
            head.set_next_frame(next)
            next.set_location((x + xMove, y + yMove))
            if not head.check(next):
                head = next
                
'''
'''
def generate_path(grid, start, end, screen, piece_size):
    path_reached = False
    Ex, Ey = end
    Sx , Sy = start
    start = grid[Sx][Sy]
    start = start.get_open()
    startX, startY = grid_movements_direction[start]
    start = 
    goalE = grid[Ex][Ey]
    goalE = goalE.get_open()
    endX, endY = grid_movements_direction[goalE[0]]
    goal = (Ex + endX, Ey + endY)
    while not path_reached:
        slope = get_slope(start, end)
        weights = get_weights(slope)
        choices = []
        for direction in directions:
            for i in range(int(weights[direction])):
                choices.append(direction)
        move = random.choice(choices)
        xMove, yMove = grid_movements_direction[move]
        x, y = start
        newPoint = (x + xMove, y + yMove)
        if newPoint != end:
            if valid_coordinates(len(grid), newPoint):
                requiered, prohibated = get_required_prohibated(grid, newPoint)
                name = match_piece(prohibated, requiered, path_reached)
                nextPiece = make_piece(name)
                newx, newy = newPoint
                grid[newx][newy] = nextPiece
                start = newPoint
                update_locations(grid, piece_size)
                grid[newx][newy].render(screen)
                pygame.display.flip()
        else:
            path_reached = True
            print("found end")



def get_slope(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return ((x1-x2),(y1-y2))

def get_next_point(point, size):
    x, y = point
    xMove, yMove = random.choice(grid_movements)
    if valid_coordinates(size, (x+xMove, y+yMove)):
        return True
    else:
        return False

def get_weights(slope):
    run, rise = slope
    weights = {"Left": 0, "Right": 0, "Top": 0, "Bottom": 0}
    if rise != 0 and run != 0:
        values = [math.degrees(math.atan(run/rise))/90, math.degrees(math.atan(rise/run))/90]
        if run < 0:
            weights["Left"] = math.fabs(values[0])*100 - 15
            weights["Right"] = 5
        if run > 0:
            weights["Right"] = math.fabs(values[0]) * 100 - 15
            weights["Left"] = 5
        if rise < 0:
            weights["Bottom"] = math.fabs(values[1])*100 - 15
            weights["Top"] = 5
        if rise > 0:
            weights["Top"] = math.fabs(values[0]) * 100 - 15
            weights["Bottom"] = 5
    else:
        if rise == 0 and run < 0:
            weights["Left"] = 100
        elif rise == 0 and run > 0:
            weights["Right"] = 100
        elif rise < 0 and run == 0:
            weights["Bottom"] = 100
        elif rise > 0 and run == 0:
            weights["Top"] = 100
    return weights

def valid_coordinates(size, point):
    x, y = point
    valid =  True
    if x < 0 or y < 0 or x == size or y == size:
        valid = False
    return valid
'''

def generate_path(current, grid, path_reached):
    currentx, currenty = current
    if grid[currentx][currenty] != 0 and grid[currentx][currenty] != 1:
        required, prohibated = get_required_prohibated(grid, current)
        while len(required) > 0:
            next = random.choice(required)
            required.remove(next)
            


def make_piece(name):
    next = "error"
    for direction in directions:
        if name in Ends[direction]:
            if name == 'BB':
                next = Bottom_Block()
            elif name == '4B':
                next = Four_Way_Block()
            elif name == 'LB':
                next = Left_Block()
            elif name == 'LBB':
                next = Left_Bottom_Block()
            elif name == 'LBTB':
                next = Left_Bottom_Top_Block()
            elif name == 'LRB':
                next = Left_Right_Block()
            elif name == 'LRBB':
                next = Left_Right_Bottom_Block()
            elif name == 'LRTB':
                next = Left_Right_Top_Block()
            elif name == 'LTB':
                next = Left_Top_Block()
            elif name == 'RB':
                next = Right_Block()
            elif name == 'RBB':
                next = Right_Bottom_Block()
            elif name == 'RBTB':
                next = Right_Bottom_Top_Block()
            elif name == 'RTB':
                next = Right_Top_Block()
            elif name == 'TB':
                next = Top_Block()
            elif name == 'TBB':
                next = Top_Bottom_Block()
        elif name in Paths[direction]:
            if name == '4C':
                next = Four_Way_Cross()
            elif name == 'H':
                next = Horizontal()
            elif name == 'LBC':
                next = Left_Bottom_Bend()
            elif name == 'LTC':
                next = Left_Top_Bend()
            elif name == 'RTC':
                next = Right_Top_Bend()
            elif name == 'RBC':
                next = Right_Bottom_Bend()
            elif name == 'V':
                next = Vertical()
            elif name == 'LRBC':
                next = Left_Right_Bottom_Cross()
            elif name == 'LRTC':
                next = Left_Right_Top_Cross()
            elif name == 'LTBC':
                next = Left_Top_Bottom_Cross()
            elif name == 'RTBC':
                next = Right_Top_Bottom_Cross()
    if next == 'error':
        print(name)
    return next


def match_piece(prohibated, required, path_reached=False):
    potentials = []
    #adds all possible pieces in any required direction
    if len(required) > 0:
        if path_reached:
            for direction in required:
                for element in Ends[direction]:
                    if element not in potentials:
                        potentials.append(element)

        for direction in required:
            for element in Paths[direction]:
                if element not in potentials:
                    potentials.append(element)
    else:
        if path_reached:
            for direction in directions:
                for element in Ends[direction]:
                    if element not in potentials:
                        potentials.append(element)

        for direction in directions:
            for element in Paths[direction]:
                if element not in potentials:
                    potentials.append(element)

    #removes any pieces in a prohibated direction
    if len(prohibated) > 0:
        if path_reached:
            for direction in prohibated:
                for element in Ends[direction]:
                    if element in potentials:
                        potentials.remove(element)

        for direction in prohibated:
            for element in Paths[direction]:
                if element in potentials:
                    potentials.remove(element)

    #makes sure all pieces go in each required direction
    potentialEnds = potentials
    potentialPaths = potentials
    for direction in required:
        potentialEnds = list(set(potentialEnds).intersection(set(Ends[direction])))
        potentialPaths = list(set(potentialPaths).intersection(set(Paths[direction])))
    potentials = potentialPaths + potentialEnds
    choice = random.randint(0, len(potentials)-1)
    return potentials[choice]

def check_valid(grid, point):
    #[top, bottom, left, right]
    x, y = point
    current = grid[x][y].get_open()
    legal = True
    for i in range(0,4):
        x, y = point
        xMove, yMove = grid_movements[i]
        x += xMove
        y += yMove
        if x == len(grid):
            if "Bottom" in current:
                legal = False
        elif y == len(grid):
            if "Right" in current:
                legal = False
        elif x < 0:
            if "Top" in current:
                legal = False
        elif y < 0:
            if "Left" in current:
                legal = False
        else:
            test = grid[x][y]
            if test != 0:
                test = test.get_open()
                if directions[i] in current:
                    if direction_opposites[directions[i]] not in test:
                        legal = False
    return legal

def update_locations(grid_array, piece_size):
    y = 0
    for row in grid_array:
        x = 0
        for piece in row:
            if piece != 0:
                try:
                    piece.set_x(x)
                    piece.set_y(y)
                    x += piece_size
                except TypeError:
                    x += piece_size
            else:
                x += piece_size
        y += piece_size

#determine start location
def determing_Start_location(grid, size):
    location = random.choice(directions)
    x = 0
    y = 0
    if location == "Top":
        y = 0
        x = random.randint(0,size-1)
    elif location == 'Bottom':
        y = size-1
        x = random.randint(0, size-1)
    elif location == 'Left':
        y = random.randint(0,size-1)
        x = 0
    elif location == 'Right':
        y = random.randint(0,size-1)
        x = size - 1

    grid[x][y] = orientation("Start")
    while not check_valid(grid, (x,y)):
        grid[x][y] = orientation("Start")
    return grid, (x,y)

def determine_End_location(grid, size):
    found = False
    while not found:
        x = random.randint(0, size-1)
        y = random.randint(0, size-1)
        if grid[x][y] == 0:
            found = True
    grid[x][y] = orientation("End")
    while not check_valid(grid, (x, y)):
        grid[x][y] = orientation("End")
    return grid, (x,y)


def orientation(switch):
    orientation = random.choice(directions)
    next = 0
    if orientation == "Top":
        if switch == "Start":
            next = Start_Top()
        else:
            next = End_Top()
    elif orientation == "Bottom":
        if switch == "Start":
            next = Start_Bottom()
        else:
            next = End_Bottom()
    elif orientation == "Left":
        if switch == "Start":
            next = Start_Left()
        else:
            next = End_Left()
    elif orientation == "Right":
        if switch == "Start":
            next = Start_Right()
        else:
            next = End_Right()

    return next

def link_all(grid, point):
    x, y = point
    current = grid[x][y]
    linkable = current.get_open()
    for direction in linkable:
        x, y = point
        xMove, yMove = grid_movements_direction[direction]
        x += xMove
        y += yMove
        next = grid[x][y]
        if next != 0:
            if direction == "Top":
                current.set_top(next)
                next.set_bottom(current)
            if direction == "Bottome":
                current.set_bottom(next)
                next.set_top(current)
            if direction == "Left":
                current.set_left(next)
                next.set_right(current)
            if direction == "Right":
                current.set_right(next)
                next.set_left(current)

def get_required_prohibated(grid, point):
    required = []
    prohibated = []
    for move in grid_movements:
        x, y = point
        xMove, yMove = move
        x += xMove
        y += yMove
        if x >= len(grid) or y >= len(grid) or x < 0 or y < 0:
            prohibated.append(grid_movements_point[move])
        else:
            test = grid[x][y]
            if test != 0:
                open_sides = test.get_open()
                if direction_opposites[grid_movements_point[move]] not in open_sides:
                    prohibated.append(grid_movements_point[move])
                else:
                    required.append(grid_movements_point[move])
    return required, prohibated