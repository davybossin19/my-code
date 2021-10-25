/*
* HeapPriorityQueue.java
*
* An implementation of a minimum PriorityQueue using a heap.
* based on the implementation in "Data Structures and Algorithms
* in Java", by Goodrich and Tamassia
*
* This implementation will throw a Runtime, HeapEmptyException
*	if the heap is empty and removeLow is called.
*
* This implementation will throw a Runtime, HeapFullException
*	if the heap is full and insert is called.
*
*/

public class HeapPriorityQueue implements PriorityQueue {

	protected final static int DEFAULT_SIZE = 10000;

	protected Comparable[] storage;
	protected int currentSize;

	/*
	 * Constructor that initializes the array to hold DEFAULT_SIZE elements
	 */
	public HeapPriorityQueue() {
		storage = new Comparable[DEFAULT_SIZE];
		currentSize = 0;
	}

	/*
	 * Constructor that initializes the array to hold size elements
	 * Precondition: size > 0
	 */
	public HeapPriorityQueue(int size) {
		//TODO: Implement this
		storage = new Comparable[size];
		currentSize = 0;
	}

	/*
	 * The array implementation of insert MUST throw
	 * a HeapFullException if the array is full
	 */
	public void insert(Comparable element ) {
		//TODO: Implement this
		// System.out.println("start of insert------- ");
		// System.out.println("Current heap: " + toString());
		// System.out.println("currentSize: " + currentSize + ": Capacity: " + storage.length);
		if (currentSize == storage.length) {
			throw new HeapFullException();
		}

		storage[currentSize++] = element;
		// System.out.println("Heap after adding to end: " + toString());
		// System.out.println("Current size: " + currentSize);

		bubbleUp(currentSize - 1);
	}

	private void bubbleUp(int index) {
		if (index > 0) {
			// System.out.println("Res: " + storage[index] +".compareTo("+storage[index/2]+") is" +
			// storage[index].compareTo(storage[index/2]));
			if (storage[index].compareTo(storage[(index -1)/2]) < 0) {
				// System.out.println("\n");
				// System.out.println("Before swap: " + toString());
				swap(index, (index-1)/2);
				// System.out.println("After swap: " + toString());
				// System.out.println("\n");
				bubbleUp((index - 1)/2);
			}
		}
	}

	private void swap(int index1, int index2) {
		Comparable temp = storage[index1];
		storage[index1] = storage[index2];
		storage[index2] = temp;
	}

	public Comparable removeMin() {
		// System.out.println();
		// System.out.println("Start of removeMin------");
		if (isEmpty()) {
			throw new HeapEmptyException();
		}
		// System.out.println();
		// System.out.println("Heap at start of Function: " + toString());
		Comparable minValue = storage[0];


		// System.out.println("Minvalue before swap: " + storage[0] + ":" + minValue);
		storage[0] = storage[currentSize - 1];
		// System.out.println("Storage[0] after swap: " + storage[0]);
		// System.out.println("Root: " + storage[1]);
		storage[currentSize - 1] = minValue;
		currentSize--;
		// System.out.println("storage[1]: " + storage[1]);
		// System.out.println("Current size: " + size());

		bubbleDown(0);
		// System.out.println("End of removeMin()-----------------");
		// System.out.println();
		return minValue;
	}

	private void bubbleDown(int index) {
		// System.out.println();
		// System.out.println("start of bubbleDown--------");
		// System.out.println(isLeaf(index));

		if (!isLeaf(index)) {
			// System.out.println("Not leaf node");
			int minChildIndex = minChild(index);
			if (storage[index].compareTo(storage[minChildIndex]) > 0) {
				// System.out.println("Index: " + index + ", minChildIndex: " + minChildIndex);
				// System.out.println("Before Swap: " + toString());
				swap(index, minChildIndex);
				// System.out.println("After Swap: " + toString());
				bubbleDown(minChildIndex);
			}
		}
		// System.out.println("End of bubbleDown--");
		// 		System.out.println();
	}

	private int minChild(int index) {

		if (((index*2) + 1) <= currentSize - 1 && ((index*2) + 2 ) > currentSize - 1) {
			return (index * 2) + 1;
		} else if (storage[(index*2) + 1].compareTo(storage[(index * 2) + 2]) < 0) {
			return (index * 2) + 1;
		} else {
			return (index * 2) + 2;
		}
	}

	private boolean isLeaf(int index) {
		// System.out.println();
		// System.out.println("Start of isLeaf()-----------");
		return (((index * 2) + 1) > (currentSize - 1));
	}

	public boolean isEmpty() {
		return currentSize == 0;
	}

	public int size() {
		return currentSize;
	}

	public Comparable getElement(int index) {
		return storage[index];
	}


	// TODO: Add other methods here

	public String toString() {
		String s = "";
		String sep = "";
		for(int i=0;i<currentSize;i++) {
			s += sep + storage[i];
			sep = " ";
		}
		return s;
	}

}
