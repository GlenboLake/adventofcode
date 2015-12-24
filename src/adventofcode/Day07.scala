package adventofcode

import scala.io.Source
import scala.util.control.Breaks.break

object Day07 extends App {
  val input = Source.fromFile("day7.txt").getLines.toList
  //  List("123 -> x", "456 -> y", "x AND y -> d", "x OR y -> e", "x LSHIFT 2 -> f", "y RSHIFT 2 -> g", "NOT x -> h", "NOT y -> i")

  var wires: Map[String, Int] = Map.empty

  def getValue(key: String): Int = {
    try {
      key.toInt
    } catch {
      case t: Throwable => wires(key)
    }
  }

  def apply(rule: String) {
    var terms = rule.split(" ")
    terms.length match {
      case 3 => wires += (terms(2) -> getValue(terms(0)))
      case 4 => {
        assert(terms(0) == "NOT")
        wires += (terms(3) -> ~wires(terms(1)))
      }
      case 5 => {
        val left = getValue(terms(0))
        val op = terms(1)
        val right = getValue(terms(2))
        val wire = terms(4)
        val result: Int = op match {
          case "AND" => left & right
          case "OR" => left | right
          case "LSHIFT" => left << right
          case "RSHIFT" => left >> right
        }
        wires += (wire -> result)
      }
    }
  }

  var rules: List[String] = input
  var revisit: List[String] = Nil
  while (rules.length > 0) {
    for (rule <- rules) {
      try {
        apply(rule)
      } catch {
        case t: Throwable => revisit +:= rule
      }
    }
    rules = revisit
    revisit = Nil
  }
  println(wires("a"))

  val aValue = wires("a")
  wires = Map.empty
  wires += ("b" -> aValue)
  rules = input
  while (rules.length > 0) {
    for (rule <- rules) {
      if (!rule.endsWith("-> b")) {
        try {
          apply(rule)
        } catch {
          case t: Throwable => revisit +:= rule
        }
      }
    }
    rules = revisit
    revisit = Nil
  }
  print(wires("a"))
}