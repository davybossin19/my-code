public class A4Exercises {

	/*
	 * Purpose: add valToAdd to all elements in the given array
	 * Parameters: int[] array - the array to modify
	 *             int valToAdd - the value to modify items by
	 * Returns: void - nothing
	 */
	public static void addToAll(int[] array, int valToAdd) {
		if (array.length > 0) {
		addToAllRecursive(array, valToAdd, array.length-1);
		}
	}

	private static void addToAllRecursive(int[] array, int valToAdd, int i) {
		if (i == 0) {
			array[i] += valToAdd;
		} else {
			array[i] += valToAdd;
			addToAllRecursive(array, valToAdd, i - 1);
		}




	}

	/*
	 * Purpose: determines whether the given array contains toFind
	 * Parameters: int[] array - the array to search
	 *             int toFind - the value to search for
	 * Returns: boolean - true if found, false otherwise
	 */
	public static boolean arrayContains(int[] array, int toFind) {
		return arrayContainsRecursive(array, toFind, array.length-1);
	}

	private static boolean arrayContainsRecursive(int[] array, int toFind, int i) {
		if (i == -1) {
			return false;
		} else if (array[i] == toFind) {
			return true;
		} else {
			return arrayContainsRecursive(array, toFind, i - 1);
		}
	}

	/*
	 * Purpose: gets the number of times there are two of the same element in a row
	 * Parameters: int[] array - the array to search
	 * Returns: int - the number of occurrences where two adjacent elements are the same
	 */
	public static int sameInARow(int[] array) {
		return sameInARowRecursive(array, -1, array.length-1);
	}

	private static int sameInARowRecursive(int[] array, int prev, int i) {
		if (i <= 0) {
			return 0;
		} else if (array[i] == array[i - 1]) {
			return 1 + sameInARowRecursive(array, prev, i - 1);
		} else {
			return sameInARowRecursive(array, prev, i - 1);
		}
	}
}
