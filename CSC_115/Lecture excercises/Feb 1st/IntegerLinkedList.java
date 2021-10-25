public class IntegerLinkedList implements IntegerList {

	private Node head;
	private int numElements;

	public IntegerLinkedList() {
		head = null;
		numElements = 0;
	}

	public void addFront (int val) {
    Node n = new Node(val);
    n.next = head;
    head = n;
    numElements++;

	}

	public void addBack (int val) {
    Node n = new Node(val);
    if (head == null) {
      head = n;
    } else {

    Node cur = head;
    while (cur.next != null) {
      cur = cur.next;
      }
    cur.next = n;
    }
    numElements++;
	}

	public int size (){
		return numElements;
	}

	public int get (int position) {
    Node cur = head;
    for (int i = 0; i < position; i++) {
      cur = cur.next;
    }
    return cur.getValue();
  }


	/* Purpose: create a string representation of list
	 * Parameters: none
	 * Returns: String - the string representation
	 */
	public String toString() {
		String s = "List contents: ";
    Node cur = head;
    while (cur != null) {
      s += " " + cur.getValue();
      cur=cur.next;
    }
		return s;
	}
}
