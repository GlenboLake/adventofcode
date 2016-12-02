package adventofcode

import scala.io.Source

object Day13 extends App {
  type Person = String
  type Network = Map[Set[Person], Int]
  
  def parseInput(filename: String): Network = {
    var network: Network = Map.empty
    val input = Source.fromFile(filename).getLines()
    for (line <- input) {
      val data = line.split(" ")
      val person1: Person = data(0)
      val person2: Person = data(10).stripSuffix(".")
      val key: Set[Person] = Set(person1, person2)
      val delta: Int = if (data(2) == "gain") data(3).toInt else -data(3).toInt
      if (network.contains(key)) {
        val value: Int = network(key)
        network += (key -> (value + delta))
      }
      else {
        network += (key -> delta)
      }
    }
    
    network
  }
  
  def addSelf(network: Network): Network = {
    var newNetwork = network
    val people = getNames(network)
    for (person <- people) {
      val key = Set(person, "Me!")
      newNetwork += (key -> 0)
    }
    newNetwork
  }
  
  def getNames(network: Network): List[Person] = {
    network.keySet.flatten.toList
  }
  
  def score(order: List[Person], network: Network): Int = {
    var total_happiness = 0
    for (i <- 0 to order.length-2) {
      total_happiness += network(Set(order(i), order(i+1)))
    }
    total_happiness + network(Set(order(0), order(order.length-1)))
  }
  
  val network: Network = parseInput("day13.txt")
  val people: List[Person] = getNames(network)
  println("Arranging " + people.length + " people")
  var max_happiness = 0
  for (order <- people.permutations) {
    val happiness = score(order, network)
    if (happiness > max_happiness) max_happiness = happiness
  }
  println(max_happiness)
  
  val newNetwork = addSelf(network)
  val newPeople: List[Person] = getNames(newNetwork)
  println("Arranging " + newPeople.length + " people")
  max_happiness = 0
  for (order <- newPeople.permutations) {
    val happiness = score(order, newNetwork)
    if (happiness > max_happiness) max_happiness = happiness
  }
  println(max_happiness)
}