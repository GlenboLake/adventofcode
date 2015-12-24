package adventofcode

object Day22 extends App {
  var best = Int.MaxValue
  val bossStartHP = 58
  val bossAttack = 9

  val spellCosts = Map[String, Int]("Magic Missile" -> 53, "Drain" -> 73, "Shield" -> 113, "Poison" -> 173, "Recharge" -> 229)
  val spells: List[String] = spellCosts.keys.toList

  def simulate(bossHP: Int, playerHP: Int, mana: Int, cost: Int, spell: String,
    shieldCharges: Int, poisonCharges: Int, rechargeCharges: Int): Unit = {
    if (cost > best) return

    var nBossHP = bossHP
    var nPlayerHP = playerHP - 1
    var nMana = mana
    var nCost = cost
    var nShieldCharges = shieldCharges
    var nPoisonCharges = poisonCharges
    var nRechargeCharges = rechargeCharges

    if (nPlayerHP <= 0) return

    // Apply effects before player turn
    if (nShieldCharges > 0) {
      nShieldCharges -= 1
    }
    if (nPoisonCharges > 0) {
      nBossHP -= 3
      nPoisonCharges -= 1
    }
    if (nRechargeCharges > 0) {
      nMana += 101
      nRechargeCharges -= 1
    }

    if (nBossHP <= 0) {
      if (nCost < best) best = nCost
      return
    }

    // Cast spell
    nCost += spellCosts(spell)
    nMana -= spellCosts(spell)
    spell match {
      case "Magic Missile" => {
        nBossHP -= 4
      }
      case "Drain" => {
        nBossHP -= 2
        nPlayerHP += 2
      }
      case "Shield" => {
        if (nShieldCharges > 0) { return }
        nShieldCharges = 6
      }
      case "Poison" => {
        if (nPoisonCharges > 0) { return }
        nPoisonCharges = 6
      }
      case "Recharge" => {
        if (nRechargeCharges > 0) { return }
        nRechargeCharges = 5
      }
    }

    if (nBossHP <= 0) {
      if (nCost < best) best = nCost
      return
    }

    // Apply effects before boss turn
    var armor = 0
    if (nShieldCharges > 0) {
      armor = 7
      nShieldCharges -= 1
    }
    if (nPoisonCharges > 0) {
      nBossHP -= 3
      nPoisonCharges -= 1
    }
    if (nRechargeCharges > 0) {
      nMana += 101
      nRechargeCharges -= 1
    }

    if (nBossHP <= 0) {
      if (nCost < best) best = nCost
      return
    }

    val damage = List(bossAttack - armor, 1).max
    nPlayerHP -= damage

    if (nPlayerHP <= 0) return

    for (nextSpell <- spells)
      if (nMana > spellCosts(nextSpell))
        simulate(nBossHP, nPlayerHP, nMana, nCost, nextSpell, nShieldCharges, nPoisonCharges, nRechargeCharges)
  }

  for (spell <- spells)
    simulate(bossStartHP, 50, 500, 0, spell, 0, 0, 0)
  println(best)
}