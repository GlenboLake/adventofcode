package adventofcode

import scala.io.Source

object Day03 extends App {
  type Point = Tuple2[Int, Int]

  var santa = new Point(0, 0)
  var houses = Set.empty[Point] + santa

  var input = Source.fromFile("day3.txt").mkString
  for (ch <- input) {
    ch match {
      case '>' => santa = new Point(santa._1 + 1, santa._2)
      case '<' => santa = new Point(santa._1 - 1, santa._2)
      case '^' => santa = new Point(santa._1, santa._2 - 1)
      case 'v' => santa = new Point(santa._1, santa._2 + 1)
    }
    houses += santa
  }
  println(houses.size)

  var santas = (new Point(0, 0), new Point(0, 0))
  var which = 0
  houses = Set.empty[Point] + santas._1

  for (ch <- input) {
    var s: Point = 
    ch match {
      case '>' => new Point(santas._1._1 + 1, santas._1._2)
      case '<' => new Point(santas._1._1 - 1, santas._1._2)
      case '^' => new Point(santas._1._1, santas._1._2 - 1)
      case 'v' => new Point(santas._1._1, santas._1._2 + 1)
    }
    houses += s
    santas = (santas._2, s)
  }
  println(houses.size)
}