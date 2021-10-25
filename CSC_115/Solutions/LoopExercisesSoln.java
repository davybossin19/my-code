class LoopExercisesSoln {
    
	public static void main (String[] args) {
		// Q1. Complete the implementation of getHighest
		testGetHighest();

		// Q2. Write and test the method factorial
		testFactorial();

		// Q2. Write and test the method sumToN
		testSumToN();
	}

	public static void testGetHighest() {
		int result = 0;
		result = getHighest(1, 2, 3);
		System.out.println("getHighest(1,2,3) result: "+result);
		result = getHighest(5, 4, 3);
		System.out.println("getHighest(5,4,3) result: "+result);
		result = getHighest(0, 2, 1);
		System.out.println("getHighest(0,2,1) result: "+result);
		result = getHighest(1, 1, 1);
		System.out.println("getHighest(1,1,1) result: "+result);
	}

	/*
	* Purpose: return the maximum of the three given values
	* Parameters: int, int, int 
	* Returns: int - integer with the highest value 
	*/
	public static int getHighest(int a, int b, int c) {
		if (a >= b && a >= c) {
			return a;
		} else if (b >= a && b >= c) {
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
		System.out.println("\ncalling factorial(0)");
		System.out.println("result: " + result);
		System.out.println("expected: " + expected);
		
		result = factorial(1);
		expected = 1;
		System.out.println("\ncalling factorial(1)");
		System.out.println("result: " + result);
		System.out.println("expected: " + expected);

		result = factorial(3);
		expected = 3*2*1;
		System.out.println("\ncalling factorial(3)");
		System.out.println("result: " + result);
		System.out.println("expected: " + expected);
		
		result = factorial(5);
		expected = 5*4*3*2*1;
		System.out.println("\ncalling factorial(5)");
		System.out.println("result: " + result);
		System.out.println("expected: " + expected);	
	}

	/*
	* Purpose: Calculate n factorial (n!)
	* Parameters: int n
	* Precondition: n >= 0
	* Returns: int - n factorial
	*/
	public static int factorial(int n) {
		int result = 1;

		for (int i = n; i > 1; i--) {
			result *= i;
		}

		return result;
	}

	public static void testSumToN() {
		int result = 0;
		int expected = 0;

		result = sumToN(1);
		expected = 1;
		System.out.println("\ncalling sumToN(1)");
		System.out.println("result: " + result);
		System.out.println("expected: " + expected);

		result = sumToN(4);
		expected = 4 + 3 + 2 + 1;
		System.out.println("\ncalling sumToN(4)");
		System.out.println("result: " + result);
		System.out.println("expected: " + expected);
		
		result = sumToN(7);
		expected = 7 + 6 + 5 + 4 + 3 + 2 + 1;
		System.out.println("\ncalling sumToN(7)");
		System.out.println("result: " + result);
		System.out.println("expected: " + expected);
	}

	/*
	* Purpose: sum the numbers from 1 to n
	* Parameters: int - the value n
	* Precondition: n > 0
	* Returns: int - the sum 
	*/
	public static int sumToN(int n) {
		int sum = 0;
		for (int i = 1; i <= n; i++) {
			sum += i;
		}
		return sum;
	}

}
