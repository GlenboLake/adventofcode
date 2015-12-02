package adventofcode

import scala.io.Source


object Day2 extends App {
  var input = Source.fromFile("day2.txt")
  var total_paper = 0
  var total_ribbon = 0
  for (present <- input.getLines) {
    var dims = present.split("x").toList.map { s: String => s.toInt }
    var sides = List(dims(0)*dims(1), dims(0)*dims(2), dims(1)*dims(2))
    total_paper += 2*sides.sum + sides.min
    total_ribbon += dims.product + 2 * dims.sum - 2 * dims.max
  }
  println("Paper: " + total_paper)
  println("Ribbon: " + total_ribbon)
  input.close()
}