public class IntegerStack {

	private static final int CAPACITY = 10;

	private int[] data;
	private int top;

	public IntegerStack() {
		data = new int[CAPACITY];
		top = 0;
	}

	/*
	 * Purpose: insert an item onto the top of the stack
	 * Parameters: (int) - the item to insert
	 * Returns: Nothing
	 */
	public void push(int v) {
		// TODO: implement this
		if (top < CAPACITY) {
			data[top] = v;
			top++;
		}
	}

	/*
	 * Purpose: removes and returns the top item from the stack
	 * Parameters: None
	 * Returns: (int) - the data value of the element removed
	 */
	public int pop() {
		// TODO: implement this
		if (isEmpty() == false) {
			int val = top();
			top--;
			return val;
		} else {
			return 0;
		}
	}

	/*
	 * Purpose: determines whether the stack is empty
	 * Parameters: None
	 * Returns: (boolean) - true if the stack is empty, false otherwise
	 */
	public boolean isEmpty() {
		// TODO: implement this
		return top == 0; // so it compiles
	}

	/*
	 * Purpose: Accesses the top item on the stack
	 * Parameters: None
	 * Returns: (int) - the data value of the top element
	 */
	public int top() {
		// TODO: implement this
		if (isEmpty == true) {
			return -1;
		}
		return data[top - 1]; // so it compiles
	}

}
