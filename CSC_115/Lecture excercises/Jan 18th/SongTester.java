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
    Song s2 = new Song("Toto", "Africa");
    Song s3 = new Song("Toto", "Africa");




		s1.setTitle("Jingle Bells");
    System.out.println("s1: " + s1.getTitle() + " - " + s1.getArtist());

    System.out.println(s3);




		/* 5a. update statements where necessary from 3b and 3c */

		/* 6a. call constructor with args, then print fields */
    System.out.println(s2.equals(s3));




		/* 6b. call alternative constructor, then print fields */





		/* 6c. try to print one of the songs
		   ie. pass your Song variable to System.out.println() */


		/* 7a. recompile and run your program - what changes in 6c. */
	}
}
