class LoopExercises {

	public static void main (String[] args) {

		// Q1. Complete the implementation of getHighest
		testGetHighest();

		// Q2. Write and test the method factorial
		testFactorial();

		// Q3. Write and test the method sumToN
		testSumToN();

	}

	public static void testGetHighest() {
		int result = 0;
		int expected = 0;
		result = getHighest(1, 2, 3);
		expected = 3;
		System.out.println("Called get highest (1,2,3)");
		System.out.println("Expected result: " + expected);
		System.out.println("Returned result: " + result);

		// What should the result be?

		result = getHighest(5, 4, 3);
		expected = 5;
		System.out.println("Called get highest (5,4,3)");
		System.out.println("Expected result: " + expected);
		System.out.println("Returned result: " + result);		// What should the result be?

		result = getHighest(0, 2, 1);
		expected = 2;
		System.out.println("Called get highest (0,2,1)");
		System.out.println("Expected result: " + expected);
		System.out.println("Returned result: " + result);
		// What should the result be?

		result = getHighest(1, 1, 1);
		expected = 1;
		System.out.println("Called get highest (1,1,1)");
		System.out.println("Expected result: " + expected);
		System.out.println("Returned result: " + result);
		// What should the result be?
	}

	/*
	 * Purpose: return the maximum of the three given values
	 * Parameters: int, int, int
	 * Returns: int - integer with the highest value
	 */
	public static int getHighest(int a, int b, int c) {
		if (a >= b && a >= c) {
			return a;
		} else if (b >= a && b >=c) {
			return b;
		} else {
			return c;
		}
	}



	public static void testFactorial() {
		int result = 0;
		int expected = 0;

		result = factorial(0);
		expected = 1;
		System.out.println("\nCalled factorial(0)");
		System.out.println("Expected result: " + expected);
		System.out.println("Returned result: " + result);

		result = factorial(1);
		expected = 1;
		System.out.println("\nCalled factorial(1)");
		System.out.println("Expected result: " + expected);
		System.out.println("Returned result: " + result);

		result = factorial(2);
		expected = 2;
		System.out.println("\nCalled factorial(2)");
		System.out.println("Expected result: " + expected);
		System.out.println("Returned result: " + result);

		result = factorial(3);
		expected = 6;
		System.out.println("\nCalled factorial(3)");
		System.out.println("Expected result: " + expected);
		System.out.println("Returned result: " + result);


	}

	/*
	 * Purpose: Calculate n factorial (n!)
	 * Parameters: int n
	 * Precondition: n >= 0
	 * Returns: int - n factorial
	 */

	// Write the factorial method here

	public static int factorial(int n) {
		int result = 1;

		for (int i = n; i >= 1; i--) {
			result *= i;
		}
		return result;
	}




	public static void testSumToN() {
		int result = 0;
		int expected = 0;

		result = sumToN(0);
		expected = 0;
		System.out.println("\nCalled sumToN(0)");
		System.out.println("Expected result: " + expected);
		System.out.println("Returned result: " + result);

		result = sumToN(1);
		expected = 1;
		System.out.println("\nCalled sumToN(1)");
		System.out.println("Expected result: " + expected);
		System.out.println("Returned result: " + result);

		result = sumToN(2);
		expected = 3;
		System.out.println("\nCalled sumToN(2)");
		System.out.println("Expected result: " + expected);
		System.out.println("Returned result: " + result);

		result = sumToN(3);
		expected = 6;
		System.out.println("\nCalled sumToN(3)");
		System.out.println("Expected result: " + expected);
		System.out.println("Returned result: " + result);
		// Write tests here
	}

	/*
	 * Purpose: sum the numbers from 1 to n
	 * Parameters: int - the value n
	 * Precondition: n > 0
	 * Returns: int - the sum
	 */

	// Write the sumToN method here
	public static int sumToN(int n) {
		int result = 0;
		for (int i = 1; i <= n; i++) {
			result += i;
		}
		return result;
	}
}
