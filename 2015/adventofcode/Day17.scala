package adventofcode

import scala.io.Source

/**
 * @author ghaber
 */
class Container(size: Int) {
  val capacity = size
  override def toString(): String = {
    capacity.toString()
  }
}

object Day17 extends App {
  val containers: List[Container] = Source.fromFile("day17.txt").getLines().map { x => new Container(x.toInt) }.toList
  var options = 0
  val capacity = 150
  var sizeOptions: Map[Int, Int] = Map.empty
  for (size <- 1 to containers.length) {
    for (combo <- containers.combinations(size)) {
      if (combo.map { x => x.capacity }.sum == capacity) {
        options += 1
        if (sizeOptions.contains(combo.length)) {
          sizeOptions += (combo.length -> (sizeOptions(combo.length) + 1))
        } else {
          sizeOptions += (combo.length -> 1)
        }
      }
    }
  }
  println(options)
  println(sizeOptions(sizeOptions.keys.min))
}