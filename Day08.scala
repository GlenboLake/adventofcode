package adventofcode

import scala.io.Source
import scala.reflect.macros.blackbox.Context
import scala.language.experimental.macros


object Day8 extends App {
  
  val input = Source.fromFile("day8.txt").getLines
  var part1 = 0
  var part2 = 0
  for (line <- input) {
    println(line)
    //println(Eval.eval(line))
    part2 += line.count { x => x=='"' || x=='\\' } + 2
  }
  println("part 1 is " + part1)
  println("part 2 is " + part2)
}