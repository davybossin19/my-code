/*
 * ArrayBasedBinaryTree.java
 *
 * An array-based BinaryTree meant to store values of type Integer
 */
public class ArrayBasedBinaryTree implements BinaryTree {
    private static final int CAPACITY = 100;
    protected Integer[] data;
    protected int root;
    protected int size;

    public ArrayBasedBinaryTree() {
        data = new Integer[CAPACITY];
        root = 0;
        size = 0;
    }

    /*
     * Purpose: inserts the given value into data at next available
     *  position in a level-order traversal
     *  The tree remains complete after insertion.
     * Parameters: Integer value - value to insert
     * Returns: nothing
	 * Precondition: the underlying array is not full
     */
    public void insert(Integer value) {
        data[size] = value;
        size++;
    }


    /*
     * Purpose: calculates and returns the index of t's left child
     * Parameters: int t - index of current element in this ArrayBasedBinaryTree
     * Returns: int - index of left child
     */
    protected int getLeft(int t) {
        // TODO...
        return (2*t) + 1;
    }

    /*
     * Purpose: calculates and returns the index of t's right child
     * Parameters: int t - index of current element in this ArrayBasedBinaryTree
     * Returns: int - index of right child
     */
    protected int getRight(int t) {
        // TODO...
        return (2*t) + 2;
    }


    public void inOrder(){
        inOrder(root);
    }

    private void inOrder(int index) {
      if (index >= size) {
        return;
      } else {
        inOrder(getLeft(index));
        System.out.println(data[index]);
        inOrder(getRight(index));
      }
    }


    public void preOrder(){
        // TODO...
        preOrder(root);
    }

    private void preOrder(int index) {
      if (index >= size) {
        return;
      } else {
        System.out.println(data[index]);
        preOrder(getLeft(index));
        preOrder(getRight(index));
      }
    }


    public void postOrder(){
        // TODO...
        postOrder(root);
    }

    private void postOrder(int index) {
      if (index >= size) {
        return;
      } else {
        postOrder(getLeft(index));
        postOrder(getRight(index));
        System.out.println(data[index]);
      }
    }


    public String toString() {
        // TODO...

        return getInOrderString(root);
    }

    private String getInOrderString(int index) {
      if (index >= size) {
        return "";
      } else {
        return getInOrderString(getLeft(index)) + data[index] + " " + getInOrderString(getRight(index));
      }
    }



    public static void main(String[] args) {

        ArrayBasedBinaryTree myTree = new ArrayBasedBinaryTree();
        for(int i=2; i<8; i++) {
            myTree.insert(i);
        }
        System.out.println("in");
        myTree.inOrder();
        System.out.println("pre");
        myTree.preOrder();
        System.out.println("post");
        myTree.postOrder();

        System.out.println("toString\n" + myTree);
    }

}
