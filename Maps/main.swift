import Foundation

let locations = ["A": 0, "B": 450, "C": 590, "D": 710, "E": 1030, "F": 1280, "G": 1360]

class HeaderInformation {
	let averageMilesPerGallon: Int
	let pricePerGallon			 : Double
	let averageSpeed         : Int

	init(averageMilesPerGallon: Int, pricePerGallon: Double, averageSpeed: Int) {
		self.averageMilesPerGallon = averageMilesPerGallon
		self.pricePerGallon 			 = pricePerGallon
		self.averageSpeed   			 = averageSpeed
	}
}

class MapInformation {
	let header: HeaderInformation
	let miles: [Int]

	init(header: HeaderInformation, miles: [Int]) {
		self.header = header
		self.miles  = miles
	}
}


func getInput() -> MapInformation {

	var hours = [Int]()
	var firstInput = [String]()

	for i in 1...6 {
		let input = readLine()!.replacingOccurrences(of: " ", with: "").uppercased().components(separatedBy: ",")
		
		if i == 1 {
			firstInput = input
		} else {
			hours.append(calculateDistance(input: input))
		}
	}

	return MapInformation(header: HeaderInformation(averageMilesPerGallon: Int(firstInput[0])!,
								 													        pricePerGallon: 			 Double(firstInput[1])!,
								 													        averageSpeed:   			 Int(firstInput[2])!),
								 			  miles: hours)
}

extension Double {
	func getIntParts() -> (whole: Int, decimal: Int) {
		let list = "\(self)".components(separatedBy: ".")
		return (Int(list[0])!, Int(list[1])!)
	}

	func getStringParts() -> (whole: String, decimal: String) {
		let list = "\(self)".components(separatedBy: ".")
		return (list[0], list[1])
	}

	func preciseRound(toPlace place: Int) -> Double {
		let divisor = pow(10.0, Double(place))
		return (self * divisor).rounded() / divisor
	}
}


func calculateDistance(input: [String]) -> Int {
	return locations[input[1]]! - locations[input[0]]!
}

func calculateOutput(info information: MapInformation) {
	print()
	for distance in information.miles {
		let time = calculateTime(distance: distance, header: information.header)
		let cost = calculateGasolineCost(distance: distance, header: information.header)
		print("\(distance), \(time), \(cost)")
	}
}

func calculateTime(distance: Int, header: HeaderInformation) -> String {
	let time = (Double(distance)/Double(header.averageSpeed)).getStringParts()

	var hours = "\(Int(Double(time.whole)!.preciseRound(toPlace: 2)))"

	var minutes = "\(Int((Double("0.\(time.decimal)")!.preciseRound(toPlace: 2) * 60).preciseRound(toPlace: 0)))"

	if hours.count < 2 { hours = "0" + hours }

	if minutes.count < 2 { minutes = "0" + minutes }

	return hours + ":" + minutes
}

func calculateGasolineCost(distance: Int, header: HeaderInformation) -> String {
	let cost = (Double(distance) / Double(header.averageMilesPerGallon)) * header.pricePerGallon
	let rounded = cost.preciseRound(toPlace: 2)

	return "$\(rounded.getStringParts().decimal.count < 2 ? "\(rounded)0" : "\(rounded)")"
}

calculateOutput(info: getInput())

// 28, 3.59, 55
// A, D
// B, F
// D, G
// C, E
// A, G

// result:

// 710, 12:55, $91.03
// 830, 15:05, $106.42
// 650, 11:49, $83.34
// 440, 08:00, $56.41
// 1360, 24:44, $174.37