public class NodeTester {

	public static void main (String[] args) {

		System.out.println("Part 1:");
		/* 1a. create a new blank (value 0) node n1 */
		Node n1 = new Node();
		Node n2 = new Node(9);

		/* 1b. create a new node n2 with a value of 9 */


		/* 1c. print the values in n1 and n2 */
		System.out.println("n1 value: " + n1.getValue());
		System.out.println("n2 value: " + n2.getValue());


		System.out.println("\nPart 2:");
		/* 2a. connect n1 to n2 such that n2 is before n1 */
		n2.setNext(n1);



		/* 2b. print the value in n1 and n2 without using the variable n1 */
		System.out.println("n1 value: " + n2.getNext().getValue());
		System.out.println("n2 value: " + n2.getValue());



		System.out.println("\nPart 3:");
		/* 3a. create a new node n3 with a value of 20 */
		Node n3 = new Node(20);


		/* 3b. assign our n1 variable so that it also references
		       the newly created node with data value 20 */
		n1 = n3;


		/* 3c. Can you still print the values in all 3 nodes? */
		System.out.println("print out 0: " + n2.getNext().getValue());
		System.out.println("print out 9: " + n2.getValue());
		System.out.println("print out 20: " + n1.getValue());
		System.out.println("print out 20: " + n3.getValue());




		System.out.println("\nPart 4:");
		/* 4a. connect n3 to the other two nodes such that n3 is
			   in between the other two */
		n3.next = n2.next;
		n2.next = n3;



		/* 4b. print all 3 values using only the n2 variable.
			   That is, you cannot use the variables n1 or n3 */
		System.out.println("n2: " + n2.getValue());
		System.out.println("n3: " + n2.getNext().getValue());
		System.out.println("n1: " + n2.next.next.getValue());



		System.out.println("\nPart 5:");
		/* 5. Create a method that accepts a node as a parameter
			  and prints out the value of the given node as well
			  as the values of all nodes that follow it. */
				printList(n2);

	}
	public static void printList(Node head) {
		Node cur = head;
		while (cur != null) {
			System.out.println("value: " + cur.getValue());
			cur = cur.next;
		}
	}
}
