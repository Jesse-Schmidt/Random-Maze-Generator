import pygame
import random

class MazePieces():
    def __init__(self):
        self.image = 0
        self.Top = 0
        self.Bottom = 0
        self.Left = 0
        self.Right = 0
        self.x = 0
        self.y = 0
        self.end = False

    def get_top(self):
        return self.Top

    def set_top(self, newTop):
        self.Top = newTop

    def get_bottom(self):
        return self.Bottom

    def set_bottom(self, newBottom):
        self.Bottom = newBottom

    def get_left(self):
        return self.Left

    def set_left(self, newLeft):
        self.Left = newLeft

    def get_right(self):
        return self.Right

    def set_right(self, newRight):
        self.Right = newRight

    def get_image(self):
        return self.image

    def set_image(self, newImage):
        self.image = newImage

    def any_open(self):
        if self.Left == 1 or self.Right == 1 or self.Top == 1 or self.Bottom == 1:
            return True
        else:
            return False

    def get_open(self):
        opens = []
        if self.Top == 1:
            opens.append("Top")
        if self.Bottom == 1:
            opens.append("Bottom")
        if self.Left == 1:
            opens.append("Left")
        if self.Right == 1:
            opens.append("Right")
        return opens

    def get_direction(self):
        opens = self.get_open()
        return random.choice(opens)


    def set_x(self, newX):
        self.x = newX

    def get_x(self):
        return self.x

    def set_y(self, newY):
        self.y = newY

    def get_y(self):
        return self.y

    def render(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def get_end(self):
        return self.end

class Bottom_Block(MazePieces):
    def __init__(self):
        MazePieces.__init__(self)
        self.Top = 1
        self.image = pygame.image.load('Images/Bottom_Block.jpg')

class End_Bottom(MazePieces):
    def __init__(self):
        MazePieces.__init__(self)
        self.Top = 1
        self.end = True
        self.image = pygame.image.load('Images/End_Bottom.jpg')

class End_Left(MazePieces):
    def __init__(self):
        MazePieces.__init__(self)
        self.Right = 1
        self.End = True
        self.image = pygame.image.load('Images/End_Left.jpg')

class End_Right(MazePieces):
    def __init__(self):
        MazePieces.__init__(self)
        self.Left = 1
        self.end = True
        self.image = pygame.image.load('Images/End_Right.jpg')

class End_Top(MazePieces):
    def __init__(self):
        MazePieces.__init__(self)
        self.Bottom = 1
        self.end = True
        self.image = pygame.image.load('Images/End_Top.jpg')

class Four_Way_Block(MazePieces):
    def __init__(self):
        MazePieces.__init__(self)
        self.Left = 1
        self.Right = 1
        self.Top = 1
        self.Bottom = 1
        self.image = pygame.image.load('Images/Four_Way_Block.jpg')

class Four_Way_Cross(MazePieces):
    def __init__(self):
        MazePieces.__init__(self)
        self.Left = 1
        self.Right = 1
        self.Top = 1
        self.Bottom = 1
        self.image = pygame.image.load('Images/Four_Way_Cross.jpg')

class Horizontal(MazePieces):
    def __init__(self):
        MazePieces.__init__(self)
        self.Left = 1
        self.Right = 1
        self.image = pygame.image.load('Images/Horizontal.jpg')

class Left_Block(MazePieces):
    def __init__(self):
        MazePieces.__init__(self)
        self.Right = 1
        self.image = pygame.image.load('Images/Left_Block.jpg')

class Left_Bottom_Bend(MazePieces):
    def __init__(self):
        MazePieces.__init__(self)
        self.Left = 1
        self.Bottom = 1
        self.image = pygame.image.load('Images/Left_Bottom_Bend.jpg')

class Left_Bottom_Block(MazePieces):
    def __init__(self):
        MazePieces.__init__(self)
        self.Left = 1
        self.Bottom = 1
        self.image = pygame.image.load('Images/Left_Bottom_Block.jpg')

class Left_Bottom_Top_Block(MazePieces):
    def __init__(self):
        MazePieces.__init__(self)
        self.Left = 1
        self.Bottom = 1
        self.Top = 1
        self.image = pygame.image.load('Images/Left_Bottom_Top_Block.jpg')

class Left_Right_Block(MazePieces):
    def __init__(self):
        MazePieces.__init__(self)
        self.Left = 1
        self.Right = 1
        self.image = pygame.image.load('Images/Left_Right_Block.jpg')

class Left_Right_Bottom_Block(MazePieces):
    def __init__(self):
        MazePieces.__init__(self)
        self.Left = 1
        self.Bottom = 1
        self.Right = 1
        self.image = pygame.image.load('Images/Left_Right_Bottom_Block.jpg')

class Left_Right_Top_Block(MazePieces):
    def __init__(self):
        MazePieces.__init__(self)
        self.Left = 1
        self.Top = 1
        self.Right = 1
        self.image = pygame.image.load('Images/Left_Right_Top_Block.jpg')

class Left_Top_Bend(MazePieces):
    def __init__(self):
        MazePieces.__init__(self)
        self.Left = 1
        self.Top = 1
        self.image = pygame.image.load('Images/Left_Top_Bend.jpg')

class Left_Top_Block(MazePieces):
    def __init__(self):
        MazePieces.__init__(self)
        self.Left = 1
        self.Top = 1
        self.image = pygame.image.load('Images/Left_Top_Block.jpg')

class Right_Block(MazePieces):
    def __init__(self):
        MazePieces.__init__(self)
        self.Left = 1
        self.image = pygame.image.load('Images/Right_Block.jpg')

class Right_Bottom_Bend(MazePieces):
    def __init__(self):
        MazePieces.__init__(self)
        self.Right = 1
        self.Bottom = 1
        self.image = pygame.image.load('Images/Right_Bottom_Bend.jpg')

class Right_Bottom_Block(MazePieces):
    def __init__(self):
        MazePieces.__init__(self)
        self.Right = 1
        self.Bottom = 1
        self.image = pygame.image.load('Images/Right_Bottom_Block.jpg')

class Right_Bottom_Top_Block(MazePieces):
    def __init__(self):
        MazePieces.__init__(self)
        self.Right = 1
        self.Bottom = 1
        self.Top = 1
        self.image = pygame.image.load('Images/Right_Bottom_Top_Block.jpg')

class Right_Top_Bend(MazePieces):
    def __init__(self):
        MazePieces.__init__(self)
        self.Right = 1
        self.Top = 1
        self.image = pygame.image.load('Images/Right_Top_Bend.jpg')

class Right_Top_Block(MazePieces):
    def __init__(self):
        MazePieces.__init__(self)
        self.Right = 1
        self.Top = 1
        self.image = pygame.image.load('Images/Right_Top_Block.jpg')

class Start_Bottom(MazePieces):
    def __init__(self):
        MazePieces.__init__(self)
        self.Top = 1
        self.image = pygame.image.load('Images/Start_Bottom.jpg')

class Start_Left(MazePieces):
    def __init__(self):
        MazePieces.__init__(self)
        self.Right = 1
        self.image = pygame.image.load('Images/Start_Left.jpg')

class Start_Right(MazePieces):
    def __init__(self):
        MazePieces.__init__(self)
        self.Left = 1
        self.image = pygame.image.load('Images/Start_Right.jpg')

class Start_Top(MazePieces):
    def __init__(self):
        MazePieces.__init__(self)
        self.Bottom = 1
        self.image = pygame.image.load('Images/Start_Top.jpg')

class Top_Block(MazePieces):
    def __init__(self):
        MazePieces.__init__(self)
        self.Bottom = 1
        self.image = pygame.image.load('Images/Top_Block.jpg')

class Vertical(MazePieces):
    def __init__(self):
        MazePieces.__init__(self)
        self.Top = 1
        self.Bottom
        self.image = pygame.image.load('Images/Vertical.jpg')

class Top_Bottom_Block(MazePieces):
    def __init__(self):
        MazePieces.__init__(self)
        self.Top = 1
        self.Bottom = 1
        self.image = pygame.image.load('Images/Top_Bottom_Block.jpg')

class Left_Right_Bottom_Cross(MazePieces):
    def __init__(self):
        MazePieces.__init__(self)
        self.Left = 1
        self.Right = 1
        self.Bottom = 1
        self.image = pygame.image.load("Images/Left_Right_Bottom_Cross.jpg")

class Left_Right_Top_Cross(MazePieces):
    def __init__(self):
        MazePieces.__init__(self)
        self.Left = 1
        self.Right = 1
        self.Top = 1
        self.image = pygame.image.load("Images/Left_Right_Top_Cross.jpg")

class Left_Top_Bottom_Cross(MazePieces):
    def __init__(self):
        MazePieces.__init__(self)
        self.Left = 1
        self.Top = 1
        self.Bottom = 1
        self.image = pygame.image.load("Images/Left_Top_Bottom_Cross.jpg")

class Right_Top_Bottom_Cross(MazePieces):
    def __init__(self):
        MazePieces.__init__(self)
        self.Bottom = 1
        self.Right = 1
        self.Top = 1
        self.image = pygame.image.load("Images/Right_Top_Bottom_Cross.jpg")