public class IntegerLinkedList {

	private IntegerNode	head;
	private int		    count;


	public IntegerLinkedList() {
		head = null;
		count = 0;
	}

	/*
	 * size
	 * Purpose: returns the size of this IntegerList
	 * Parameters: none
	 * Returns: int - the size
	 */
	public int size() {
		return count;
	}

	/*
	 * addFront
	 * Purpose: adds element with i to the front of this Integerlist
	 * Parameters: int - i
	 * Returns: nothing
	 */
	public void addFront (int i) {
		IntegerNode n = new IntegerNode(i, head);

		head = n;

		count++;

	}


	/*
	 * toString
	 * Purpose: returns a String representation of this IntegerList
	 * Parameters: none
	 * Returns: String - the String representation
	 */
	public String toString() {
		String s = "";
		IntegerNode tmp = head;

		while (tmp!=null) {
			s += tmp.getElement();
			if(tmp.next!=null)
				s += " ";
			tmp = tmp.next;
		}

		return s;
	}

	/*
	 * addOne
	 * Purpose: adds 1 to every element in this IntegerList
	 * Parameters: none
	 * Returns: nothing
	 */
	public void addOne() {
		IntegerNode tmp = head;

		while (tmp!=null) {
			int valPlusOne = tmp.getElement() + 1;
			tmp.setElement(valPlusOne);
			tmp = tmp.next;
		}
	}

	/*
	 * addOneRecursive
	 * Purpose: recursively adds 1 to every element in this IntegerList
	 * Parameters: none
	 * Returns: nothing
	 */
	public void addOneRecursive() {
		addOneRecursiveHelper(head);
	}

	/*
	 * addOneRecursiveHelper
	 * Purpose: recursively adds 1 to IntegerNode n and every element following n
	 * Parameters: IntegerNode - n
	 * Returns: nothing
	 */
	private void addOneRecursiveHelper(IntegerNode n) {
		if (n==null) {
			return;
		} else {

			// get data in current node and add 1 to it
			int valPlusOne = n.getElement() + 1;
			// set element in current node to valPlusOne
			n.setElement(valPlusOne);

			// add one to the elements in the  REST of the list
			addOneRecursiveHelper(n.next);
		}
	}

	/*
	 * doubleAll
	 * Purpose: recursively doubles every element in this IntegerList
	 * Parameters: none
	 * Returns: nothing
	 */
	// ToDo: implement and test this method
	public void doubleAll() {
		doubleAllHelper(head);
	}

	private void doubleAllHelper(IntegerNode cur) {
		if (cur == null) {
			return;
		} else {
			int valDoubled = cur.getElement() * 2;
			cur.setElement(valDoubled);
			doubleAllHelper(cur.next);
		}
	}



	/*
	 * doubleOddValues
	 * Purpose: recursively doubles every odd valued element in this IntegerList
	 *  By "odd valued element" we mean the Node's element is an odd number
	 *  NOT that it is at an odd position in the list
	 * Parameters: none
	 * Returns: nothing
	 */
	// ToDo: implement and test this method
	public void doubleOddValues() {
		doubleOddValuesHelper(head);
	}

	private void doubleOddValuesHelper(IntegerNode cur) {
		if (cur == null) {
			return;
		} else if (cur.getElement() % 2 == 1 || cur.getElement() % 2 == -1 ) {
			int valDoubled = cur.getElement() * 2;
			cur.setElement(valDoubled);
			doubleOddValuesHelper(cur.next);
		} else {
			doubleOddValuesHelper(cur.next);
		}
	}




	/*
	 * sum
	 * Purpose: recursively sums every element in this IntegerList
	 * Parameters: none
	 * Returns: int - the sum
	 */
	public int sum() {
		return sum(head);
	}


	/*
	 * sum
	 * Purpose: recursively sums element in IntegerNode n and every element following n
	 * Parameters: IntegerNode - n
	 * Returns: int - the sum
	 */
	private int sum(IntegerNode n) {
		if (n==null) {
			return 0;
		} else {
			int first = n.getElement();
			int sumRest = sum(n.next);

			return first + sumRest;
		}
	}

	/*
	 * product
	 * Purpose: recursively computes the product of every element in this IntegerList
	 *  Note: the product of an empty list is 1
	 * Parameters: none
	 * Returns: int - the product
	 */
	// ToDo: implement and test this method

	public int product() {
		return productHelper(head, 1);
	}

	private int productHelper(IntegerNode cur, int product) {
		if (cur == null) {
			return  product * 1;
		} else {
			product *= cur.getElement();
			return productHelper(cur.next, product);
		}
	}





	/*
	 * doubleOddPositionValues
	 * Purpose: recursively doubles every element at an odd postion in this IntegerList
	 *          the first  element in this list is at position 0 (is not odd)
	 *          the second element in this list is at position 1 (is odd)
	 *          the third  element in this list is at position 2 (is not odd)
	 *          ...
	 * Parameters: none
	 * Returns: nothing
	 */
	public void doubleOddPositionValues() {
		doubleOddPositionValues(head, 0);
	}

	/*
	 * doubleOddPositionValues
	 * Purpose: recursively doubles element in IntegerNode n if n is at odd position
	 *          and every element after n at odd positions
	 * Parameters: IntegerNode - n, int - position
	 * Returns: nothing
	 */
	private void doubleOddPositionValues(IntegerNode n, int position) {
		if (n==null) {
			return;
		} else {
			if (position % 2 != 0) {
				int doubleVal = n.getElement() * 2;
				n.setElement(doubleVal);
			}
			doubleOddPositionValues(n.next, position+1);
		}
	}


	/*
	 * isSorted
	 * Purpose: recursively determines whether every element in this IntegerList
	 *      is sorted in ascending order
	 *      {1, 2, 2, 5} is sorted in ascending order
	 *      {3, 2, 2, 5} is not sorted in ascending order
	 * Parameters: none
	 * Returns: boolean - true if sorted, false otherwise
	 * Note: an empty list is considered sorted
	 */
	// ToDo: implement and test this method

	public boolean isSorted() {
		return isSortedHelper(head, null);
	}

	private boolean isSortedHelper(IntegerNode cur, IntegerNode prev) {
		if (cur == null) {
			return true;
		} else if (prev != null && prev.getElement() > cur.getElement()) {
			return false;
		}	else {
			return isSortedHelper(cur.next, cur);
		}
	}






	/*
	 * allNegative
	 * Purpose: recursively determines whether all elements in this IntegerList are negative
	 * Parameters: none
	 * Returns: boolean - true if all negative, false otherwise
	 * Note: an empty list is considered to have all negative values (as there are no
	 *       non-negative values found in the list)
	 */
	// ToDo: implement and test this method

	public boolean allNegative() {
		 return allNegativeHelper(head);
	}

	private boolean allNegativeHelper(IntegerNode cur) {
		if (cur == null) {
			return true;
		} else if (-1 < cur.getElement()) {
			return false;
		} else {
			return allNegativeHelper(cur.next);
		}
	}



}
