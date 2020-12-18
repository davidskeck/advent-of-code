
def trees_per_slope(input_data, xSlope, ySlope):
    yIdx = 0
    xIdx = 0
    treeCount = 0
    listLength = len(input_data)
    lineLength = len(input_data[0])
    while yIdx + ySlope < listLength:
        yIdx += ySlope
        xIdx += xSlope
        if xIdx > lineLength - 1:
            xIdx -= lineLength
        if input_data[yIdx][xIdx] == '#':
            treeCount += 1
    
    return treeCount


def main():
    input_data = []
    with open("input.txt") as input:
        for line in input:
            input_data.append(line.strip())

    input_data = input_data[:-1]
    
    treeCount = trees_per_slope(input_data, 3, 1)

    print("Trees encountered (p1): {}".format(treeCount))

    partTwoInputs = [(1, 1), (5, 1), (7, 1), (1, 2)]

    partTwoAnswer = treeCount
    for slope in partTwoInputs:
        xSlope, ySlope = slope
        treesFound = trees_per_slope(input_data, xSlope, ySlope)
        partTwoAnswer *= treesFound

    print("P2 trees multiplied (p2): {}".format(partTwoAnswer))
        

if __name__ == "__main__":
    main()

