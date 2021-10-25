public class IntegerArrayList implements IntegerList {

	private static final int INITIAL_SIZE = 5;

	private int[] data;
	private int numElements;

	public IntegerArrayList() {
		data = new int[INITIAL_SIZE];
		numElements = 0;
	}

	/*
	 * expandAndCopy
	 * Purpose: create a new array twice as big and
	 *          copy all elements from arr into it
	 * Parameters: int[] arr - the array to copy
	 * Return: none
	 */
	public void expandAndCopy(int[] arr) {
		int[] bigger = new int[arr.length*2];
		for (int i=0; i < arr.length; i++) {
			bigger[i] = arr[i];
		}
		data = bigger;
	}

	public void addFront(int val) {
		// will inserting this item go outside the array bounds?
		if (numElements >= data.length) {
			//create a bigger array, and copy values over
			expandAndCopy(data);
		}
		
		// assume now there is space in the array...
		// but we need to shuffle every item to the right
		// one index so we can insert into index 0
		for (int i = numElements; i>0; i--) {
			data[i] = data[i-1];
		}
		data[0] = val;
		numElements++;
	}
	

		
	public void addBack(int val) {
		// will inserting this item go outside the array bounds?
		if (numElements >= data.length) {
			//create a bigger array, and copy values over
			expandAndCopy(data);
		}
		data[numElements] = val;
		numElements++;
	}

	
	public int size() {
		return numElements;
	}
	
	public int get(int position) {
		return data[position];
	}

	/* toString
	 * Purpose: create a string representation of list
	 * Parameters: none
	 * Returns: String - the string representation of the list
	 */
	public String toString() {
		String s = "List contents:";

		for(int i=0; i<numElements; i++) {
			s += " " + data[i];
		}

		return s;
	}

}
