import java.lang.Math;
/*
 * RefBasedBinarySearchTree.java
 *
 * A ref-based BinaryTree meant to store values of type Integer
 */
public class RefBasedBinarySearchTree extends RefBasedBinaryTree {

  public void insert(Integer value) {
    if (root == null) {
      root = new TreeNode(value);
    } else {
      insert(root, value);
    }
  }

  private void insert(TreeNode cur, Integer value) {
    if (cur.getValue() == value) {
      return;
    } else if (value < cur.getValue()) {
      if (cur.left == null) {
        cur.left = new TreeNode(value);
      } else {
        insert(cur.left, value);
      }
    } else {
      if (cur.right == null) {
        cur.right = new TreeNode(value);
      } else {
        insert(cur.right, value);
      }
    }
  }

  public boolean find(int val) {
    return find(val, root);
  }

  private boolean find(int val, TreeNode cur) {
    if (cur == null) {
      return false;
    } else if (cur.getValue() == val) {
      return true;
    } else if (val < cur.getValue()) {
      return find(val, cur.left);
    } else {
      return find(val, cur.right);
    }
  }

  public int getMax() throws TreeEmptyException {
    if (root == null) {
      throw new TreeEmptyException();
    } else {
      int max = root.getValue();
      TreeNode cur = root;

      while (cur.right != null) {
        cur = cur.right;
        if (cur.getValue() > max) {
          max = cur.getValue();
        }
      }
      return max;
    }
  }

  public TreeNode getSibling(int key) {
  if (root == null) {
    return null;
  }
  else if (root.getValue().compareTo(key) == 0) {
    return null;
  }
  else {
    return getSibling(key, root);
  }
}

private TreeNode getSibling(int key, TreeNode cur) {
  if (cur == null) {
    return null;
    // Key is bigger than key of cur
  } else if (cur.getValue().compareTo(key) < 0) {
    if (cur.getRight().getValue().compareTo(key) == 0) {
      return cur.getLeft();
    } else {
      return getSibling(key, cur.getRight());
    }
  } else {
    if (cur.getLeft().getValue().compareTo(key) == 0) {
      return cur.getRight();
    } else {
       return getSibling(key, cur.getLeft());
    }
  }
}

    public static void main(String[] args) {
        // use these trees to test the methods you will implement
        RefBasedBinarySearchTree emptyTree = new RefBasedBinarySearchTree();
        RefBasedBinarySearchTree myTree = new RefBasedBinarySearchTree();
        myTree.insert(2);
        myTree.insert(1);
        myTree.insert(5);
        myTree.insert(7);
        myTree.insert(0);
        myTree.insert(4);
        myTree.insert(6);
        myTree.insert(10);

        System.out.println("in");
        myTree.inOrder();
        System.out.println("pre");
        myTree.preOrder();
        System.out.println("post");
        myTree.postOrder();

        // System.out.println("toString\n" + myTree);
        //
        // System.out.println("Testing getMax()----------------");
        // try{
        //   System.out.println(emptyTree.getMax() + " this shouldnt happen");
        // } catch (TreeEmptyException e) {
        //   System.out.println("Exception caught as expected");
        // }
        // try{
        //   System.out.println("Result: " + myTree.getMax() +", Should be: 10");
        // } catch (TreeEmptyException e) {
        //   System.out.println("Something went wrong");
        // }
        // System.out.println();
        //
        // System.out.println("testing find()-------------");
        // System.out.println(myTree.find(2) + ": should be true");
        // System.out.println(myTree.find(4) + ": should be true");
        // System.out.println(myTree.find(7) + ": should be true");
        // System.out.println(myTree.find(25) + ": should be false");
        // System.out.println();
        //
        // System.out.println("testing sum()");
        // System.out.println(myTree.sum() + " Should be 35");
        // System.out.println(emptyTree.sum() + "Should be 0");
        // System.out.println();

        System.out.println("Testing level order()------------");
        System.out.println(myTree.getSibling(4));
        myTree.levelOrder();
    }
}
