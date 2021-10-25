public class Junk{
  public static void main(String[] args) {
    Point p25 = new Point(2,5);
		Point p48 = new Point(4,8);
    Shape r00 = new Rectangle();
		Shape c25 = new Circle(9, p25);

    ShapeList array = new ShapeList();

    array.add(r00);
    array.add(c25);

    // for (int i = 0; i < array.size(); i++) {
    System.out.println(array);
    // }

  }
}
