import java.lang.Math;
import java.util.LinkedList;
/*
 * RefBasedBinaryTree.java
 *
 * A ref-based BinaryTree meant to store values of type Integer
 */
public class RefBasedBinaryTree implements BinaryTree {
    protected TreeNode root;

    public RefBasedBinaryTree() {
        this.root = null;
    }

    public void insert(Integer value){
        if (root==null)
            root = new TreeNode(value);
        else
            insert(null, root, value);

    }
    // not a balanced insert
    private void insert(TreeNode parent, TreeNode t, Integer value) {
        if (t==null) {
            if(parent.getLeft()==null) {
                parent.setLeft(new TreeNode(value));
			} else {
                parent.setRight(new TreeNode(value));
			}
        }  else {
            int htLeft = height(t.getLeft());
            int htRight = height(t.getRight());
            if (htLeft>htRight) {
                insert(t, t.getRight(), value);
			} else {
                insert(t, t.getLeft(), value);
			}
        }
    }

    private int height(TreeNode t) {
        if (t==null) {
            return -1;
		} else {
            int highest = Math.max(height(t.getLeft()), height(t.getRight()));
            return 1 + highest;
        }
    }

    /*
     * Purpose: prints the value at each TreeNode in this BinaryTree
     *          following an in-order traversal
     * Parameters: none
     * Returns: Nothing
     */
    public void inOrder(){
        inOrder(root);
        System.out.println();
    }

    /*
     * Purpose: prints the value at each TreeNode in t,
     *          following an in-order traversal
     * Parameters: TreeNode t
     * Returns: Nothing
     */
    private void inOrder(TreeNode t){
        if (t==null)
            return;
        else {
            inOrder(t.getLeft());
            System.out.print(t.getValue() + " ");
            inOrder(t.getRight());
        }
    }

    /*
     * Purpose: prints the value at each TreeNode in this BinaryTree
     *          following a pre-order traversal
     * Parameters: none
     * Returns: Nothing
     */
    public void preOrder(){
        preOrder(root);
        System.out.println();
    }

    /*
     * Purpose: prints the value at each TreeNode in t,
     *          following a pre-order traversal
     * Parameters: TreeNode t
     * Returns: Nothing
     */
    private void preOrder(TreeNode t){
        if (t==null)
            return;
        else {
            System.out.print(t.getValue() + " ");
            preOrder(t.getLeft());
            preOrder(t.getRight());
        }
    }

    /*
     * Purpose: prints the value at each TreeNode in this BinaryTree
     *          following a post-order traversal
     * Parameters: none
     * Returns: Nothing
     */
    public void postOrder(){
        postOrder(root);
        System.out.println();
    }

    /*
     * Purpose: prints the value at each TreeNode in t,
     *          following a post-order traversal
     * Parameters: TreeNode t
     * Returns: Nothing
     */
    private void postOrder(TreeNode t){
        if (t==null)
            return;
        else {
            postOrder(t.getLeft());
            postOrder(t.getRight());
            System.out.print(t.getValue() + " ");
        }
    }

    /*
     * Purpose: returns a String reprensentation of this BinaryTree
     * Parameters: none
     * Returns: String - the representation
     */
    public String toString() {
        return toString(root);
    }

    private String toString(TreeNode t) {
        if(t==null)
            return "";
        else {
            String s = "";

            s += toString(t.getLeft());
            s += t.getValue() + " ";
            s += toString(t.getRight());

            return s;
        }
    }

    public int sum() {
      return sum(root);
    }

    private int sum(TreeNode cur) {
      if (cur == null) {
        return 0;
      } else {
        return sum(cur.getLeft()) + cur.getValue() + sum(cur.getRight());
      }
    }

    public boolean find(int val) {
      return find(val, root);
    }

    private boolean find(int val, TreeNode cur) {
      if (cur == null) {
        return false;
      } else {
        return find(val, cur.left)||cur.getValue() == val||find(val, cur.right);
      }
    }

    public int getMax() throws TreeEmptyException {
      if (root == null) {
        throw new TreeEmptyException();
      }
      return getMax(root);
    }

    private int getMax(TreeNode cur) {
      if (cur == null) {
        return 0;
      } else {
        return Math.max(getMax(cur.left),getMax(cur.right));
      }
    }

    private int max(int a, int b, int c) {
      if (a >= b && a >= c) {
        return a;
      } else if (b >= a && b >=c) {
        return b;
      } else {
        return c;
      }
    }

    public void levelOrder() {
      LinkedList<TreeNode> queue = new LinkedList<TreeNode>();

		  queue.add(root);

		  while(queue.size() != 0) {
			     TreeNode n = queue.removeFirst();
			     System.out.print(n + " ");

			     if (n.left != null) {
				     queue.add(n.left);
			        }
			      if (n.right != null) {
				     queue.add(n.right);
			        }
		    }
    }




    public static void main(String[] args) {
        // use these trees to test the methods you will implement in Part II
        RefBasedBinaryTree emptyTree = new RefBasedBinaryTree();
        RefBasedBinaryTree myTree = new RefBasedBinaryTree();
        for(int i=2; i<8; i++) {
            myTree.insert(i);
        }

        myTree.insert(10);

        System.out.println("Testing getMax()----------------");
        try{
          System.out.println(emptyTree.getMax() + " this shouldnt happen");
        } catch (TreeEmptyException e) {
          System.out.println("Exception caught as expected");
        }
        try{
          System.out.println("Result: " + myTree.getMax() +", Should be: 10");
        } catch (TreeEmptyException e) {
          System.out.println("Something went wrong");
        }
        System.out.println();

        System.out.println("testing find()-------------");
        System.out.println(myTree.find(2) + ": should be true");
        System.out.println(myTree.find(4) + ": should be true");
        System.out.println(myTree.find(7) + ": should be true");
        System.out.println(myTree.find(25) + ": should be false");
        System.out.println();

        System.out.println("testing sum()");
        System.out.println(myTree.sum() + "Should be 37");
        System.out.println(emptyTree.sum() + "Should be 0");
        System.out.println();

        System.out.println("Testing level order()------------");
        myTree.levelOrder();



    }

}
