public class ComparableTester {

	public static void main(String[] args) {
		// Integer num1 = new Integer(2);
		// Integer num2 = new Integer(4);
		// Integer num3 = new Integer(8);
		//
		// String s1 = "comparing";
		// String s2 = "different";
		// String s3 = "strings";

		Student s1 = new Student("v00123456", 4, 7.3);
		Student s2 = new Student("v00123457", 3, 8);

		/*
		1. Use the compareTo method to compare the
		   Integers and Strings initialized above.
		*/
		if (s1.compareTo(s2) < 0) {
			System.out.println(s1 + " comes first");
		} else if (s1.compareTo(s2) == 0) {
			System.out.println("They are ordered eqaually");
		} else {
			System.out.println(s2);
		}

		/*
		2. Add implementation to the Student class
		   so that it implements the Comparable interface
		*/

		/*
		3. Create at least two Student objects and
		   use the compareTo method in the Student
		   class to compare them.
		*/
	}

}
