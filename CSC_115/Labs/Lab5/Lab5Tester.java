/*
 * Lab5Tester.java
 */
public class Lab5Tester {

    private static int testPassCount = 0;
    private static int testCount = 0;

    public static void main (String[] args) {

        try {
            testAddOne();
            testAddOneRecursive();
            testDoubleAll();
            testDoubleOddValues();
            testSumValues();
            testProduct();
            testDoubleAtOddPositions();
            testIsSorted();
            testAllNegative();



        } catch (Exception e) {

            System.out.println("Your code threw an Exception.");
            System.out.println("Perhaps a stack trace will help:");
            e.printStackTrace(System.out);
        }
        System.out.println("Passed " + testPassCount + "/" + testCount + " tests");
    }

    public static void testAddOne() {

        System.out.println("Testing addOne-----------------------------------");


        IntegerLinkedList emptyList = new IntegerLinkedList();
        IntegerLinkedList list3 = new IntegerLinkedList();

        list3.addFront(-2);
        list3.addFront(0);
        list3.addFront(7);

        emptyList.addOne();
        // System.out.println(emptyList);
        displayResults(emptyList.toString().equals(""), "testAddOne - empty");


        list3.addOne();
        // System.out.println(list3);
        displayResults(list3.toString().equals("8 1 -1"), "testAddOne - length3");

    }

    public static void testAddOneRecursive() {

        System.out.println("Testing addOneRecursive--------------------------");

        IntegerLinkedList emptyList = new IntegerLinkedList();
        IntegerLinkedList list3 = new IntegerLinkedList();

        list3.addFront(-2);
        list3.addFront(0);
        list3.addFront(7);

        emptyList.addOneRecursive();
        // System.out.println(emptyList);
        displayResults(emptyList.toString().equals(""), "testAddOne - empty");


        list3.addOneRecursive();
        // System.out.println(list3);
        displayResults(list3.toString().equals("8 1 -1"), "testAddOne - length3");
    }

    public static void testDoubleAll() {
      System.out.println("Testing doubleAll----------------------------------");

      IntegerLinkedList emptyList = new IntegerLinkedList();
      IntegerLinkedList list3 = new IntegerLinkedList();

      list3.addFront(-2);
      list3.addFront(0);
      list3.addFront(7);

      emptyList.doubleAll();
      // System.out.println(emptyList);
      displayResults(emptyList.toString().equals(""), "testDoubleAll - empty");


      list3.doubleAll();
      // System.out.println(list3);
      displayResults(list3.toString().equals("14 0 -4"), "testDoubleAll- length3");
    }

    public static void testDoubleOddValues() {
      System.out.println("Testing doubleOddValues----------------------------");

      IntegerLinkedList emptyList = new IntegerLinkedList();
      IntegerLinkedList list3 = new IntegerLinkedList();
      IntegerLinkedList list1 = new IntegerLinkedList();


      list3.addFront(-1);
      list3.addFront(3);
      list3.addFront(7);

      list1.addFront(5);

      emptyList.doubleOddValues();
      // System.out.println(emptyList);
      displayResults(emptyList.toString().equals(""), "testDoubleOddValues - empty");


      list3.doubleOddValues();
      // System.out.println(list3);
      displayResults(list3.toString().equals("14 6 -2"), "testDoubleOddValues- length3");

      list1.doubleOddValues();
      // System.out.println(list3);
      displayResults(list1.toString().equals("10"), "testDoubleOddValues- length3");
    }

    public static void testProduct() {
      System.out.println("Testing product------------------------------------");

      IntegerLinkedList emptyList = new IntegerLinkedList();
      IntegerLinkedList list3 = new IntegerLinkedList();
      IntegerLinkedList list4 = new IntegerLinkedList();


      int result;
      int expected;

      list3.addFront(-2);
      list3.addFront(0);
      list3.addFront(7);

      list4.addFront(-2);
      list4.addFront(2);
      list4.addFront(7);

      result = emptyList.product();
      expected = 1;
      // System.out.println(emptyList);
      displayResults(result == expected, "testProduct - empty");


      result = list3.product();
      expected = 7 * 0 * -2;
      // System.out.println(list3);
      displayResults(result == expected, "testProduct- length3");

      result = list4.product();
      expected = 7 * 2 * -2;
      // System.out.println(result);
      displayResults(result == expected, "testProduct- length3");

    }


    public static void testSumValues() {

      System.out.println("Testing sumValues----------------------------------");


        IntegerLinkedList emptyList = new IntegerLinkedList();
        IntegerLinkedList list3 = new IntegerLinkedList();

        list3.addFront(-2);
        list3.addFront(0);
        list3.addFront(7);

        int result = emptyList.sum();
        displayResults(result == 0, "testSumValues - empty");

        result = list3.sum();
        displayResults(result == 5, "testSumValues - length3");
    }


    public static void testDoubleAtOddPositions() {

        System.out.println("Testing doubleOddPositionValue-------------------");


        IntegerLinkedList emptyList = new IntegerLinkedList();
        IntegerLinkedList list3a = new IntegerLinkedList();

        list3a.addFront(-2);
        list3a.addFront(5);
        list3a.addFront(7);
        list3a.addFront(8);

        emptyList.doubleOddPositionValues();
        displayResults(emptyList.toString().equals(""), "testDoubleAtOddPositions - empty");

        list3a.doubleOddPositionValues();
        displayResults(list3a.toString().equals("8 14 5 -4"), "testDoubleAtOddPositions - length3");
    }

    public static void testIsSorted() {

        System.out.println("Testing isSorted-------------------");


        IntegerLinkedList emptyList = new IntegerLinkedList();
        IntegerLinkedList list3a = new IntegerLinkedList();
        IntegerLinkedList list3b = new IntegerLinkedList();


        boolean result;
        boolean expected;

        list3a.addFront(-2);
        list3a.addFront(5);
        list3a.addFront(7);
        list3a.addFront(8);

        list3a.addFront(10);
        list3a.addFront(9);
        list3a.addFront(-5);
        list3a.addFront(-10);

        result = emptyList.isSorted();
        expected = true;
        displayResults(result == expected, "testIsSorted - empty");

        result = list3a.isSorted();
        expected = false;
        displayResults(result == expected, "testIsSorted - length3");

        result = list3b.isSorted();
        expected = true;
        displayResults(result == expected, "testIsSorted - length3");
    }

    public static void testAllNegative() {
      System.out.println("Testing isNegative-------------------");


      IntegerLinkedList emptyList = new IntegerLinkedList();
      IntegerLinkedList list3a = new IntegerLinkedList();
      IntegerLinkedList list3b = new IntegerLinkedList();


      boolean result;
      boolean expected;

      list3a.addFront(-2);
      list3a.addFront(-5);
      list3a.addFront(-7);
      list3a.addFront(-8);

      list3b.addFront(10);
      list3b.addFront(9);
      list3b.addFront(-5);
      list3b.addFront(-10);

      result = emptyList.allNegative();
      expected = true;
      displayResults(result == expected, "testingAllNegative - empty");

      result = list3a.allNegative();
      expected = true;
      // System.out.println(result);
      displayResults(result == expected, "testingAllNegative - length3");

      result = list3b.allNegative();
      expected = false;
      // System.out.println(result);
      displayResults(result == expected, "testingAllNegative - length3");
    }




    public static void displayResults (boolean passed, String testName) {
        /* There is some magic going on here getting the line number
         * Borrowed from:
         * http://blog.taragana.com/index.php/archive/core-java-how-to-get-java-source-code-line-number-file-name-in-code/
         */
        testCount++;
        if (passed)
        {
            System.out.println ("Passed test: " + testCount);
            testPassCount++;
        }
        else
        {
            System.out.println ("Failed test: " + testName + " at line "
                                + Thread.currentThread().getStackTrace()[2].getLineNumber());
        }
    }


}
