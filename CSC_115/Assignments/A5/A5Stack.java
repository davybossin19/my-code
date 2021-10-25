//David Bossin
//V00906664


public class A5Stack<T> implements Stack<T> {

	private Node<T> head;
	private int count;

	public A5Stack() {
		// TODO: implement this
		head = null;
	}

	public void push(T v) {
		// TODO: implement this
		Node<T> n = new Node<T>(v);
		n.setNext(head);
		head = n;
		count++;

	}

	public T pop() throws EmptyStackException {
		// TODO: implement this
		if (isEmpty()) {
			throw new EmptyStackException();
		}
		T val = head.getData();
		head = head.getNext();
		count--;

		return val; // so it compiles
	}

	public T top() throws EmptyStackException {
		// TODO: implement this
		if (isEmpty()) {
			throw new EmptyStackException();
		}
		return head.getData(); // so it compiles
	}

	public void popAll() {
		// TODO: implement this
		head = null;
	}

	public boolean isEmpty() {
		// TODO: implement this

		return head == null; // so it compiles
	}

}
