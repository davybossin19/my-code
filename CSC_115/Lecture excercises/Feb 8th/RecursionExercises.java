public class RecursionExercises {

	/*
	 * Purpose: sum all values from n down to 1
	 * Parameters: (int) - n
	 * Returns: (int) - the sum
	 * Preconditions: n > 0
	 */
	public static int sum(int n) {
		// TODO: implement this method
    if (n == 1) {
      return 1;
    } else {
      return n + sum(n - 1);
    }
	}

	/*
	 * Purpose: sum all values from n^2 down to 1^2
	 * Parameters: (int) - n
	 * Returns: (int) - the sum of squares
	 * Preconditions: n > 0
	 */
	public static int sumSquares(int n) {
		// TODO: implement this method
    if (n == 1) {
      return 1;
    } else {
      return n*n + sumSquares(n - 1);
    }
	}

	/*
	 * Purpose: sum all odd values from n down to 1
	 * Parameters: (int) - n
	 * Returns: (int) - the sum of odd values
	 * Preconditions: n > 0
	 */
	public static int sumOdd(int n) {
		// TODO: implement this method
    if (n == 1) {
      return 1;
    } else if (n % 2 == 1) {
      return n + sumOdd(n - 2);
    } else {
      return sumOdd(n - 1);
    }
	}

	/*
	 * Purpose: sum all values up to i in the array
	 * Parameters: (int[]) arr - the array
	 *             (int) i - current index to consider
	 * Returns: (int) - the sum
	 * Preconditions: i < arr.length
	 */
	public static int sumArray(int[] arr, int i) {
		// TODO: implement this method
    if (arr.length == 0) {
      return 0;
    } else if (i == 0) {
      return arr[i];
    } else {
      return arr[i] + sumArray(arr, i - 1);
    }
	}

	/*
	 * Purpose: count the number of negative values found
	 *          in the array up to index i
	 * Parameters: (int[]) arr - the array
	 *             (int) i - current index to consider
	 * Returns: (int) - count of negatives values found
	 * Preconditions: i < arr.length
	 */
	public static int countNegative(int[] arr, int i) {
		// TODO: implement this method
    if (arr.length == 0) {
      return 0;
    } else if (i == 0 && arr[i] < 0) {
      return 1;
    } else if (i == 0 && arr[i] >= 0) {
      return 0;
    } else if (i > 0 && arr[i] < 0) {
      return 1 + countNegative(arr, i - 1);
    } else {
      return countNegative(arr, i - 1);
    }
	}

	/*
	 * Purpose: count the number of values in array up to
	 *          index i with a value equal to n
	 * Parameters: (int[]) arr - the array
	 *             (int) i - current index to consider
				   (int) n - value to search for
	 * Returns: (int) - count of elements equal to n
	 * Preconditions: 0 <= i < arr.length
	 */
	public static int countEqualTo(int[] arr, int i, int n) {
		// TODO: implement this method
    if (arr.length == 0) {
      return 0;
    } else if (i == 0 && arr[i] == n) {
      return 1;
    } else if (i == 0 && arr[i] != n) {
      return 0;
    } else if (i > 0 && arr[i] == n) {
      return 1 + countEqualTo(arr, i - 1, n);
    } else {
      return countEqualTo(arr, i - 1, n);
    }
	}

	/*
	 * Purpose: determine if the values in array
	 *          up to index i are all above n
	 * Parameters: (int[]) arr - the array
	 *             (int) i - current index to consider
				   (int) n - threshold elements must be greater than
	 * Returns: (boolean) - true if all values are greater than n
	 * Preconditions: 0 <= i < arr.length
	 */
	public static boolean allAbove(int[] arr, int i, int n) {
		// TODO: implement this method
    if (arr.length == 0) {
      return true;
    } else if (i == 0 && arr[i] > n) {
      return true;
    } else if (i == 0 && arr[i] <= n) {
      return false;
    } else if (arr[i] <= n) {
      return false;
    } else {
      return allAbove(arr, i - 1, n);
    }
	}
}
