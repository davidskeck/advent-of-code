//: Playground - noun: a place where people can play

import Foundation

let turnByTurnString = "L3, R1, L4, L1, L2, R4, L3, L3, R2, R3, L5, R1, R3, L4, L1, L2, R2, R1, L4, L4, R2, L5, R3, R2, R1, L1, L2, R2, R2, L1, L1, R2, R1, L3, L5, R4, L3, R3, R3, L5, L190, L4, R4, R51, L4, R5, R5, R2, L1, L3, R1, R4, L3, R1, R3, L5, L4, R2, R5, R2, L1, L5, L1, L1, R78, L3, R2, L3, R5, L2, R2, R4, L1, L4, R1, R185, R3, L4, L1, L1, L3, R4, L4, L1, R5, L5, L1, R5, L1, R2, L5, L2, R4, R3, L2, R3, R1, L3, L5, L4, R3, L2, L4, L5, L4, R1, L1, R5, L2, R4, R2, R3, L1, L1, L4, L3, R4, L3, L5, R2, L5, L1, L1, R2, R3, L5, L3, L2, L1, L4, R4, R4, L2, R3, R1, L2, R1, L2, L2, R3, R3, L1, R4, L5, L3, R4, R4, R1, L2, L5, L3, R1, R4, L2, R5, R4, R2, L5, L3, R4, R1, L1, R5, L3, R1, R5, L2, R1, L5, L2, R2, L2, L3, R3, R3, R1"

let turnByTurn = turnByTurnString.components(separatedBy: ", ")

enum CardinalDirections {
    case north
    case south
    case east
    case west
}

enum TurnDirections {
    case left
    case right
}

var currentDirection: CardinalDirections = .north

func changeDirection(currentTurn: TurnDirections) {
    switch currentDirection {
    case .north:
        if currentTurn == .left {
            currentDirection = .west
        } else {
            currentDirection = .east
        }
    case .east:
        if currentTurn == .left {
            currentDirection = .north
        } else {
            currentDirection = .south
        }
    case .south:
        if currentTurn == .left {
            currentDirection = .east
        } else {
            currentDirection = .west
        }
    case .west:
        if currentTurn == .left {
            currentDirection = .south
        } else {
            currentDirection = .north
        }
    }
}

extension String {
    var integerValue:Int {
        return Int(String(self)) ?? 0
    }
}

struct Point {
    var x = 0
    var y = 0
}

let origin = Point()
var destination = Point()
var previousDestination = Point()
var destinationsVisited = [Point]()
var firstDestinationVistedTwice = Point()

for turn in turnByTurn {
    var numberOfSteps = ""
    previousDestination = destination
    
    for character in turn.characters {
        if character == "L" {
            changeDirection(currentTurn: .left)
        } else if character == "R" {
            changeDirection(currentTurn: .right)
        } else {
            numberOfSteps.insert(character, at: numberOfSteps.endIndex)
        }
    }
    
    let numberOfStepsInt = numberOfSteps.integerValue
    
    switch currentDirection {
    case .north:
        destination.y += numberOfStepsInt
    case .east:
        destination.x += numberOfStepsInt
    case .south:
        destination.y -= numberOfStepsInt
    case .west:
        destination.x -= numberOfStepsInt
    }
    
    var nextPath = previousDestination
    for x in 1...numberOfStepsInt {
        switch currentDirection {
        case .north:
            nextPath.y += 1
        case .east:
            nextPath.x += 1
        case .south:
            nextPath.y -= 1
        case .west:
            nextPath.x -= 1
        }
        for previousDestination in destinationsVisited {
            if previousDestination.x == nextPath.x && previousDestination.y == nextPath.y {
                print("The first location visited twice is", abs(nextPath.x) + abs(nextPath.y), "blocks away.")
            }
        }
        destinationsVisited.append(nextPath)
    }

}

print("The distance in blocks from the final point is", abs(destination.x) + abs(destination.y))
