package adventofcode

import scala.io.Source

class AdjustableLight(var state: Int = 0) {
  def turnOn(): Unit = {
    state += 1
  }
  def turnOff(): Unit = {
    state -= 1
    if (state < 0) state = 0
  }
  def toggle(): Unit = {
    state += 2
  }
}

object Day06Part2 extends App {
  type Grid = Map[Tuple2[Int, Int], AdjustableLight]
  var grid: Grid = Map.empty
  val input = Source.fromFile("day6.txt").getLines()

  def adjust(startx: Int, starty: Int, endx: Int, endy: Int, action: String): Unit = {
    for (x <- startx to endx) {
      for (y <- starty to endy) {
        action match {
          case "on" => grid(x, y).turnOn()
          case "off" => grid(x, y).turnOff()
          case "toggle" => grid(x, y).toggle()
        }
      }
    }
  }
  
  def pop(): Int = {
    var total = 0
    for (light <- grid.values) total += light.state
    total
  }

  for (x <- 0 to 999) {
    for (y <- 0 to 999) {
      grid += ((x, y) -> new AdjustableLight)
    }
  }
  for (line <- input) {
    var fields = line.split(" ").toList
    if (line.startsWith("turn"))
      fields = fields.slice(1, fields.length)
    var startx = fields(1).split(",")(0).toInt
    var starty = fields(1).split(",")(1).toInt
    var endx = fields(3).split(",")(0).toInt
    var endy = fields(3).split(",")(1).toInt
    adjust(startx, starty, endx, endy, fields(0))
  }
//  for (x <- 0 to 9) {
//    for (y <- 0 to 9) {
//      print(grid(x, y))
//    }
//    println()
//  }
  print(pop)
}