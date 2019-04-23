import math

class Camera:
    pos = [0, 0, 0] #The cameras position (xPos, yPos, ZPos)
    rot = [0, 0] #The cameras rotation (xRot, yRot)
    rotRad = [(rot[0] / 180 * math.pi), (rot[1] / 180 * math.pi)] #Convert the rotation to radian