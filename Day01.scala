package adventofcode

import scala.io.Source

object Day1 extends App {
  val input = Source.fromFile("day1.txt").mkString
  var floor: Int = 0
  var index: Int = 0
  var basement = false
  for (ch <- input) {
    index += 1
    ch match {
      case '(' => floor += 1
      case ')' => floor -= 1
    }
    if (!basement && floor < 0) {
      basement = true
      println("Entered basement! " + index.toString)
    }
  }
  println(floor)
}