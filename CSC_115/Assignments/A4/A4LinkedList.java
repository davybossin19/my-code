public class A4LinkedList implements A4List {

	// Completed for you, should not be changed
	private StudentNode head;
	private StudentNode tail;
	private int numElements;

	// Completed for you, should not be changed
	public A4LinkedList() {
		head = null;
		tail = null;
		numElements = 0;
	}

	// Completed for you, should not be changed
	public int size(){
		return numElements;
	}

	// Completed for you, should not be changed
	public boolean isEmpty() {
		return head == null;
	}

	// Completed for you, should not be changed
	public void insert(Student s) {
		StudentNode n = new StudentNode(s);
		if (head == null) {
			head = n;
		} else {
			tail.next = n;
		}
		tail = n;
		numElements++;
	}

	/*
	 * Purpose: create a string representation of list
	 * Parameters: none
	 * Returns: String - the string representation
	 *
	 * Completed for you, should not be changed
	 */
	public String toString() {
		return "{" + toStringRecursive(head) + "}";
	}

	public String toStringRecursive(StudentNode cur) {
		if (cur == null) {
			return "";
		} else if (cur.next == null) {
			return cur.getData().toString() + toStringRecursive(cur.next);
		} else {
			return cur.getData().toString() + ", " + toStringRecursive(cur.next);
		}
	}

	public boolean inProgram(String program) {
		return inProgramRecursive(head, program);
	}

	private boolean inProgramRecursive(StudentNode cur, String program) {
    if (cur == null) {
      return false;
    } else if (cur.getData().getProgram() == program) {
      return true;
    } else {
      return inProgramRecursive(cur.next, program);
    }
	}

	public Student getStudent(String sID) {
		return getStudentRecursive(head, sID);
	}

	private Student getStudentRecursive(StudentNode cur, String sID) {
    if (cur == null) {
      return null;
    } else if (cur.getData().getSID() == sID) {
      return cur.getData();
    } else {
      return getStudentRecursive(cur.next, sID);
    }
	}

	public double averageGPA() {
		if (size() == 0) {
			return 0.0;
		} else {
			return sumGPARecursive(head)/size();
		}
	}

	private double sumGPARecursive(StudentNode cur) {
		if (cur == null) {
      return 0;
    } else {
      return cur.getData().getGPA() + sumGPARecursive(cur.next);
    }
	}

	public double programAverage(String program) {
		// call a recursive helper  method!
    if (getCountInProgram(program, head) == 0) {
      return 0.0;
    } else {
      return getCumulativeGPARecursive(head, program)/getCountInProgram(program, head);
    }
  }

  private double getCumulativeGPARecursive(StudentNode cur, String program) {
    if (cur == null) {
      return 0;
    } else if (cur.getData().getProgram() == program) {
      return cur.getData().getGPA() +
      getCumulativeGPARecursive(cur.next, program);
    } else {
      return getCumulativeGPARecursive(cur.next, program);
    }
  }

  private int getCountInProgram(String program, StudentNode cur) {
    if (cur == null) {
      return 0;
    } else if (cur.getData().getProgram() == program) {
      return 1 + getCountInProgram(program, cur.next);
    } else {
      return getCountInProgram(program, cur.next);
    }
  }

	public Student highestGPA() {
    if (size() == 0) {
      return null;
    } else {
      return getHighestGPARecursive(head, head);
    }
	}

  private Student getHighestGPARecursive(StudentNode curHighestGPA, StudentNode cur) {
    if (cur == null) {
      return curHighestGPA.getData();
    } else if (curHighestGPA.getData().getGPA() < cur.getData().getGPA()) {
      curHighestGPA = cur;
    }
    return getHighestGPARecursive(curHighestGPA, cur.next);
  }


}
