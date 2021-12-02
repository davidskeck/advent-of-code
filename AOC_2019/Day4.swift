let puzzleInput = "197487-673251"

import Foundation

struct PasswordRange {
    let begin: Int
    let end: Int
}

func populateRange(input: String) -> PasswordRange? {
    let range = input.split { $0.isPunctuation }
    if range.count == 2 {
        if let rangeBegin = Int(range[0]) {
            if let rangeEnd = Int(range[1]) {
                return PasswordRange(begin: rangeBegin, end: rangeEnd)
            }
        }
    }
    return nil
}

func ensureSixDigits(input: Int) -> Bool {
    // It is a six-digit number.
    let password = String(input)
    return password.count == 6
}

func ensureAdjacentDigits(input: Int) -> Bool {
    // Two adjacent digits are the same (like 22 in 122345).
    let password = String(input)
    return password.range(of: #"(\d)\1+"#, options: .regularExpression) != nil
}

func ensureNoDecrease(input: Int) -> Bool {
    let password = String(input)
    // Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
    var passwordOK = false
    for i in 0 ..< password.count - 1 {
        let currentIndex = password.index(password.startIndex, offsetBy: i)
        let nextIndex = password.index(password.startIndex, offsetBy: i + 1)
        let currentValue = String(password[currentIndex])
        let nextValue = String(password[nextIndex])
        
        if let currentInt = Int(currentValue) {
            if let nextInt = Int(nextValue) {
                if currentInt <= nextInt {
                    passwordOK = true
                } else {
                    passwordOK = false
                    break
                }
            }
        }
    }
    return passwordOK
}

func ensureOnlyTwoAdjacentDigits(input: Int) -> Bool {
    let password = String(input)
    
    var passwordOK = false
    for i in 0 ... password.count - 3 {
        let currentIndex = password.index(password.startIndex, offsetBy: i)
        let nextIndex = password.index(password.startIndex, offsetBy: i + 1)
        let finalIndex = password.index(password.startIndex, offsetBy: i + 2)
        let currentValue = String(password[currentIndex])
        let nextValue = String(password[nextIndex])
        let finalValue = String(password[finalIndex])
        
        if let currentInt = Int(currentValue) {
            if let nextInt = Int(nextValue) {
                if let finalInt = Int(finalValue) {
                    if i == 0 {
                        if currentInt == nextInt && finalInt != currentInt {
                            passwordOK = true
                            break
                        }
                    } else if i == password.count - 3 {
                        if(nextInt == finalInt && currentInt != finalInt) {
                            passwordOK = true
                            break
                        }
                    }
                    if i > 0 {
                        if currentInt == nextInt {
                            let previousIndex = password.index(password.startIndex, offsetBy: i - 1)
                            let previousValue = String(password[previousIndex])
                            if let previousInt = Int(previousValue) {
                                if previousInt != currentInt && finalInt != currentInt {
                                    passwordOK = true
                                    break
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    return passwordOK
}

if let passwordRange = populateRange(input: puzzleInput) {
    var passwordCountPartOne = 0
    
    // Within the range, exclude begin and end
    for i in passwordRange.begin + 1 ..< passwordRange.end {
        if (ensureSixDigits(input: i)) {
            if (ensureAdjacentDigits(input: i)) {
                if (ensureNoDecrease(input: i)) {
                    passwordCountPartOne += 1
                }
            }
        }
    }
    
    print(passwordCountPartOne)
    
    var passwordCountPartTwo = 0
    for i in passwordRange.begin + 1 ..< passwordRange.end {
        if (ensureSixDigits(input: i)) {
            if (ensureOnlyTwoAdjacentDigits(input: i)) {
                if (ensureNoDecrease(input: i)) {
                    passwordCountPartTwo += 1
                }
            }
        }
    }

    print(passwordCountPartTwo)
}
