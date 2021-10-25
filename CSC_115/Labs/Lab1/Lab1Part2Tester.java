/*
 * Lab1Part2Tester.java
 *
 * A tester for the methods in your Student class
 *
 */
public class Lab1Part2Tester {

    public static void main(String[] args) {

		Student s1 = new Student();
		Student s2 = new Student("V00123456");

		// 1.
		// What do you expected to output?
		// What part of the class file defines this?
		System.out.println(s1);
		System.out.println(s2);

		Student s3 = new Student("V00998877");

		// 2.
		// Add a grade field to the student class, and update the following:
		//  - initialize the grade value to -1 in the two constructors
		//  - create a third construct or that takes an sID and grade as parameters
		//  - uncomment the following two lines and see if -1 is output

		System.out.println("s1's grade: "+s1.getGrade());
		System.out.println("s2's grade: "+s2.getGrade());

		// 3.
		// Update s1's grade so that it is 91 and s2's so that it is 70
		// The second set of print statements should now output different grades

		// ** UPDATE GRADES HERE **
		s1.setGrade(91);
		s2.setGrade(70);
		System.out.println("\ns1's new grade: "+s1.getGrade());
		System.out.println("s2's new grade: "+s2.getGrade());

		// 4.
		// Uncomment the following 4 lines:
		// The constructor should work if you completed 2. correctly

		Student s4 = new Student("V00123456", 84);
		s1.setSID("V00998877");
		System.out.println("\ns4's sID: "+s4.getSID());
		System.out.println("s4's grade: "+s4.getGrade());



		// 5.
		// Update the toString method so that the following lines
		// output both the student's sID and grade
		// For example, System.out.println(s4) should output:
		// sID: v00123456, grade: 84

		System.out.println(s1 + "  expected: sID: V00998877, grade: 91"); // what should be output?
		System.out.println(s4);



		// 6.
		// Which students would be considered equal?
		// How does the Student class code determine whether two students are equal?


		if (s1.equals(s2)) {
			System.out.println(s1 + " and " + s2 + " are equal");
		} else {
			System.out.println(s1 + " and " + s2 + " are not equal");
		}

		if (s1.equals(s3)) {
			System.out.println(s1 + " and " + s3 + " are equal");
		} else {
			System.out.println(s1 + " and " + s3 + " are not equal");
		}

		if (s2.equals(s3)) {
			System.out.println(s2 + " and " + s3 + " are equal");
		} else {
			System.out.println(s2 + " and " + s3 + " are not equal");
		}

		if (s2.equals(s4)) {
			System.out.println(s2 + " and " + s4 + " are equal");
		} else {
			System.out.println(s2 + " and " + s4 + " are not equal");
		}

	}
}
