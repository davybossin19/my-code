/*
 * A3Tester
 *
 * A class to test the methods required for Assignment 3
 *
 */
public class A3Tester {

	private static int testPassCount = 0;
	private static int testCount = 0;

    public static void main(String[] args) {

		// Uncomment each method one at a time,
		// and implement the method in A3LinkedList.java
		// until all tests pass. It is strongly
		// recommended that you add additional tests
		// to ensure the correctness of your implementation.

		testAddFront();
		testAddBack();
		testSizeAndIsEmpty();
		testRemoveFront();
		testRemoveBack();
		testRotate();
		testInterleave();

		System.out.println("Passed " + testPassCount + "/" + testCount + " tests");
    }


	public static void testAddFront() {
		String result = "";
		A3LinkedList list1 = new A3LinkedList();

    System.out.println("Testing addFront()-----------------------------------");
		result = list1.frontToBack();
		displayResults(result.equals("{}"), "testAddFront");

		list1.addFront("A");
		result = list1.frontToBack();
		displayResults(result.equals("{A}"), "testAddFront");

		list1.addFront("V");
		list1.addFront("A");
		list1.addFront("J");
		result = list1.frontToBack();
		displayResults(result.equals("{JAVA}"), "testAddFront");
		result = list1.backToFront();
		displayResults(result.equals("{AVAJ}"), "testAddFront");
    System.out.println();
	}

	public static void testAddBack() {
		String result = "";
		A3LinkedList list1 = new A3LinkedList();

    System.out.println("Testing addBack()------------------------------------");
		result = list1.frontToBack();
		displayResults(result.equals("{}"), "testAddBack");

		list1.addBack("F");
		result = list1.frontToBack();
		displayResults(result.equals("{F}"), "testAddBack");

		list1.addBack("U");
		list1.addBack("N");
		result = list1.frontToBack();
		displayResults(result.equals("{FUN}"), "testAddBack");
		result = list1.backToFront();
		displayResults(result.equals("{NUF}"), "testAddBack");
    System.out.println();

	}

	public static void testSizeAndIsEmpty() {
		int result = 0;
		A3LinkedList list1 = new A3LinkedList();

    System.out.println("Testing Size and isEmpty()---------------------------");

		result = list1.size();
		displayResults(result==0, "testSizeAndIsEmpty");
		displayResults(list1.isEmpty()==true, "testSizeAndIsEmpty");

		list1.addFront("C");
		list1.addFront("S");
		list1.addFront("C");
		result = list1.size();
		displayResults(result==3, "testSizeAndIsEmpty");
		displayResults(list1.isEmpty()==false, "testSizeAndIsEmpty");

		list1.addBack("115");
		result = list1.size();
		displayResults(result==4, "testSizeAndIsEmpty");
    System.out.println();


	}

	public static void testRemoveFront() {
		String result = "";
		int int_result = 0;
		A3LinkedList list1 = new A3LinkedList();

		System.out.println("Testing removeFront()--------------------------------");

		list1.addBack("P");
		list1.addBack("I");
		list1.addBack("N");
		list1.addBack("K");
		result = list1.frontToBack();
		displayResults(result.equals("{PINK}"), "testRemoveFront");

		list1.removeFront();
		result = list1.frontToBack();
		displayResults(result.equals("{INK}"), "testRemoveFront");
		result = list1.backToFront();
		displayResults(result.equals("{KNI}"), "testRemoveFront");
		int_result = list1.size();
		displayResults(int_result == 3, "testRemoveFront by size");
    displayResults(list1.isEmpty() == false, "testRemoveFront by isEmpty");

		list1.removeFront();
		result = list1.frontToBack();
		displayResults(result.equals("{NK}"), "testRemoveFront");
		result = list1.backToFront();
		displayResults(result.equals("{KN}"), "testRemoveFront");
		int_result = list1.size();
		displayResults(int_result == 2, "testRemoveFront by size");
    displayResults(list1.isEmpty() == false, "testRemoveFront by isEmpty");

		list1.removeFront();
		result = list1.frontToBack();
		displayResults(result.equals("{K}"), "testRemoveFront");
		result = list1.backToFront();
		displayResults(result.equals("{K}"), "testRemoveFront");
		int_result = list1.size();
		displayResults(int_result == 1, "testRemoveFront by size");
    displayResults(list1.isEmpty() == false, "testRemoveFront by isEmpty");

		list1.removeFront();
		result = list1.frontToBack();
		displayResults(result.equals("{}"), "testRemoveFront");
		result = list1.backToFront();
		displayResults(result.equals("{}"), "testRemoveFront");
		int_result = list1.size();
		displayResults(int_result == 0, "testRemoveFront by size");
    displayResults(list1.isEmpty() == true, "testRemoveFront by isEmpty");
		System.out.println();


		/* Write additional tests here to ensure all of your pointers
		   have been updated correctly.

		   You should also ensure that your size and isEmpty
		   methods work with removal as well as addition */

	}

	public static void testRemoveBack() {
		// Write all of your own tests here
    String result = "";
		int int_result = 0;
		A3LinkedList list1 = new A3LinkedList();

		System.out.println("Testing removeBack()---------------------------------");


    list1.addBack("P");
		list1.addBack("I");
		list1.addBack("N");
		list1.addBack("K");
		result = list1.frontToBack();
		displayResults(result.equals("{PINK}"), "testRemoveBack");

		list1.removeBack();
		result = list1.frontToBack();
		displayResults(result.equals("{PIN}"), "testRemoveBack");
		result = list1.backToFront();
		displayResults(result.equals("{NIP}"), "testRemoveBack");
		int_result = list1.size();
		displayResults(int_result == 3, "testRemoveBack by size");
    displayResults(list1.isEmpty() == false, "testRemoveBack by isEmpty");

		list1.removeBack();
		result = list1.frontToBack();
		displayResults(result.equals("{PI}"), "testRemoveBack");
		result = list1.backToFront();
		displayResults(result.equals("{IP}"), "testRemoveBack");
		int_result = list1.size();
		displayResults(int_result == 2, "testRemoveBack by size");
    displayResults(list1.isEmpty() == false, "testRemoveBack by isEmpty");

		list1.removeBack();
		result = list1.frontToBack();
		displayResults(result.equals("{P}"), "testRemoveBack");
		result = list1.backToFront();
		displayResults(result.equals("{P}"), "testRemoveBack");
		int_result = list1.size();
		displayResults(int_result == 1, "testRemoveBack by size");
    displayResults(list1.isEmpty() == false, "testRemoveBack by isEmpty");

		list1.removeBack();
		result = list1.frontToBack();
		displayResults(result.equals("{}"), "testRemoveBack");
		result = list1.backToFront();
		displayResults(result.equals("{}"), "testRemoveBack");
		int_result = list1.size();
		displayResults(int_result == 0, "testRemoveBack by size");
    displayResults(list1.isEmpty() == true, "testRemoveBack by isEmpty");
		System.out.println();


	}

	public static void testRotate() {
		String result = "";
		int int_result = 0;
		A3LinkedList list1 = new A3LinkedList();

		System.out.println("Testing rotate()-------------------------------------");


		list1.addBack("A");
		list1.addBack("B");
		list1.addBack("C");
		list1.addBack("D");
		list1.addBack("E");
		list1.addBack("F");
		list1.addBack("G");
		result = list1.frontToBack();
		displayResults(result.equals("{ABCDEFG}"), "testRotate");

		list1.rotate(1);
		result = list1.frontToBack();
		displayResults(result.equals("{GABCDEF}"), "testRotate");
		result = list1.backToFront();
		displayResults(result.equals("{FEDCBAG}"), "testRotate");
		int_result = list1.size();
		displayResults(int_result == 7, "testRotate");
		displayResults(list1.isEmpty() == false, "testRotate");

		list1.rotate(3);
		result = list1.frontToBack();
		displayResults(result.equals("{DEFGABC}"), "testRotate");
		result = list1.backToFront();
		displayResults(result.equals("{CBAGFED}"), "testRotate");
		int_result = list1.size();
		displayResults(int_result == 7, "testRotate");
		displayResults(list1.isEmpty() == false, "testRotate");
		System.out.println();


		/* Write additional tests here to ensure all of your pointers
		   have been updated correctly. */

	}

	public static void testInterleave() {
		A3LinkedList list1 = new A3LinkedList();
		A3LinkedList list2 = new A3LinkedList();
		A3LinkedList list3 = new A3LinkedList();
		A3LinkedList list4 = new A3LinkedList();
		A3LinkedList list5 = new A3LinkedList();
		A3LinkedList list6 = new A3LinkedList();
		A3LinkedList list7 = new A3LinkedList();
		A3LinkedList list8 = new A3LinkedList();

		String result1 = "";
		String result2 = "";

		System.out.println("Testing Interleave()---------------------------------");

// Testing list1 and lis2
		list1.addBack("A");
		list1.addBack("B");
		list1.addBack("C");
		list1.addBack("D");
		list1.addBack("E");
		list1.addBack("F");
		list1.addBack("G");
		result1 = list1.frontToBack();
		displayResults(result1.equals("{ABCDEFG}"), "testInterleave");

		list2.addBack("L");
		list2.addBack("M");
		list2.addBack("N");
		list2.addBack("O");
		list2.addBack("P");
		list2.addBack("Q");
		list2.addBack("R");
		result2 = list2.frontToBack();
		displayResults(result2.equals("{LMNOPQR}"), "testInterleave");

		list1.interleave(list2);
		result1 = list1.frontToBack();
		result2 = list2.frontToBack();
		displayResults(result1.equals("{AMCOEQG}"), "testInterleave");
		displayResults(result2.equals("{LBNDPFR}"), "testInterleave");

		result1 = list1.backToFront();
		result2 = list2.backToFront();
		displayResults(result1.equals("{GQEOCMA}"), "testInterleave");
		displayResults(result2.equals("{RFPDNBL}"), "testInterleave");

// Testing list3 and list4
		list3.addBack("A");
		list3.addBack("B");
		list3.addBack("C");
		list3.addBack("D");
		list3.addBack("E");
		list3.addBack("F");
		list3.addBack("G");
		list3.addBack("H");

		result1 = list3.frontToBack();
		displayResults(result1.equals("{ABCDEFGH}"), "testInterleave");

		list4.addBack("L");
		list4.addBack("M");
		list4.addBack("N");
		list4.addBack("O");
		list4.addBack("P");
		list4.addBack("Q");
		list4.addBack("R");
		list4.addBack("S");

		result2 = list4.frontToBack();
		displayResults(result2.equals("{LMNOPQRS}"), "testInterleave");

		list3.interleave(list4);
		result1 = list3.frontToBack();
		result2 = list4.frontToBack();
		displayResults(result1.equals("{AMCOEQGS}"), "testInterleave");
		displayResults(result2.equals("{LBNDPFRH}"), "testInterleave");

		result1 = list3.backToFront();
		result2 = list4.backToFront();
		displayResults(result1.equals("{SGQEOCMA}"), "testInterleave");
		displayResults(result2.equals("{HRFPDNBL}"), "testInterleave");

		//Testing list5 and list6
		list5.addBack("A");


		result1 = list5.frontToBack();
		displayResults(result1.equals("{A}"), "testInterleave");

		list6.addBack("L");


		result2 = list6.frontToBack();
		displayResults(result2.equals("{L}"), "testInterleave");

		list5.interleave(list6);
		result1 = list5.frontToBack();
		result2 = list6.frontToBack();
		displayResults(result1.equals("{A}"), "testInterleave");
		displayResults(result2.equals("{L}"), "testInterleave");

		result1 = list5.backToFront();
		result2 = list6.backToFront();
		displayResults(result1.equals("{A}"), "testInterleave");
		displayResults(result2.equals("{L}"), "testInterleave");
// Testing list7 and list8
		list7.addBack("A");
		list7.addBack("B");

		result1 = list7.frontToBack();
		displayResults(result1.equals("{AB}"), "testInterleave");

		list8.addBack("L");
		list8.addBack("M");

		result2 = list8.frontToBack();
		displayResults(result2.equals("{LM}"), "testInterleave");

		list7.interleave(list8);
		result1 = list7.frontToBack();
		result2 = list8.frontToBack();
		displayResults(result1.equals("{AM}"), "testInterleave");
		displayResults(result2.equals("{LB}"), "testInterleave");

		result1 = list7.backToFront();
		result2 = list8.backToFront();
		displayResults(result1.equals("{MA}"), "testInterleave");
		displayResults(result2.equals("{BL}"), "testInterleave");





		/* Write additional tests here to ensure all of your pointers
		   have been updated correctly. */

	}

	public static void displayResults (boolean passed, String testName) {
       /* There is some magic going on here getting the line number
        * Borrowed from:
        * http://blog.taragana.com/index.php/archive/core-java-how-to-get-java-source-code-line-number-file-name-in-code/
        */

        testCount++;
        if (passed)
        {
            System.out.println ("Passed test: " + testName);
            testPassCount++;
        }
        else
        {
            System.out.println ("Failed test: " + testName + " at line "
                                + Thread.currentThread().getStackTrace()[2].getLineNumber());
        }
    }

}
