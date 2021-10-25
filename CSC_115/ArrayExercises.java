public class ArrayExercises {
	private static int testPassCount = 0;
	private static int testCount = 0;

	public static void main (String[] args) {

		// Q1. Complete the arrayReview Questions
		arrayReview ();

		// Q2. Complete the implementation of ArraysEqual, which
		// determines if two arrays have the same elements in the same order.

		// testArraysEqual();


		// Q3. Write and test a method that takes an array of integers,
		// and doubles all the values in the array

		// testDouble();


		// Q4. Write and test a method that given an array of integers,
		//  returns the sum of all the odd numbers in the array

		//System.out.println("Passed " + testPassCount + "/" + testCount + " tests");

	}

	public static void arrayReview () {

		// Q1a. What is the output of the following:
		 int[] array1 = null;
		 System.out.println("array1: " + array1);

		// Q1b. What is the output of the following:
		//int[] array1[1] = 5;
		//System.out.println("array1[1]: " + array1[1]);

		// Q1c. What is the output of the following:
		int[] array2 = {4, 5, 6};
		System.out.println("array2: " + array2);
		System.out.println("array2[1]: " + array2[1]);

		// Q1d. What is the output of the following:
		double[] array3 = new double[10];
		System.out.println("array3[10]: " + array3[0]);
		System.out.println("array3[10]: " + array3[10]);

	}

	public static void testArraysEqual() {
		int[] asc1 = {1, 2, 3, 4};
		int[] asc2 = {1, 2, 3, 4, 5};
		int[] des1 = {4, 3, 2, 1};
		int[] des2 = {4, 3, 2, 1};
		boolean same = arraysEqual(asc1, asc2);
		// What should the result be?

		same = arraysEqual(asc1, des1);
		// What should the result be?

		same = arraysEqual(des1, des2);
		// What should the result be?
	}

	/*
	 * Purpose: Determines whether two arrays are equal
	 * Parameters: int[] a, int[] b - the two arrays
	 * Returns: boolean - true if arrays are the size length with
	 *                    the same values at each position
	 */
	public static boolean arraysEqual(int[] a, int[] b) {
		return false; // so it compiles
	}


	public static void testDouble() {
		int[] a1 = {7, 1, 3, 4};
		int[] a1x2 = {14, 2, 6, 8};

		doubleAll(a1);
		// How do we test if the method works?
	}

	/*
	 * Purpose: Doubles the values of all elements in given array
	 * Parameters: int[] arr - the array to modify
	 * Returns: void - nothing
	 */
	public static void doubleAll(int[] arr) {

	}

}
