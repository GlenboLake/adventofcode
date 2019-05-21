package adventofcode

object Day11 extends App {
  val input = "hxbxwxba"
  def incrementString(string: String): String = {
    val wrap = ('z' + 1).toChar.toString
    val next = (string.codePointAt(string.length - 1) + 1).toChar.toString
    if (next == wrap)
      incrementString(string.slice(0, string.length - 1)) + "a"
    else
      string.slice(0, string.length - 1) + next
  }

  def validatePassword(password: String): Boolean = {
    // Assume 8 lowercase letters is met anyway, but test new requirements.
    val ints = password.map { ch => ch.toInt }
    if (password.contains("i") || password.contains("o") || password.contains("l")) {
      false
    } else if (ints.map { i => ints.containsSlice(List(i, i + 1, i + 2)) }.forall { x => !x }) {
      false
    } else {
      val doubles = ('a' to 'z').map { ch => ch.toString * 2 }
      def countSubstring(str: String, substr: String) = substr.r.findAllMatchIn(str).length
      doubles.map { str => countSubstring(password, str) }.sum >= 2
    }
  }

  def nextPassword(old: String): String = {
    var password = incrementString(old)
    while (!validatePassword(password))
      password = incrementString(password)
    password
  }

  var next = nextPassword("hxbxwxba")
  println(next)
  println(nextPassword(next))
}