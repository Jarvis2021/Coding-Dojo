import UIKit

let type: String = "Rectangle"
let description: String = "A quadrilateral with four right angles"
var width: Float = 5
var height: Float = 10.5
var area: Float = width * height
height += 1
width += 1
area = width * height
// Note how you can "interpolate" variables into Strings using the following syntax
print("The shape is a \(type) or \(description) with an area of \(area)")
