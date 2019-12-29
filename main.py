import math

# This Programs basically tells you that a point is in the circle or not

def isinsidethecircle(radius,centre,other_point):
    # Absoulute Value is needed
    length = abs(other_point[0]) - abs(centre[0])
    breadth = abs(other_point[1]) - abs(centre[1])
    distance_between_centre_and_point = math.sqrt((length*length)+(breadth*breadth))
    if distance_between_centre_and_point > radius:
        return False
    else:
        return True
