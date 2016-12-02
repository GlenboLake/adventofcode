package adventofcode

import scala.io.Source
import scala.collection.mutable.MutableList

object Day23 extends App {
  // Registers
  var registers = MutableList[Int](1, 0)
  val instructions = Source.fromFile("day23.txt").getLines().toList
//  val instructions = List("inc a", "jio a, +2", "tpl a", "inc a")
  var instOffset = 0
  
  val register = """(\w+) ([ab])""".r
  val jump = """jmp ([+-]\d+)""".r
  val conditionalJump = """(ji[eo]) ([ab]), ([+-]\d+)""".r
  
  while (instOffset >= 0 && instOffset < instructions.length) {
    println(s"$instOffset: ${instructions(instOffset)}")
    instructions(instOffset) match {
      case register(op, reg) => {
        val regIndex = if (reg=="a") 0 else 1
        op match {
          case "hlf" =>
            registers(regIndex) /= 2
          case "tpl" =>
            registers(regIndex) *= 3
          case "inc" =>
            registers(regIndex) += 1
        }
        instOffset += 1
      }
      case jump(offset) => {
        instOffset += offset.toInt
      }
      case conditionalJump(op, reg, offset) => {
        val regIndex = if (reg=="a") 0 else 1
        val jump: Boolean = op match {
          case "jie" => registers(regIndex) % 2 == 0
          case "jio" => registers(regIndex) == 1
        }
        instOffset += (if (jump) offset.toInt else 1)
      }
    }
  }
  println(registers(0), registers(1))
}