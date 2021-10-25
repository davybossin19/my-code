// SongTester.java
public class SongTester {
	private static int testCount = 0;
	private static int testPassCount = 0;

	public static void main (String[] args) {

		Song s1 = new Song("Champions", "Queen", 327);
		Song s2 = new Song("Halo", "Beyonce", 151);
		Song s3 = new Song("Africa", "Toto", 358);
		s1.setArtist("James Blunt");

		Song mySong = null;
		mySong = s1;

		mySong.setTitle("Rockstars");



		/* Q5. Create an array of Songs to store our songs */
		Song [] mySongs = new Song[5];
		mySongs[0] = s1;
		mySongs[1] = s2;
		mySongs[2] = s3;
		mySongs[3] = new Song("Thunderstruck", "ACDC", 532);
		mySongs[4] = new Song();


		/* Q6a. Print out all of the songs in the array */

		for (int i = 0; i < mySongs.length; i++) {
			System.out.println(mySongs[i]);
		}

		/* Q6b. Write and test a method called getPlaylistLength that takes an
		array of Songs and returns the total length of all songs in the array */


		/* Q6c. Write and test a method called containsArtist that takes an
		array of Songs and the name of an artist and determines whether there
		is a song with the given artist name found in the array. */

		// System.out.println("PASSED " +testPassCount+ " / " +testCount+" tests");
}
	public static void testGetPlaylistLength() {
		System.out.println("\nTesting getPlaylistLength");

		Song s1 = new Song("Champions", "Queen", 327);
		Song s2 = new Song("Halo", "Beyonce", 151);
		Song s3 = new Song("Africa", "Toto", 358);
		Song s4 = new Song("Thunderstruck", "ACDC", 532);

		Song[] arr0 = {};
		Song[] arr1 = {s1, s2};
		Song[] arr2 = {s1, s2, s3, s4};

		int result = 0;
		int expected = 0;

		result = getPlaylistLength(arr0);
		expected = 0;
		displayResults("playlistLength for arr0", result == expected);

		result = getPlaylistLength(arr1);
		expected = 327 + 151;
		displayResults("playlistLength for arr1", result == expected);

		result = getPlaylistLength(arr2);
		expected = 327 + 151 + 358 + 532;
		displayResults("playlistLength for arr2", result == expected);
	}

	public static void testAddTime() {
		System.out.println("Testing the addTime method in the song class");

		Song s1 = new Song("Champions", "Queen", 327);
		Song s2 = new Song("Halo", "Beyonce");
	}

	public static int getPlaylistLength(Song[] array) {
		int result = 0;
	}

	public static void displayResults (String testName, boolean passed) {
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
