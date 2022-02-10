// main.swift

import Helpers
import Location
import WorkLocation

var workInformations = [translateInput(userInput: getInput()), 
                        translateInput(userInput: getInput()), 
                        translateInput(userInput: getInput()), 
                        translateInput(userInput: getInput())]

var totalCost = Double.zero
for info in workInformations {
	let calc = calculation(with: info)
	print("$\(calc)0")
	totalCost += calc
}

print("$\(totalCost)0")