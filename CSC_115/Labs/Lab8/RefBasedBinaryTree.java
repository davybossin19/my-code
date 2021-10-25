import java.lang.Math;
/*
 * RefBasedBinaryTree.java
 *
 * A ref-based BinaryTree meant to store values of type Integer
 */
public class RefBasedBinaryTree implements BinaryTree {
    protected TreeNode root;

    public RefBasedBinaryTree() {
        root = null;

    }

    public void insert(Integer value){
            insert(null, root, value);
    }

    /*
     * Purpose: recursively determines the shortest path (root to leaf)
     *      inserts a new TreeNode with given value at that leaf
     * Parameters: TreeNode parent - the parent to t
     *             TreeNode t - the current TreeNode in recursive traversal
     *             Integer value - the value to be inserted
     * Returns: nothing
     */
    private void insert(TreeNode parent, TreeNode t, Integer value) {
        if (t==null) {
            if(parent == null)
                root = new TreeNode(value);
            else if(parent.getLeft()==null)
                parent.setLeft(new TreeNode(value));
            else
                parent.setRight(new TreeNode(value));

        }  else {
            int htLeft = height(t.getLeft());
            int htRight = height(t.getRight());
            if (htLeft>htRight)
                insert(t, t.getRight(), value);
            else
                insert(t, t.getLeft(), value);
        }
    }

    /*
     * Purpose: computes and returns the height of BinaryTree t
     *      NOTE a BinaryTree with no node is height 0
     * Parameters: TreeNode t - the BinaryTree
     * Returns: int - the height
     */
    private int height(TreeNode t) {
        // TODO...
        if (t == null) {
          return 0;
        } else {
          int leftHeight = height(t.left);
          int rightHeight = height(t.right);

          return 1 + Math.max(leftHeight, rightHeight);

          // if (rightHeight > leftHeight) {
          //   return 1 + rightHeight;
          // }
          // else return 1 + leftHeight;
        }
    }


    public void inOrder(){
        // TODO...
        inOrder(root);
    }

    private void inOrder(TreeNode n) {
      if (n == null) {
        return;
      } else {
        inOrder(n.left);
        System.out.println(n.data);
        inOrder(n.right);
      }
    }



    public void preOrder(){
        // TODO...
        preOrder(root);
    }

    private void preOrder(TreeNode n) {
      if (n == null) {
        return;
      } else {
        System.out.println(n.data);
        preOrder(n.left);
        preOrder(n.right);
      }
    }


    public void postOrder(){
        // TODO...
        postOrder(root);
    }

    private void postOrder(TreeNode n) {
      if (n == null) {
        return;
      } else {
        postOrder(n.left);
        postOrder(n.right);
        System.out.println(n.data);
      }
    }



    public String toString() {
        // TODO...
        return getInOrderString(root);

    }

    private String getInOrderString(TreeNode n) {
      if (n == null) {
        return "";
      } else {
        return getInOrderString(n.left) + n.data + " " + getInOrderString(n.right);
      }
    }

    // public int getSumTree() {
    //    return getSumTree(root);
    // }
    //
    // private int getSumTree(TreeNode n) {
    //   if (n == null) {
    //     return 0;
    //   } else {
    //     return getSumTree(n.left) + n.data + getSumTree(n.right);
    //   }
    // }




    // provided for testing of RefBasedBinaryTree class
    public static void main(String[] args) {

        RefBasedBinaryTree myTree = new RefBasedBinaryTree();
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

        // System.out.println(myTree.getSumTree());
    }
}
