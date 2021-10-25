public class Rectangle implements Shape {

	private int length; //length units along x axis
	private int width;  //width units along y axis
	private Point position; // position is the (x,y) coordinates of lower left corner of the rectangle

	public Rectangle() {
		this.length = 0;
		this.width = 0;
		this.position = new Point();
	}

	public Rectangle(int length, int width) {
		this.length = length;
		this.width = width;
		this.position = new Point();
	}

	public Rectangle(int length, int width, Point position) {
		this.length = length;
		this.width = width;
		this.position = position;
	}

	public double area() {
		double totalArea;
		totalArea = this.length * this.width;
		return totalArea;
	}

	public double perimeter() {
		double totalPerimeter;
		totalPerimeter = (this.length * 2) + (this.width * 2);
		return totalPerimeter;
	}

	public boolean contains(Point p) {
		int ptX = p.getX();
		int ptY = p.getY();

		int positionX = position.getX();
		int positionY = position.getY();

		int xDistance = ptX-positionX;
		int yDistance = ptY-positionY;

		boolean contains = false;

		if ((xDistance <= this.length && yDistance <= this.width) &&
		(ptX >= positionX && ptY >= positionY)) {
			contains = true;
		} return contains;
	}

	public String toString() {
		return "Rectangle of dimensions: " + length + " by " + width +
		" at Point: " + position;

	}

}
