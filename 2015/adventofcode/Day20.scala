package adventofcode

object Day20 extends App {
  def divisors(n: Int): List[Int] = {
    val small: Seq[Int] = for (i <- 1 to math.sqrt(n).toInt; if n % i == 0) yield i
    val large: Seq[Int] = for (i <- small; if n != i*i) yield n/i
    small.toList ++ large.toList
  }
  
  val target = 29000000
  var value = 0
  var p1: Int = 0
  var p2: Int = 0
  
  while (p1==0 || p2==0) {
    value += 1
    val div = divisors(value)
    if (p1==0) {
      if (div.sum * 10 >= target) {
        p1 = value
      }
    }
    if (p2==0) {
      if (div.filter{ d => value / d <= 50 }.sum * 11 >= target) {
        p2 = value
      }
    }
  }
  println(p1, p2)
}