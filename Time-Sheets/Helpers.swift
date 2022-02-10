// Helpers.swift

import Foundation

func getInput() -> [String] {
	print("Enter input: ", terminator: "")
	let input = readLine()!.replacingOccurrences(of: " ", with: "")
	let inputArray = input.components(separatedBy: ",")

	guard inputArray.count == 3 else { fatalError("Please enter 3 items: Location, StartTime and EndTime") }

	return inputArray
}

func translateInput(userInput: [String]) -> WorkInformation {
	WorkInformation(location: Int(userInput[0])!, startTime: decodeTimesToNumbers(userInput[1]), endTime: decodeTimesToNumbers(userInput[2]))
}

func decodeTimesToNumbers(_ input: String) -> Double {
	switch input {
			case "1": return 9
			case "2": return 9.5
			case "3": return 10
			case "4": return 10.5
			case "5": return 11
			case "6": return 11.5
			case "7": return 12
			case "8": return 12.5
			case "9": return 1
			case "A": return 1.5
			case "B": return 2
			case "C": return 2.5
			case "D": return 3
			case "E": return 3.5
			case "F": return 4
			case "G": return 4.5
			case "H": return 5
			default:  fatalError("Invalid Time! - Please try again")
	}
}

func calculation(with workInformation: WorkInformation) -> Double {
	let endTime     = workInformation.endTime   >= 1 && workInformation.endTime   < 9 ? workInformation.endTime   + 12 : workInformation.endTime
	let startTime   = workInformation.startTime >= 1 && workInformation.startTime < 9 ? workInformation.startTime + 12 : workInformation.startTime
	let hoursWorked = abs(endTime - startTime)
	switch workInformation.location {
			case 1...9:     return abs(workInformation.endTime - workInformation.startTime) * 10.0
			case 10...19:   return hoursWorked <= 4 ? hoursWorked * 8  : 32 + (hoursWorked - 4) * 12
			case 20...29  : return hoursWorked <= 4 ? hoursWorked * 12 : 48 + (hoursWorked - 4) * 24
			default: fatalError("Invalid Location! - Please try again")
	}
}