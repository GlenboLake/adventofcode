package adventofcode

import java.security.MessageDigest

object Day4 extends App {
  def md5(s: String) = MessageDigest.getInstance("MD5").digest(s.getBytes).map("%02X" format _).mkString
  val input = "ckczppom"
  
  var value = 0
  while (md5(input+value).slice(0, 5) != "00000") {
    value += 1
  }
  println(value)
  value = 0
  while (md5(input+value).slice(0, 6) != "000000") {
    value += 1
  }
  println(value)
}