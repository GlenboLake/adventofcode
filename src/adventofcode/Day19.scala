

package adventofcode

import scala.io.Source

object Day19 extends App {
  var replacements: List[Tuple2[String, String]] = Nil
  var starting: String = ""
  val rep = "([A-Za-z]+) => ([A-Za-z]+)".r
  val medicine = "[A-Za-z]+".r
  for (line <- Source.fromFile("day19.txt").getLines) {
    line match {
      case rep(before, after) => {
        replacements +:= (before, after)
      }
      case medicine => {
        starting = line
      }
    }
  }

  val element = "[A-Z][a-z]?".r
  val elements = element.findAllMatchIn(starting).map { x => x.toString }.toList

  var combinations: Set[String] = Set.empty

  // Calibration
  for (rep <- replacements) {
    for (i <- 0 to elements.length-1) {
      if (elements(i) == rep._1) {
        combinations += (elements.slice(0, i) ++ rep._2 ++ elements.slice(i+1, elements.length)).mkString("")
      }
    }
  }
  println(combinations.size)
  
  // Fabrication
  val reductions = replacements.sortBy(x => x._2.length).reverse
  var steps = 0
  var sequence = starting
  while (sequence != "e") {
    for (red <- reductions) {
      while (sequence.contains(red._2)) {
        sequence = sequence.replaceFirst(red._2, red._1)
        steps += 1
      }
    }
  }
  println(steps)
}