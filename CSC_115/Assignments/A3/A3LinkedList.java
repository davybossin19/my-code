// Name: David Bossin
// Student number: v00906664

public class A3LinkedList implements A3List {
	private A3Node head;
	private A3Node tail;
	private int length;

	public A3LinkedList() {
		head = null;
		tail = null;
		length = 0;
	}

	public void addFront(String s) {
		A3Node n = new A3Node(s);

		if (isEmpty()) {
			head = n;
			tail = n;
		} else {
		head.prev = n;
		n.next = head;
		head = n;
		}
		length++;
	}

	public void addBack(String s) {
		A3Node n = new A3Node(s);
		if (isEmpty()) {
			head = n;
			tail = n;
		} else {
		n.prev = tail;
		tail.next = n;
		tail = n;
		}
		length++;
	}


	public int size() {
		return length;
	}

	public boolean isEmpty() {
		return length==0;
	}

	public void removeFront() {
		if (length == 1) {
			head = null;
			tail = null;
			length--;

		} else if (length > 0) {
				A3Node temp = head.next;
				head = temp;
				head.prev = null;
				length--;
			}
	}

	public void removeBack() {
		if (length == 1) {
			head = null;
			tail = null;
			length--;
		} else if (length > 0) {
				A3Node temp = tail.prev;
				tail = temp;
				tail.next = null;
				length--;
			}
	}


	public void rotate(int n) {
		if (length > 1) {
			for (int i = 0; i < n; i++) {
				A3Node temp = tail.prev;
				tail.next = head;
				head.prev = tail;
				head = tail;
				tail = temp;
				tail.next = null;
				head.prev = null;
			}
		}


	}

	public A3Node getHead() {
		return head;
	}

	public void setTail(A3Node tail) {
		this.tail = tail;
	}

	public void interleave(A3LinkedList other) {
		A3Node cur1 = head;
		A3Node cur2 = other.getHead();
		A3Node temp1 = cur1.getNext();
		A3Node temp2 = cur2.getNext();


			for (int i = 0; i < length; i++) {
				temp1 = cur1.getNext();
				temp2 = cur2.getNext();
				cur1.setNext(temp2);
				cur2.setNext(temp1);

				if (cur1.getNext() != null) {
					temp1.setPrev(cur2);
					temp2.setPrev(cur1);
				} if (length % 2 == 0 && cur1.getNext() == null) {
					tail = cur2;
					other.setTail(cur1);
				}
					cur1 = temp1;
					cur2 = temp2;
		}
	}

	/* Purpose: return a string representation of the list
	 *          when traversed from front to back
	 * Parameters: none
	 * Returns: nothing
	 */
	public String frontToBack() {
		String result = "{";
		A3Node cur = head;
		while (cur != null) {
			result += cur.getData();
			cur = cur.next;
		}
		result += "}";
		return result;
	}

	/* Purpose: return a string representation of the list
	 *          when traversed from back to front
	 * Parameters: none
	 * Returns: nothing
	 */
	public String backToFront() {
		String result = "{";
		A3Node cur = tail;
		while (cur != null) {
			result += cur.getData();
			cur = cur.prev;
		}
		result += "}";
		return result;
	}
}
