public class Mammal extends Animal {

  private int gestationPeriod; // time in months

  public Mammal() {
    // calls default constructor of parent class
    gestationPeriod = 10;
    System.out.println("Mammal constructor (0 parameters)");
  }

  public Mammal(int gestationPeriod) {
    this.gestationPeriod = gestationPeriod;
    System.out.println("Mammal contructor (1 parameters)");
  }

  public Mammal(String species, String sound, int gestationPeriod) {
    super(species, sound);
    this.gestationPeriod = gestationPeriod;
    System.out.println("Mammal contructor (3 parameters)");
  }

  public String toString() {
    String s = super.toString();
    s += ":" + gestationPeriod;
    return s;
  }

}
