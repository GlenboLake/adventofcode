package adventofcode

import scala.io.Source
import scala.util.control.Breaks._

object Day24 extends App {
  val packages: List[Long] = Source.fromFile("day24.txt").getLines().map { x => x.toLong }.toList
  val groupWeight = packages.sum / 4

  var i = 2
  while (packages.combinations(i).filter { group => group.sum == groupWeight }.length == 0) {
    i += 1
  }
  println(packages.combinations(i).filter { group => group.sum == groupWeight }.map { group => group.product }.min)
}