def checkStraightLine(coordinates: list[list[int]]) -> bool:
    for point in coordinates:
        if point[1] - point[0] == 1 or point[0] - point[1] == -1:
            print(point)
            pass
        else:
            return False
    return True


coordinates = [[0, 0], [0, 1], [0, -1]]
print(checkStraightLine(coordinates))
