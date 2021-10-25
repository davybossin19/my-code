public class IntegerStack {
	
	private static final int DEFAULT_CAPACITY = 10;
	
	private int[] data;
	private int top;
	
	public IntegerStack() {
		data = new int[DEFAULT_CAPACITY];
		top = 0; 
	}
	
	/*
	 * Purpose: insert an item onto the top of the stack
	 * Parameters: (int) - the item to insert 
	 * Returns: Nothing
	 */
	public void push(int v) {
		// handle case if stack is full
		if (top < data.length) {
			data[top] = v;
			top++;
		}
	}
	
	/*
	 * Purpose: removes and returns the top item from the stack
	 * Parameters: None
	 * Returns: (int) - the data value of the element removed
	 *                  -1 is the stack is empty
	 */
	public int pop() {
		if (isEmpty()) {
			return -1;
		}
		int val = data[top-1];
		top--;
		return val;
	}
	
	/*
	 * Purpose: determines whether the stack is empty
	 * Parameters: None
	 * Returns: (boolean) - true if the stack is empty, false otherwise
	 */
	public boolean isEmpty() {
		return top == 0;
	}
	
	/*
	 * Purpose: Accesses the top item on the stack
	 * Parameters: None
	 * Returns: (int) - the data value of the top element
	 * 					-1 if the stack is empty
	 */
	public int top() { // also often named peek()
		if (isEmpty()) {
			return -1;
		}
		return data[top-1];
	}
	


	
	// Following two methods made for ease of testing
	
	public IntegerStack(int[] elements) {
		data = new int[elements.length];
		top = 0;
		for (int i = elements.length-1; i >= 0; i--) {
			push(elements[i]);
		}
	}
	
	public String toString() {
		String result = "{";
		for (int i = top-1; i >= 0; i--) {
			if (i == 0) {
				result += data[i];
			} else {
				result += data[i] + ", ";
			}
		}
		result += "}";
		return result;
	}

}