public class LinkedListTester {

	public static void main (String[] args) {

		/* The following tester code was used to test IntegerArrayList
		   change it so that it tests the IntegerLinkedList we implement */

		IntegerList myList = new IntegerLinkedList();
		IntegerList myList2 = new IntegerLinkedList();

		System.out.println("List is empty:");
		System.out.println(myList);
		System.out.println();

		myList.addBack(10);
		myList.addBack(12);
		myList.addBack(4);
		myList.addBack(6);
		myList.addBack(7);
		System.out.println("List should contain: 10 12 4 6 7");
		System.out.println(myList);
		System.out.println();

		System.out.println("Value at index 3 should be 6:");
		System.out.println("Value at index 3 returned: "+ myList.get(3));
		System.out.println("Value at index 0 should be 10:");
		System.out.println("Value at index 0 returned: "+ myList.get(0));
		System.out.println();

		myList.addFront(15);
		myList.addFront(71);
		myList.addBack(17);

		System.out.println("List should contain: 71 15 10 12 4 6 7 17");
		System.out.println(myList);
		System.out.println();

		System.out.println("size should be 8. Size returned: " + myList.size());
		System.out.println();

		//adding to new empty list starting at front
		myList2.addFront(11);
		myList2.addFront(14);
		myList2.addBack(3);
		myList2.addBack(13);

		System.out.println("List should contain: 14 11 3 13");
		System.out.println(myList2);
		System.out.println("size should be 4. Size returned: " + myList2.size());
	}
}
