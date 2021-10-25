public class ShapeList{

	private static final int DEFAULT_SIZE = 2;

	private Shape[] elements;
	private int count;

	public ShapeList() {
		// TODO: initialize the fields
    elements = new Shape[DEFAULT_SIZE];
    count = 0;

		// elements should be initialized as an empty
		// array that holds DEFAULT_SIZE shapes

	}

	/*
	 * Purpose: returns the number of elements in list
	 * Parameters: none
	 * Returns: int - the number of elements
	 */
	public int size() {
		// TODO
		return count;
	}

  public void expandAndCopy() {
    Shape[] copy = new Shape[elements.length*2];

    for (int i = 0; i < count; i++) {
      copy[i] = elements[i];
    } this.elements = copy;
  }

	/*
	 * Purpose: adds Shape s to back of this list
	 * Parameters: Shape - s
	 * Returns: nothing
	 */
	public void add(Shape s) {
		// TODo
    if (isFull()) {
      expandAndCopy();
    }
    elements[count] = s;
    count++;
	}

	/*
	 * Purpose: returns a String reprensentation of the elements
	 *      in this list separated by newlines
	 * Parameters: none
	 * Returns: String - the representation
	 */
	public String toString() {
		// TODO
    String result = "";

    for (int i = 0; i < count;i++) {
      result += elements[i] + "\n";
    }

		return result; // so it compiles
	}

	/*
	 * Purpose: removes the first element in this list
	 * Parameters: none
	 * Returns: nothing
	 */
	public void removeFront() {
    if (count > 0) {
  		for (int i = 0; i < count - 1; i++) {
        elements[i] = elements[i + 1];
      }
      count--;
    }
	}

  public boolean isFull() {
    if (elements.length == count) {
      return true;
    } else {
      return false;
    }
  }



}
