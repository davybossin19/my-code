/* David Bossin
* Student.java
* A Student class
*/
public class Student {

	private String sID;
	private int grade;

	public Student() {
		sID = "";
		grade = -1;
	}

	public Student(String sID) {
		this.sID = sID;
		grade = -1;
	}

	public Student(String sID, int grade) {
		this.sID = sID;
		this.grade = grade;
	}

	/*
	 * Purpose: set's this Student's sID to sID parameter value
	 * Parameters: String - sID
	 * Returns: nothing
	 */
	public void setSID(String sID) {
		this.sID = sID;
	}

	/*
	 * Purpose: returns this Student's sID
	 * Parameters: none
	 * Returns: String - the sID
	 */
	public String getSID() {
		return this.sID;
	}

	public void setGrade(int grade) {
		this.grade = grade;
	}

	public int getGrade() {
		return this.grade;
	}

	/*
	 * Purpose: returns a String representation of this Student
	 *      in the form "sID:grade"
	 * Parameters: none
	 * Returns: String - the representation
	 */
	public String toString() {
		return "sID: " + this.sID + ", grade: " + this.grade;
	}

	/*
	 * Purpose: returns true if this Student's sID
	 *      equals other Student's sID
	 * Parameters: none
	 * Returns: boolean - true if equal, false otherwise
	 */
	public boolean equals(Student other) {
		return (this.sID.equals(other.sID));
	}

}
