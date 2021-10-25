/* Name: David Bossin
	 SID: V00906664 */
public class A2Exercises {

	/*
	 * Purpose: Add b to the given array of books
	 * Parameters: Book[] array - the array to add the book to
	 * 			   Book b - the book to add to the array
	 * Returns: Book[] - a new array containing all of the books
	 *                   found in arr plus book b
	 */
	public static Book[] addBook(Book[] array, Book b) {
		Book[] result = new Book[array.length + 1];

		int i = 0;

		for (i = 0; i < array.length; i++) {
			result[i] = array[i];
			// System.out.println(i);
		}
		// System.out.println(i);
		result[i] = b;
		return result; // so it compiles
	}

	/*
	 * Purpose: get the sum of all the page counts from all of the books in the array
	 * Parameters: Book[] array
	 * Returns: int - the total number of pages found in all books in the array
	 */
	public static int numberOfPages(Book[] array) {
		int result = 0;
		int arrLength = array.length;

		for (int i = 0; i < arrLength; i++) {
			result += array[i].getTotalPages();
		}
		return result; // so it compiles
	}

	/*
	 * Purpose: get the number of books in the array
	 *          with a rating equal to the given rating
	 * Parameters: Book[] arr - the array of books
	 *             int rating - the rating to search for
	 * Returns: int - the number of books with the given rating
	 */
	public static int booksWithRating(Book[] arr, int rating) {
		int result = 0;

		for (int i = 0; i < arr.length; i++) {
			if (arr[i].getRating() == rating) {
				result++;
			}
		}
		return result; // so it compiles
	}

	/*
	 * Purpose: get the number of books in the array written by
	 *          an author who is older than the given author
	 * Parameters: Book[] arr - the array of books
	 *             Author auth - the author to compare with
	 * Returns: int - the number of books written by an older author
	 */
	public static int numOlderAuthors(Book[] arr, Author auth) {
		int result = 0;

		for (int i = 0; i < arr.length; i++) {
			if (arr[i].getAuthor().olderThan(auth)) {
				result++;
			}
		}
		return result; // so it compiles
	}
}
