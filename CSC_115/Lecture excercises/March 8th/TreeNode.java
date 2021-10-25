public class TreeNode {

	private int data;
	// 1. What other fields will we need in a TreeNode?
	protected TreeNode left;
	protected TreeNode right;
	// 2. Write constructor(s) for a TreeNode
	public TreeNode (int data) {
		this.data = data;
		left = null;
		right = null;

	}

	public TreeNode (int data, TreeNode right, TreeNode left) {
		this.data = data;
		this.left = left;
		this.right = right;
	}

	public void preOrder(TreeNode node) {
		if (node == null) {
			return;
		}
		preOrder(node.left);
		System.out.print(node.data + ',');
		preOrder(node.right);
	}




	public static void main(String[] args) {

		// 3. Create an instance of a TreeNode (call it a) with int value 5
		TreeNode a = new TreeNode(5);

		// 4a. Create another instance of a TreeNode (call it b) with int value 8
		//     and make it the right child of the TreeNode a that you created above.
		TreeNode b = new TreeNode(8);
		a.right = b;

		// 4b. Print out the value of the TreeNode b without using b in the print statement
		System.out.println(a.right.data);

		// 5. Create a tree with the following structure:
		//            5
		//          /   \
		//         2     8
		//       /   \
		//      1     4
		TreeNode c = new TreeNode(2);
		a.left = c;

		TreeNode d = new TreeNode(4);
		c.right = d;

		TreeNode e = new TreeNode(1);
		c.left = e;

		a.preOrder(a);

		// 6. How could we print out the contents of the tree? What is the expected output?
	}


}
