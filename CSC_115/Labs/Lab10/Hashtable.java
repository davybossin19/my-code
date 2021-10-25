public class Hashtable{

private static final int TABLE_SZ = 7; // a prime number

	Student[] table;
	int count;  // number of Students in the table

	public Hashtable() {
		table = new Student[TABLE_SZ];
		count = 0;
	}



	/* MethodName: insertCollisions
	 * Purpose: insert (or update entry) s in this Hashtable with no collision handling strategy
	 * Parameters: Student - s
	 * Throws:  TableFullException - if inserting a new key into a full table
	 *          CollisionException - if inserting a new key into table at index that is full
	 * Returns: nothing
	 */
	// TODO: complete this function


  public void insertCollisions(Student s) throws TableFullException, CollisionException {
    int hash = s.hashCode() % TABLE_SZ;

    if (count >= TABLE_SZ && !table[hash].equals(s)) {
      throw new TableFullException();
    }
    else if (table[hash] != null && !table[hash].equals(s)){
      throw new CollisionException();
    }
    else {
      if (table[hash] == null) {
        count++;
      }
      table[hash] = s;
    }
  }

	/* MethodName: getCollisions
	 * Purpose: find Student with sid in this Hashtable with no collision handling and returns their grade
	 * Parameters: String - sid
	 * Throws:  KeyNotFoundException  - if Student with sid is not found in table
	 * Returns: int - the grade of Student with sid
	 */
	// TODO: complete this function

  public int getCollisions(String sID) throws KeyNotFoundException {
    int hash = sID.hashCode() % TABLE_SZ;

    if (table[hash] == null || !table[hash].getSID().equals(sID)) {
      throw new KeyNotFoundException();
    } else {
       return table[hash].getGrade();
    }
  }

	/* MethodName: insertLinearProbing
	 * Purpose: insert (or update entry) s in this Hashtable with Linear Probing to handle collisions
	 * Parameters: Student - s
	 * Throws: TableFullException  - if inserting a new key into a full table
	 * Returns: nothing
	 */
	// TODO: complete this function
  public void insertLinearProbing(Student s) throws TableFullException {
    int hash = s.hashCode() % TABLE_SZ;

    if (count >= TABLE_SZ && !table[hash].equals(s)) {
      throw new TableFullException();
    } else {
      if (table[hash] == null) {
        table[hash] = s;
        count++;
      } else if (table[hash].equals(s)) {
        table[hash] = s;
      } else {
        for (int i = hash; i < hash + TABLE_SZ; i++) {
          if (table[i % TABLE_SZ] == null) {
            table[i % TABLE_SZ] = s;
            count++;
            break;
          }
        }
      }
    }
  }

	/* getLinearProbing
	 * Purpose: find Student with sid in this Hashtable that uses Linear Probing and returns their grade
	 * Parameters: String - sid
	 * Throws:  KeyNotFoundException  - if Student with sid is not found in table
	 * Returns: int - the grade of Student with sid
	 */
	// TODO: complete this function
  public int getLinearProbing(String sID) throws KeyNotFoundException {
    int hash = sID.hashCode() % TABLE_SZ;

    boolean keyInTable = true;

    for (int i = hash; i < hash + TABLE_SZ; i++) {
      if (table[i % TABLE_SZ] == null) {
        throw new KeyNotFoundException();
      } else if (table[i % TABLE_SZ].getSID().equals(sID)) {
        return table[i % TABLE_SZ].getGrade();
      }
    }
    // If we have looped through entire table then we know key wont be found
    throw new KeyNotFoundException();
  }




	/*
	 * Purpose: returns the number of elements in this Hashtable
	 * Parameters: none
	 * Returns: int - the number of elements
	 */
	public int size() {
		return count;
	}

	/*
	 * Purpose: returns a String reprensentation of elements
	 *      in this Hashtable separated by newlines
	 * Parameters: none
	 * Returns: String - the representation
	 */
	public String toString() {
		String s = "";

		for(int i=0; i<TABLE_SZ; i++) {
			if (table[i] != null) {
				s  += table[i] + "\n";
			}
		}

		return s;
	}


}
