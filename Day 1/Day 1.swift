// Notes:
// Command-line Swift. Using the latest snapshot too (November 30th).
// The hardest parts were getting the file to open, which is super easy in other languages
// and finding a fast way to do the second part, which requires a lot of iterating.
// I wonder if I got into trouble because of Swift's problems with large arrays.
// Good challange overall, really demonstrates how important it can be to have the
// right data structure for certain problems. :D

import Foundation

let inputFilePath = URL(fileURLWithPath: FileManager.default.currentDirectoryPath + "/Day 1/input.txt")

do {
    let text = try String(contentsOf: inputFilePath, encoding: .utf8)
    let lines: [String] = text.components(separatedBy: "\n")
    var totalValue = 0
    var firstIterationTotal = 0
    var firstRepeatingNumber = 0
    var firstRepeatingNumberFound = false
    var valueHistory = Set<Int>()
    valueHistory.insert(totalValue)
    for line in lines {
        if let currentNumber = Int(line) {
            totalValue += currentNumber

            if !firstRepeatingNumberFound {
                if valueHistory.contains(totalValue) {
                    firstRepeatingNumber = totalValue
                    firstRepeatingNumberFound = true
                }
            }

            valueHistory.insert(totalValue)
        } else {
            print("Uh oh. Error occured.")
        }
    }

    firstIterationTotal = totalValue

    while !firstRepeatingNumberFound {
        for line in lines {
            if let currentNumber = Int(line) {
                totalValue += currentNumber

                if !firstRepeatingNumberFound {
                    if valueHistory.contains(totalValue) {
                        firstRepeatingNumber = totalValue
                        firstRepeatingNumberFound = true
                        break
                    }
                }

                valueHistory.insert(totalValue)
            } else {
                print("Uh oh. Error occured.")
            }
        }
    }

    print("Challenge 1:", firstIterationTotal)
    if firstRepeatingNumberFound {
        print("Challenge 2:", firstRepeatingNumber)
    }
}
catch {
    print(error)
}
