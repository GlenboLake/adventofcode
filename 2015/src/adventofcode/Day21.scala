package adventofcode

object Day21 extends App {
  val bossHP = 109
  val bossDamage = 8
  val bossArmor = 2
  def turnsToDeath(attack: Int, defense: Int, hp: Int): Int = {
    math.ceil(hp.toDouble / List(attack - defense, 1).max).toInt
  }

  def sumTuples(list: Seq[Tuple3[Int, Int, Int]]): Tuple3[Int, Int, Int] = {
    list.foldLeft((0, 0, 0)) {
      case ((a, b, c), (x, y, z)) => (a + x, b + y, c + z)
    }
  }

  val weapons = List((8, 4, 0), (10, 5, 0), (25, 6, 0), (40, 7, 0), (74, 8, 0))
  val armors = List((0, 0, 0), (13, 0, 1), (31, 0, 2), (53, 0, 3), (75, 0, 4), (102, 0, 5))
  val ringsInShop = List((25, 1, 0), (50, 2, 0), (100, 3, 0), (20, 0, 1), (40, 0, 2), (80, 0, 3))
  val rings = List((0, 0, 0)) ++ ringsInShop ++ ringsInShop.combinations(2).map { x => sumTuples(x) }

  var winCost = Int.MaxValue
  var loseCost = 0
  for (weapon <- weapons) {
    for (armor <- armors) {
      for (ring <- rings) {
        val equipment = sumTuples(List(weapon, armor, ring))
        val bossTurns = turnsToDeath(equipment._2, bossArmor, bossHP)
        val playerTurns = turnsToDeath(bossDamage, equipment._3, 100)
        if (playerTurns > bossTurns && equipment._1 < winCost) {
          winCost = equipment._1
        }
        if (playerTurns <= bossTurns && equipment._1 > loseCost) {
          loseCost = equipment._1
        }
      }
    }
  }
  println(winCost)
  println(loseCost)
}