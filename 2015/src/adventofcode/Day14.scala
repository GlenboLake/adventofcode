package adventofcode

import scala.io.Source
import scala.collection.mutable.MutableList

class Reindeer(speed: Int, duration: Int, rest: Int) {
  def travel(time: Int): Int = {
    var distance = 0
    var timeLeft = time
    while (timeLeft >= duration + rest) {
      timeLeft -= duration + rest
      distance += speed * duration
    }
    if (timeLeft < duration) {
      distance += speed * timeLeft
    } else {
      distance += speed * duration
    }
    distance
  }
}

object Day14 extends App {
  val input = Source.fromFile("day14.txt").getLines
  var deer: List[Reindeer] = Nil
  for (line <- input) {
    val data = line.split(" ")
    val speed: Int = data(3).toInt
    val duration: Int = data(6).toInt
    val rest = data(13).toInt
    deer ++= List(new Reindeer(speed, duration, rest))
  }
  println(deer.map { d => d.travel(2503) }.max)
  var scores: List[Int] = deer.map { x => 0 }
  
  for (t <- 1 to 2503) {
    var dists = deer.map { d => d.travel(t) }
    var bestDistance = dists.max
    for (i <- 0 to deer.length-1) {
      if (dists(i) == bestDistance)  {
        scores = scores.updated(i, scores(i)+1)
      }
    }
  }
  println(scores.max)
}