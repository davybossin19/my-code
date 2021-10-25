public class Dog extends Mammal {
  private String name;

  public Dog() {
    super("Dog", "woof", 2);
    name = "George";
    System.out.println("dog contructor (0 parameters)");
  }

  public Dog(String name) {
    super("Dog", "woof", 2);
    this.name = name;
    System.out.println("dog constructor (1 parameters)");
  }

  public Dog(String species, String sound, String name) {
    super(species, sound, 2);
    this.name = name;
    System.out.println("dog constructor (3 parameters)");
  }

  public void speak() {
    System.out.println("My name is " + name);
  }

  public void feed() {
    System.out.println("I need food twice a day");
  }
}
