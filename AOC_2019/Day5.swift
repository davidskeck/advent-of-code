let puzzleInput = """
3,225,1,225,6,6,1100,1,238,225,104,0,2,106,196,224,101,-1157,224,224,4,224,102,8,223,223,1001,224,7,224,1,224,223,223,1002,144,30,224,1001,224,-1710,224,4,224,1002,223,8,223,101,1,224,224,1,224,223,223,101,82,109,224,1001,224,-111,224,4,224,102,8,223,223,1001,224,4,224,1,223,224,223,1102,10,50,225,1102,48,24,224,1001,224,-1152,224,4,224,1002,223,8,223,101,5,224,224,1,223,224,223,1102,44,89,225,1101,29,74,225,1101,13,59,225,1101,49,60,225,1101,89,71,224,1001,224,-160,224,4,224,1002,223,8,223,1001,224,6,224,1,223,224,223,1101,27,57,225,102,23,114,224,1001,224,-1357,224,4,224,102,8,223,223,101,5,224,224,1,224,223,223,1001,192,49,224,1001,224,-121,224,4,224,1002,223,8,223,101,3,224,224,1,223,224,223,1102,81,72,225,1102,12,13,225,1,80,118,224,1001,224,-110,224,4,224,102,8,223,223,101,2,224,224,1,224,223,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,7,677,226,224,102,2,223,223,1005,224,329,101,1,223,223,108,226,226,224,102,2,223,223,1006,224,344,101,1,223,223,1108,226,677,224,102,2,223,223,1006,224,359,1001,223,1,223,107,677,677,224,1002,223,2,223,1005,224,374,1001,223,1,223,1107,226,677,224,102,2,223,223,1005,224,389,1001,223,1,223,107,677,226,224,1002,223,2,223,1005,224,404,101,1,223,223,8,226,677,224,102,2,223,223,1005,224,419,101,1,223,223,7,226,677,224,1002,223,2,223,1005,224,434,101,1,223,223,1007,677,677,224,102,2,223,223,1006,224,449,1001,223,1,223,107,226,226,224,1002,223,2,223,1006,224,464,1001,223,1,223,1007,226,226,224,102,2,223,223,1006,224,479,1001,223,1,223,1008,226,226,224,102,2,223,223,1006,224,494,101,1,223,223,7,677,677,224,102,2,223,223,1005,224,509,1001,223,1,223,108,677,226,224,102,2,223,223,1005,224,524,101,1,223,223,1108,677,226,224,1002,223,2,223,1006,224,539,101,1,223,223,1108,677,677,224,102,2,223,223,1005,224,554,101,1,223,223,8,677,226,224,102,2,223,223,1005,224,569,101,1,223,223,8,677,677,224,102,2,223,223,1005,224,584,101,1,223,223,1107,226,226,224,102,2,223,223,1006,224,599,101,1,223,223,108,677,677,224,102,2,223,223,1006,224,614,101,1,223,223,1008,677,226,224,1002,223,2,223,1005,224,629,1001,223,1,223,1107,677,226,224,102,2,223,223,1005,224,644,101,1,223,223,1008,677,677,224,1002,223,2,223,1005,224,659,101,1,223,223,1007,677,226,224,1002,223,2,223,1005,224,674,1001,223,1,223,4,223,99,226
"""

let OPCODE_SIZE = 5

enum OpCode: Int {
	case ADD =   1
	case MULT =  2
	case INPUT = 3 // requests integer as input and save at position
	case OUT =   4 // take integer and print it
	case HCF =  99 // halt
}

let OperationSizes = [
	OpCode.ADD:   4,
	OpCode.MULT:  4,
	OpCode.INPUT: 2,
	OpCode.OUT:   2,
	OpCode.HCF:   1,
]

enum ParameterMode: Int {
	case POSITION_MODE =  0 // fetch from index
	case IMMEDIATE_MODE = 1 // use as value
}

struct Parameter {
	let value: Int
	let mode: ParameterMode
}

struct IntcodeOperation {
    let opcode: OpCode
    let parameters: [Parameter]
}

struct ExecutionState {
    var instructionPointer = 0
    var executionShouldProceed = true
}

var lines = puzzleInput.split { $0 == "," }
var intcodeProgram: [Int] = []
for line in lines {
    if let value = Int(line) {
        intcodeProgram.append(value)
    }
}

func runOperation(state: inout ExecutionState, operation: IntcodeOperation) {
	switch operation.opcode {
	case .ADD:
		break
	case .MULT:
		break
	case .INPUT:
		print("Input: ")
	    let input = readLine()!
		intcodeProgram[operation.parameters[0].value] = Int(input)!
		state.instructionPointer = state.instructionPointer + OperationSizes[operation.opcode]!
	case .OUT:
		switch operation.parameters[0].mode {
		case .POSITION_MODE:
			print(intcodeProgram[operation.parameters[0].value])
		case .IMMEDIATE_MODE:
			print(operation.parameters[0].value)
		}
		state.instructionPointer = state.instructionPointer + OperationSizes[operation.opcode]!x
	case.HCF:
		state.executionShouldProceed = false
	}
}

var state = ExecutionState()

while state.executionShouldProceed {
	let instruction = intcodeProgram[state.instructionPointer]
	let size = String(instruction).count
	
    switch size {
    case 1, 2:
		let opCode = OpCode(rawValue: intcodeProgram[state.instructionPointer])!		
		let size = OperationSizes[opCode]!
		var parameters: [Parameter] = []
		for i in 1 ..< size
		{
			let parameter = Parameter(value: intcodeProgram[state.instructionPointer + i], mode: ParameterMode(rawValue: 0)!)
			parameters.append(parameter)
		}
		
		let operation = IntcodeOperation(opcode: opCode, parameters: parameters)
		runOperation(state: &state, operation: operation)
	case 3:
		break
	case 4:
		break
	case 5:
		break
	default:
		break
	}
}

//
// func parseOperationData(opData: String) -> (OpCode?, [ParameterMode]?) {
// 	if opData.count >= OPCODE_SIZE {
//
// 	}
// }
//
// func populateOperation(opData: String, instructionData: intcodeProgram) -> IntcodeOperation {
// 	let (opcode, parameterModes) = parseOperationData(opData)
//
//
// 	let operation = IntcodeOperation(opcode:
// }
//
// func executeIntcodeOperation(state: inout ExecutionState, operation: IntcodeOperation) {
//
//     if operation.opcode == OPCODE_ADD {
//         let result = intcodeProgram[operation.inputOnePosition] + intcodeProgram[operation.inputTwoPosition]
//         intcodeProgram[operation.outputPosition] = result
//     }
//     else if operation.opcode == OPCODE_MULT {
//         let result = intcodeProgram[operation.inputOnePosition] * intcodeProgram[operation.inputTwoPosition]
//         intcodeProgram[operation.outputPosition] = result
//     }
//     else if operation.opcode == OPCODE_HCF {
//         state.executionShouldProceed = false
//     }
// }
//
// func sufficientInstructionsRemain(state: ExecutionState, instructionData: [Int]) -> Bool {
//     return state.instructionPointer + 1 < instructionData.count
// }
//
// var state = ExecutionState()
//
// while state.executionShouldProceed {
//     if sufficientInstructionsRemain(state: state, instructionData: intcodeProgram) {
// 		let operation = IntcodeOperation(opcode:)
//         let operation = IntcodeOperation(opcode: intcodeProgram[state.instructionPointer], inputOnePosition: intcodeProgram[state.instructionPointer + 1], inputTwoPosition: intcodeProgram[state.instructionPointer + 2], outputPosition: intcodeProgram[state.instructionPointer + 3])
//         executeIntcodeOperation(state: state, operation: operation)
//         state.instructionPointer += 4
//     }
//     else
//     {
//         state.executionShouldProceed = false
//     }
// }
//
// intcodeProgram
//
// // MARK: Part Two
//
// let desiredResult = 19690720
//
// var intcodeProgramConstant: [Int] = []
// for line in lines {
//     if let value = Int(line) {
//         intcodeProgramConstant.append(value)
//     }
// }
//
// for noun in 0 ... 99 {
//     for verb in 0 ... 99 {
//         intcodeProgram = intcodeProgramConstant
//
//         intcodeProgram[1] = noun
//         intcodeProgram[2] = verb
//
//         state = ExecutionState()
//
//         while state.executionShouldProceed {
//             if sufficientInstructionsRemain(state: state, instructionData: intcodeProgram) {
//                 let operation = IntcodeOperation(opcode: intcodeProgram[state.instructionPointer], inputOnePosition: intcodeProgram[state.instructionPointer + 1], inputTwoPosition: intcodeProgram[state.instructionPointer + 2], outputPosition: intcodeProgram[state.instructionPointer + 3])
//                 executeIntcodeOperation(state: state, operation: operation)
//                 state.instructionPointer += 4
//             }
//             else
//             {
//                 state.executionShouldProceed = false
//             }
//         }
//
//         if intcodeProgram[0] == desiredResult {
//             100 * noun + verb
//             break
//         }
//
//     }
// }
