package adventofcode

import scala.io.Source

object Day9 extends App {
  type City = String
  type PathMap = Map[Tuple2[City, City], Int]
  var cities: List[City] = Nil
  var paths: PathMap = Map.empty
  val input = Source.fromFile("day9.txt").getLines
  for (line <- input) {
    val data = line.split(" ")
    val city1: City = data(0)
    val city2: City = data(2)
    val distance: Int = data(4).toInt
    paths += ((city1, city2) -> distance)
    paths += ((city2, city1) -> distance)
    if (!cities.contains(city1)) cities ::= city1
    if (!cities.contains(city2)) cities ::= city2
  }
  var min_distance = Int.MaxValue
  var max_distance = 0
  for (route <- cities.permutations) {
    var distance = 0
    for (i <- 0 to route.length-2) {
      distance += paths((route(i), route(i+1)))
    }
    if (distance < min_distance) {
      min_distance = distance
    }
    if (distance > max_distance) {
      max_distance = distance
    }
  }
  println(min_distance)
  println(max_distance)
}