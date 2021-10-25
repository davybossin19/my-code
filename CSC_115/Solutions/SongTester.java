// SongTester.java
//
// We will write code here to test our implementation of Song.java
//
// We have put this code in a different file to help you understand 
// the difference between static and non-static.  In the real world,
// this style of test code might be included in the Song.java file.

public class SongTester {
    
	public static void main (String[] args) {
		Song s1 = new Song();
		Song s2 = new Song("Beyonce", "Halo", 208);
		Song s3 = new Song("Toto", "Africa", 354);
		
		// System.out.println("s1: " + s1.getTitle() + " - " + s1.getArtist());
		// System.out.println("s2: " + s2.getTitle() + " - " + s2.getArtist());
		// System.out.println("s3: " + s3.getTitle() + " - " + s3.getArtist());

		s1.setTitle("Jingle Bells");
		// System.out.println("s1: " + s1.getTitle() + " - " + s1.getArtist());

		/* 6c. try to print one of the songs
		   ie. pass your Song variable to System.out.println() */
		System.out.println(s2);
		System.out.println(s3);
		
		s2.addTime(10);
		System.out.println(s2); // Halo by Beyonce should now be 218 seconds
		
		Song s4 = new Song("Toto", "Africa", 428);
		Song s5 = new Song("Toto", "Africa", 104);
		Song s6 = new Song("Toto", "Africa", 104);
		
		if (s3.equals(s4)) {
			System.out.println("songs are equal");
		} else {
			System.out.println("songs are not equal");
		}
		


		/* 7a. recompile and run your program - what changes in 6c. */
	}
}