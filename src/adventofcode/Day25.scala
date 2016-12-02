package adventofcode

object Day25 extends App {
  def nextCode(code: Long): Long = {
    (code * 252533) % 33554393
  }

  def codeAt(row: Int, column: Int): Int = {
    (row + column - 1) * (row + column) / 2 - row + 1
  }

  val row = 2978
  val column = 3083
  var code = 20151125L
  for (i <- 2 to codeAt(row, column))
    code = nextCode(code)
  println(code)
}