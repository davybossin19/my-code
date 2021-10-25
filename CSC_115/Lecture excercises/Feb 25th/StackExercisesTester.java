public class StackExercisesTester {

	private static int testPassCount = 0;
	private static int testCount = 0;

	public static void main(String[] args) {
		testSum();
		testDoubleAll();
		testContains();
		testGetMax();
		// testContainsAll();

		System.out.println("PASSED " + testPassCount + " / " + testCount + " tests");
	}


	public static void testSum() {
		System.out.println("\ntesting sum");
		IntegerStack s0 = new IntegerStack();
		int[] s1Elements = {7, 2, 4};
		IntegerStack s1 = new IntegerStack(s1Elements);
		int[] s2Elements = {8, 2, 5, 7, 2, 1, 4};
		IntegerStack s2 = new IntegerStack(s2Elements);

		int result = 0;
		int expected = 0;
		String contents = "";

		result = sum(s0);
		displayResults(result==expected, "sum empty stack");

		result = sum(s1);
		expected = 7 + 2 + 4;
		contents = s1.toString();
		displayResults(result==expected, "sum s1");
		displayResults(contents.equals(s1.toString()), "s1 contents unchanged");

		result = sum(s2);
		expected = 8 + 2 + 5 + 7 + 2 + 1 + 4;
		contents = s2.toString();
		displayResults(result==expected, "sum s2");
		displayResults(contents.equals(s2.toString()), "s2 contents unchanged");
	}

	/*
	 * Purpose: get the sum of all elements in the stack
	 * Parameters: IntegerStack s - the stack of integers
	 * Returns: int - the sum of all elements
	 */
	public static int sum(IntegerStack s) {
		if (s.isEmpty()) {
			return 0;
		}

		int top = s.pop();
		int sumOfRest = sum(s);

		s.push(top);
		return top + sumOfRest;
	}



	public static void testDoubleAll() {
		System.out.println("\ntesting doubleAll");
		IntegerStack s0 = new IntegerStack();
		int[] s1Elements = {7, 2, 4};
		IntegerStack s1 = new IntegerStack(s1Elements);
		int[] s2Elements = {8, 2, 5, 7, 2, 1, 4};
		IntegerStack s2 = new IntegerStack(s2Elements);

		String expected = "{}";

		doubleAll(s0);
		displayResults(expected.equals(s0.toString()), "doubleAll empty stack");

		doubleAll(s1);
		expected = "{14, 4, 8}";
		displayResults(expected.equals(s1.toString()), "doubleAll s1 stack");

		doubleAll(s2);
		expected = "{16, 4, 10, 14, 4, 2, 8}";
		displayResults(expected.equals(s2.toString()), "doubleAll s2 stack");
	}

	/*
	 * Purpose: double all elements in the given stack
	 * Parameters: IntegerStack s - the stack of integers
	 * Returns: void - nothing
	 */
	public static void doubleAll(IntegerStack s) {
		if (s.isEmpty()) {
			return;
		}

		int top = s.pop();
		doubleAll(s);

		s.push(top*2);
	}



	public static void testContains() {
		System.out.println("\ntesting contains");
		IntegerStack s0 = new IntegerStack();
		int[] s1Elements = {6, 2, 5, 7, 2, 8, 4};
		IntegerStack s1 = new IntegerStack(s1Elements);

		boolean found = false;
		String contents = "";

		found = contains(s0, 7);
		displayResults(!found, "contains 7 in empty stack");

		found = contains(s1, 6);
		contents = s1.toString();
		displayResults(found, "contains 6 in s1");
		displayResults(contents.equals(s1.toString()), "s1 contents unchanged");

		found = contains(s1, 3);
		contents = s1.toString();
		displayResults(!found, "contains 3 in s1");
		displayResults(contents.equals(s1.toString()), "s1 contents unchanged");

		found = contains(s1, 7);
		contents = s1.toString();
		displayResults(found, "contains 7 in s1");
		displayResults(contents.equals(s1.toString()), "s1 contents unchanged");

		found = contains(s1, 4);
		contents = s1.toString();
		displayResults(found, "contains 4 in s1");
		displayResults(contents.equals(s1.toString()), "s1 contents unchanged");
	}


	/*
	 * Purpose: determine whether the stack contains value toFind
	 * Parameters: IntegerStack s - the stack of integers
	 *             int toFind - the value to search for
	 * Returns: boolean - true if found, false otherwise
	 */
	public static boolean contains(IntegerStack s, int toFind) {
		boolean found = false;

		if (s.isEmpty()) {
			return found;
		}

		int top = s.pop();
		if (top == toFind) {
			found = true;
		} else {
			found = contains(s, toFind);
		}

		s.push(top);
		return found;
	}



	public static void testGetMax() {
		System.out.println("\ntesting getMax");
		IntegerStack s0 = new IntegerStack();
		int[] s1Elements = {7, 2, 4};
		IntegerStack s1 = new IntegerStack(s1Elements);
		int[] s2Elements = {7, 2, 9};
		IntegerStack s2 = new IntegerStack(s2Elements);
		int[] s3Elements = {6, 2, 5, 7, 2, 8, 4};
		IntegerStack s3 = new IntegerStack(s3Elements);

		int result = 0;
		int expected = 0;
		String contents = "";

		result = getMax(s0);
		displayResults(result==expected, "getMax empty stack");

		result = getMax(s1);
		expected = 7;
		contents = s1.toString();
		displayResults(result==expected, "getMax s1");
		displayResults(contents.equals(s1.toString()), "s1 contents unchanged");

		result = getMax(s2);
		expected = 9;
		contents = s2.toString();
		displayResults(result==expected, "getMax s2");
		displayResults(contents.equals(s2.toString()), "s2 contents unchanged");

		result = getMax(s3);
		expected = 8;
		contents = s3.toString();
		displayResults(result==expected, "getMax s3");
		displayResults(contents.equals(s3.toString()), "s3 contents unchanged");
	}

	/*
	 * Purpose: get the maximum value in the given stack
	 * Parameters: IntegerStack s - the stack of integers
	 * Returns: int - the maximum value, 0 if empty
	 * Preconditions: all elements in stack have a value > 0
	 */
	public static int getMax(IntegerStack s) {
		int max = 0;

		if (s.isEmpty()) {
			return 0;
		}

		int top = s.pop();
		int maxOfRest = getMax(s);

		if (top > maxOfRest) {
			return top;
		} else {
			max = maxOfRest;
		}

		s.push(top);
		return max;

	}


	public static void testContainsAll() {
		System.out.println("\ntesting containsAll");
		IntegerStack s1, s2;
		int[] elements1 = {2, 1, 3};
		int[] elements2 = {1};
		int[] elements3 = {4};
		int[] elements4 = {3, 1, 2};
		int[] elements5 = {2, 1, 3, 7, 9, 1};
		int[] elements6 = {8, 5, 4, 2, 1, 3};
		int[] elements7 = {2, 5, 4, 1, 9, 6, 3};
		int[] elements8 = {2, 2, 2, 1, 1, 3};
		int[] elements9 = {2, 1, 1};
		int[] elements0 = {2, 1, 1, 3};


		boolean foundAll = false;

		s1 = new IntegerStack();			// {}
		s2 = new IntegerStack();			// {}
		foundAll = containsAll(s1, s2);
		displayResults(foundAll, "containsAll({}, {})");

		s2 = new IntegerStack(elements1);	// {2, 1, 3}
		foundAll = containsAll(s1, s2);
		displayResults(foundAll, "containsAll({}, {2,1,3})");

		foundAll = containsAll(s2, s1);
		displayResults(!foundAll, "containsAll({2,1,3}, {})");

		s1 = new IntegerStack(elements2);	// {1}
		s2 = new IntegerStack(elements1);	// {2, 1, 3}
		foundAll = containsAll(s1, s2);
		displayResults(foundAll, "containsAll({1}, {2,1,3})");

		s1 = new IntegerStack(elements3);	// {4}
		s2 = new IntegerStack(elements1);	// {2, 1, 3}
		foundAll = containsAll(s1, s2);
		displayResults(!foundAll, "containsAll({4}, {2,1,3})");

		s1 = new IntegerStack(elements4); // {3, 1, 2}
		s2 = new IntegerStack(elements1); // {2, 1, 3}
		foundAll = containsAll(s1, s2);
		displayResults(!foundAll, "containsAll({3,1,2}, {2,1,3})");

		s1 = new IntegerStack(elements1); // {2, 1, 3}
		s2 = new IntegerStack(elements5); // {2, 1, 3, 7, 9, 1}
		foundAll = containsAll(s1, s2);
		displayResults(foundAll, "containsAll({2,1,3}, {2,1,3,7,9,1})");

		s1 = new IntegerStack(elements1); // {2, 1, 3}
		s2 = new IntegerStack(elements6); // {8, 5, 4, 2, 1, 3}
		foundAll = containsAll(s1, s2);
		displayResults(foundAll, "containsAll({2,1,3}, {8,5,4,2,1,3})");

		s1 = new IntegerStack(elements1); // {2, 1, 3}
		s2 = new IntegerStack(elements7); // {2, 5, 4, 1, 9, 6, 3}
		foundAll = containsAll(s1, s2);
		displayResults(foundAll, "containsAll({2,1,3}, {2,5,4,1,9,6,3})");

		s1 = new IntegerStack(elements1); // {2, 1, 3}
		s2 = new IntegerStack(elements8); // {2, 2, 2, 1, 1, 3}
		foundAll = containsAll(s1, s2);
		displayResults(foundAll, "containsAll({2,1,3}, {2,2,2,1,1,3})");

		s1 = new IntegerStack(elements1); // {2, 1, 3}
		s2 = new IntegerStack(elements9); // {2, 1, 1}
		foundAll = containsAll(s1, s2);
		displayResults(!foundAll, "containsAll({2,1,3}, {2,1,1})");

		s1 = new IntegerStack(elements1); // {2, 1, 3}
		s2 = new IntegerStack(elements0); // {2, 1, 1, 3}
		foundAll = containsAll(s1, s2);
		displayResults(foundAll, "containsAll({2,1,3}, {2,1,1,3})");

		s1 = new IntegerStack(elements1); // {2, 1, 3}
		s2 = new IntegerStack(elements0); // {2, 1, 1, 3}
		foundAll = containsAll(s2, s1);
		displayResults(!foundAll, "containsAll({2,1,1,3}, {2,1,3})");
	}


	/*
	 * Purpose: determines whether all of the elements in s1
	 *          are found in s2, in the same order
	 * Parameters: IntegerStack s1, s2
	 * Returns: boolean - true if all values in s1 are found in s2
	 *                    in the same order, false otherwise
	 */
	public static boolean containsAll(IntegerStack s1, IntegerStack s2) {
		return false;
	}

	public static void displayResults (boolean passed, String testName) {
		/* There is some magic going on here getting the line number
		* Borrowed from:
		* http://blog.taragana.com/index.php/archive/core-java-how-to-get-java-source-code-line-number-file-name-in-code/
		*/

		testCount++;
		if (passed) {
			System.out.println ("Passed test: " + testName);
			testPassCount++;
		} else {
			System.out.println ("Failed test: " + testName + " at line "
					+ Thread.currentThread().getStackTrace()[2].getLineNumber());
		}
    }

}
