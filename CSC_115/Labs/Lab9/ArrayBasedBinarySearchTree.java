public class ArrayBasedBinarySearchTree extends ArrayBasedBinaryTree{

  public void insert(Integer value) {
    // System.out.println("Start of public insert");
    if (size == 0) {
      // System.out.println("Adding fit")
      data[0] = value;
    } else {
      insert(value, 0);
    }
    size++;
  }

  private void insert(Integer value, Integer index) {
    if (value == data[index]) {
      return;
    } else if (value < data[index]) {
      if (data[getLeft(index)] == null) {
        data[getLeft(index)] = value;
      } else {
        insert(value, getLeft(index));
      }
    } else {
      if (data[getRight(index)] == null) {
        data[getRight(index)] = value;
      } else {
        insert(value, getRight(index));
      }
    }
  }


    public static void main(String[] args) {
        ArrayBasedBinarySearchTree emptyTree = new ArrayBasedBinarySearchTree();

        ArrayBasedBinarySearchTree myTree = new ArrayBasedBinarySearchTree();
        myTree.insert(2);
        myTree.insert(1);
        myTree.insert(5);
        myTree.insert(7);
        myTree.insert(0);
        myTree.insert(4);
        myTree.insert(6);

        System.out.println("in");
        myTree.inOrder();
        System.out.println("pre");
        myTree.preOrder();
        System.out.println("post");
        myTree.postOrder();

        System.out.println("toString\n" + myTree);
    }

}
