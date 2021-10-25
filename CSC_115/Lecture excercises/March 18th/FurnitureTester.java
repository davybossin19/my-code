public class FurnitureTester {

	public static void main(String[] args) {
		Furniture f1 = new Furniture("vase", "x1z4322", "ceramic", 40.00);
		Furniture f2 = new Furniture("rocking chair", "ab998c", "wood", 179.99);

		System.out.println(f1);
		System.out.println(f1.getName() + " sale price: $" + f1.salePrice() +"\n");
		System.out.println(f2);

		Couch c1 = new Couch("sofa", "s11fd8", "Leather", 699.9, 4);
		Couch c2 = new Couch("futon", "lz2789h", "cotton", 199.87, 2);

		System.out.println(c1);
		System.out.println(c2);
		/* 1) Create a subclass of the Furniture class for a certain type of furniture */

		/* 2) Create another subclass that includes a has-a relationship */
		Shape s1 = new Circle(5);
		Shape s2 = new Rectangle(10, 20);
		Table t1 = new Table("circle", "90feud", "oak", 780.00, s1);
		Table t2 = new Table("patio", "89feud", "glass", 100.00, s2);

		Furniture[] storeItems = {f1, c1, t1, t2, f2, c2, t2};
		for (int i = 0; i < storeItems.length; i++) {
			System.out.println(storeItems[i]);
		}

		/* 3) Create a furniture array the contains different types of furniture */

	}
}
