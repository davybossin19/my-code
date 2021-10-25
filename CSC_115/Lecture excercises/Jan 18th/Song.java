// Song.java

public class Song {
  private String artist;
  private String title;

  public Song() {
    System.out.println("First constructor called");
    artist = "no artist";
    title = "unknown";
  }

  public Song(String a, String t) {
    System.out.println("Second constructor called");
    artist = a;
    title = t;
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

  public String toString() {
    return "Song: " + title + " by " + artist;
  }

  public boolean equals(Song other) {
    if (this.title.equals(other.getTitle()) && this.artist.equals(other.getArtist())) {
      return true;
    }
    else {
      return false;
    }
  }
}
