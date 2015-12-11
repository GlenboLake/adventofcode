package adventofcode

object Day10 extends App {
  def lookSay(list: List[Int]): List[Int] = {
    var rv: List[Int] = Nil
    var count = 0
    var value = 0
    for (i <- list) {
      if (i == value) {
        count += 1
      } else {
        if (value > 0) {
          rv ++= List(count, value)
        }
        count = 1
        value = i
      }
    }
    rv ++ List(count, value)
  }

  val elements: Map[String, List[String]] = Map(
    "H" -> List("H"),
    "He" -> List("Hf", "Pa", "H", "Ca", "Li"),
    "Li" -> List("He"),
    "Be" -> List("Ge", "Ca", "Li"),
    "B" -> List("Be"),
    "C" -> List("B"),
    "N" -> List("C"),
    "O" -> List("N"),
    "F" -> List("O"),
    "Ne" -> List("F"),
    "Na" -> List("Ne"),
    "Mg" -> List("Pm", "Na"),
    "Al" -> List("Mg"),
    "Si" -> List("Al"),
    "P" -> List("Ho", "Si"),
    "S" -> List("P"),
    "Cl" -> List("S"),
    "Ar" -> List("Cl"),
    "K" -> List("Ar"),
    "Ca" -> List("K"),
    "Sc" -> List("Ho", "Pa", "H", "Ca", "Co"),
    "Ti" -> List("Sc"),
    "V" -> List("Ti"),
    "Cr" -> List("V"),
    "Mn" -> List("Cr", "Si"),
    "Fe" -> List("Mn"),
    "Co" -> List("Fe"),
    "Ni" -> List("Zn", "Co"),
    "Cu" -> List("Ni"),
    "Zn" -> List("Cu"),
    "Ga" -> List("Eu", "Ca", "Ac", "H", "Ca", "Zn"),
    "Ge" -> List("Ho", "Ga"),
    "As" -> List("Ge", "Na"),
    "Se" -> List("As"),
    "Br" -> List("Se"),
    "Kr" -> List("Br"),
    "Rb" -> List("Kr"),
    "Sr" -> List("Rb"),
    "Y" -> List("Sr", "U"),
    "Zr" -> List("Y", "H", "Ca", "Tc"),
    "Nb" -> List("Er", "Zr"),
    "Mo" -> List("Nb"),
    "Tc" -> List("Mo"),
    "Ru" -> List("Eu", "Ca", "Tc"),
    "Rh" -> List("Ho", "Ru"),
    "Pd" -> List("Rh"),
    "Ag" -> List("Pd"),
    "Cd" -> List("Ag"),
    "In" -> List("Cd"),
    "Sn" -> List("In"),
    "Sb" -> List("Pm", "Sn"),
    "Te" -> List("Eu", "Ca", "Sb"),
    "I" -> List("Ho", "Te"),
    "Xe" -> List("I"),
    "Cs" -> List("Xe"),
    "Ba" -> List("Cs"),
    "La" -> List("Ba"),
    "Ce" -> List("La", "H", "Ca", "Co"),
    "Pr" -> List("Ce"),
    "Nd" -> List("Pr"),
    "Pm" -> List("Nd"),
    "Sm" -> List("Pm", "Ca", "Zn"),
    "Eu" -> List("Sm"),
    "Gd" -> List("Eu", "Ca", "Co"),
    "Tb" -> List("Ho", "Gd"),
    "Dy" -> List("Tb"),
    "Ho" -> List("Dy"),
    "Er" -> List("Ho", "Pm"),
    "Tm" -> List("Er", "Ca", "Co"),
    "Yb" -> List("Tm"),
    "Lu" -> List("Yb"),
    "Hf" -> List("Lu"),
    "Ta" -> List("Hf", "Pa", "H", "Ca", "W"),
    "W" -> List("Ta"),
    "Re" -> List("Ge", "Ca", "W"),
    "Os" -> List("Re"),
    "Ir" -> List("Os"),
    "Pt" -> List("Ir"),
    "Au" -> List("Pt"),
    "Hg" -> List("Au"),
    "Tl" -> List("Hg"),
    "Pb" -> List("Tl"),
    "Bi" -> List("Pm", "Pb"),
    "Po" -> List("Bi"),
    "At" -> List("Po"),
    "Rn" -> List("Ho", "At"),
    "Fr" -> List("Rn"),
    "Ra" -> List("Fr"),
    "Ac" -> List("Ra"),
    "Th" -> List("Ac"),
    "Pa" -> List("Th"),
    "U" -> List("Pa"))

  val elemLengths: Map[String, Int] = Map(
    "H" -> "22".length,
    "He" -> "13112221133211322112211213322112".length,
    "Li" -> "312211322212221121123222112".length,
    "Be" -> "111312211312113221133211322112211213322112".length,
    "B" -> "1321132122211322212221121123222112".length,
    "C" -> "3113112211322112211213322112".length,
    "N" -> "111312212221121123222112".length,
    "O" -> "132112211213322112".length,
    "F" -> "31121123222112".length,
    "Ne" -> "111213322112".length,
    "Na" -> "123222112".length,
    "Mg" -> "3113322112".length,
    "Al" -> "1113222112".length,
    "Si" -> "1322112".length,
    "P" -> "311311222112".length,
    "S" -> "1113122112".length,
    "Cl" -> "132112".length,
    "Ar" -> "3112".length,
    "K" -> "1112".length,
    "Ca" -> "12".length,
    "Sc" -> "3113112221133112".length,
    "Ti" -> "11131221131112".length,
    "V" -> "13211312".length,
    "Cr" -> "31132".length,
    "Mn" -> "111311222112".length,
    "Fe" -> "13122112".length,
    "Co" -> "32112".length,
    "Ni" -> "11133112".length,
    "Cu" -> "131112".length,
    "Zn" -> "312".length,
    "Ga" -> "13221133122211332".length,
    "Ge" -> "31131122211311122113222".length,
    "As" -> "11131221131211322113322112".length,
    "Se" -> "13211321222113222112".length,
    "Br" -> "3113112211322112".length,
    "Kr" -> "11131221222112".length,
    "Rb" -> "1321122112".length,
    "Sr" -> "3112112".length,
    "Y" -> "1112133".length,
    "Zr" -> "12322211331222113112211".length,
    "Nb" -> "1113122113322113111221131221".length,
    "Mo" -> "13211322211312113211".length,
    "Tc" -> "311322113212221".length,
    "Ru" -> "132211331222113112211".length,
    "Rh" -> "311311222113111221131221".length,
    "Pd" -> "111312211312113211".length,
    "Ag" -> "132113212221".length,
    "Cd" -> "3113112211".length,
    "In" -> "11131221".length,
    "Sn" -> "13211".length,
    "Sb" -> "3112221".length,
    "Te" -> "1322113312211".length,
    "I" -> "311311222113111221".length,
    "Xe" -> "11131221131211".length,
    "Cs" -> "13211321".length,
    "Ba" -> "311311".length,
    "La" -> "11131".length,
    "Ce" -> "1321133112".length,
    "Pr" -> "31131112".length,
    "Nd" -> "111312".length,
    "Pm" -> "132".length,
    "Sm" -> "311332".length,
    "Eu" -> "1113222".length,
    "Gd" -> "13221133112".length,
    "Tb" -> "3113112221131112".length,
    "Dy" -> "111312211312".length,
    "Ho" -> "1321132".length,
    "Er" -> "311311222".length,
    "Tm" -> "11131221133112".length,
    "Yb" -> "1321131112".length,
    "Lu" -> "311312".length,
    "Hf" -> "11132".length,
    "Ta" -> "13112221133211322112211213322113".length,
    "W" -> "312211322212221121123222113".length,
    "Re" -> "111312211312113221133211322112211213322113".length,
    "Os" -> "1321132122211322212221121123222113".length,
    "Ir" -> "3113112211322112211213322113".length,
    "Pt" -> "111312212221121123222113".length,
    "Au" -> "132112211213322113".length,
    "Hg" -> "31121123222113".length,
    "Tl" -> "111213322113".length,
    "Pb" -> "123222113".length,
    "Bi" -> "3113322113".length,
    "Po" -> "1113222113".length,
    "At" -> "1322113".length,
    "Rn" -> "311311222113".length,
    "Fr" -> "1113122113".length,
    "Ra" -> "132113".length,
    "Ac" -> "3113".length,
    "Th" -> "1113".length,
    "Pa" -> "13".length,
    "U" -> "3".length)

  def sequenceLength(elements: List[String]): Int =
    elements.map { elem => elemLengths(elem) }.sum

  def lookSayElements(start_elem: String, iters: Int): Int =
    lookSayElements(List(start_elem), iters)
  def lookSayElements(elems: List[String], iters: Int): Int = {
    if (iters == 0) {
      sequenceLength(elems)
    } else {
      lookSayElements(elems.flatMap { elem => elements(elem) }, iters - 1)
    }
  }

  //  println(lookSayElements("Po", 40))
  //  println(lookSayElements("Po", 50))

  for (i <- 50 to 70) {
    val start = System.nanoTime()
    lookSayElements("Po", i)
    val end = System.nanoTime()
    println(i + "-> " + (end - start) / 1e9)
  }
}