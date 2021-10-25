public class Couch extends Furniture {
  private int numSeats;

  public Couch(String name, String itemID, String material, double price, int numSeats) {
    super(name, itemID, material, price);
    this.numSeats = numSeats;
  }

  public String toString() {
    String s = super.toString();
    s += "this couch seats " + numSeats + " people";
    s += "\n";
    return s;
  }
}
