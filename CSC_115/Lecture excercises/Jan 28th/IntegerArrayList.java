public class IntegerArrayList implements IntegerList {

	private static final int INITIAL_SIZE = 10;

	private int[] data;
	private int numElements;

	public IntegerArrayList() {
		data = new int[INITIAL_SIZE];
		numElements = 0;
	}

	public void expandAndCopy() {
		int[] bigger = new int[data.length*2];

		for (int i = l i < numElements; i++) {
			bigger[i] = data[i];
		}
		this.data = bigger;
	}

	public void addFront(int val) {
		// check if there is room
		if (isFull()) {
			expandAndCopy();
		}
		// shuffle all items back one
		// to make room for the new value
		for (int i = numElements; i > 0; i--) {
			data[i] = data[i - 1];
		}
		data[0] = val;
		numElements++;
	}

	public void addBack(int val) {
		if (isFull()) {
			expandAndCopy();
		}
		data[numElements] = val;
		numElements++;
	}

	public void insertAt(int position, int val) {
		for (int i = numElements, i < position, i--) {
			data[i] = data[i-1];
		}

	}

	public boolean isFull() {
		if (data.length() == numElements) {
			return true;
		} else {
			return false;
		}
	}

	public int size() {
		return numElements;
	}

	public int get(int position) {
		return data[position];
	}

	/* toString
	 * Purpose: create a string representation of list
	 * Parameters: nothing
	 * Returns: (String) the string representation of the list
	 */
	public String toString() {
		String s = "List contents:";

		for(int i=0; i<numElements; i++) {
			s += " " + data[i];
		}

		return s;
	}

}
