// Song.java

public class Song {
	private String artist;
	private String title;
	private int duration; // in seconds
	// could add duration, year, writer, etc..

	public Song() {
		artist = "no artist";
		title = "default";
		duration = 0;
	}
	
	public Song(String a, String t) {
		artist = a;
		title = t;
		duration = 0;
	}
	
	public Song(String a, String t, int d) {
		artist = a;
		title = t;
		duration = d;
	}
	
	public String getArtist() {
		return artist;
	}
	
	public String getTitle() {
		return title;
	}
	
	public void setTitle(String newTitle) {
		title = newTitle;
	}
	
	public void addTime(int timeToAdd) {
		duration += timeToAdd;
	}

	public String toString() {
		return "Song: " + title + " by " + artist + " (" + duration + ")";
	}
	
	public boolean equals(Song other) {
		if (this.artist.equals(other.getArtist()) && this.title.equals(other.getTitle())) {
			return true;
		} else {
			return false;
		}
	}
   
}