package adventofcode

import scala.io.Source

object Day05 extends App {
  val input = Source.fromFile("day5.txt").getLines().toTraversable

  def vowelCount(str: String): Int = {
    str.count { ch => "aeiou".contains(ch) }
  }
  def doubleLetters(str: String): Int = {
    def countSubstring(str: String, substr: String) = substr.r.findAllMatchIn(str).length
    ('a' to 'z').map { ch => ch.toString * 2 }.map { s => countSubstring(str, s) }.sum
  }
  def containsForbidden(str: String): Boolean = {
    List("ab", "cd", "pq", "xy").exists { sub => str.containsSlice(sub) }

  }

  def nice(str: String): Boolean = {
    vowelCount(str) >= 3 && doubleLetters(str) >= 1 && !containsForbidden(str)
  }

  println(input.count { x => nice(x) })

  def hasSandwich(str: String): Boolean = {
    """(.).\1""".r.findFirstIn(str).nonEmpty
  }
  def hasDoublePairs(str: String): Boolean = {
    """(..).*\1""".r.findFirstIn(str).nonEmpty
  }

  def reallyNice(str: String): Boolean = {
    hasSandwich(str) && hasDoublePairs(str)
  }

  println(input.count { x => reallyNice(x) })
}