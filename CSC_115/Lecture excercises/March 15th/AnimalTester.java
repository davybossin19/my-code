public class AnimalTester{

	public static void main(String args[]) {

		Animal a1 = new Animal();
		Animal a2 = new Animal("lion", "roar");
		a1.speak();
		a2.speak();
		System.out.println("a1: " + a1);
		System.out.println("a2: " + a2);

		System.out.println("\n");

		Mammal m1 = new Mammal();
		Animal m2 = new Mammal();
		m1.speak();
		m2.speak();

		Mammal m3 = new Mammal("pig", "oink", 4);
		Mammal m4 = new Mammal("fox", "fox noise", 7);
		m3.speak();
		m4.speak();

		System.out.println(m3);
		System.out.println(m4);

		System.out.println("\n");


		Animal d1 = new Dog();
		Animal d2 = new Dog("Marley");
		Animal d3 = new Dog("Pug", "Yip yip", "Pudgey");

		d1.speak();
		d2.speak();
		d3.speak();

		((Dog) d1).feed();





	}
}
