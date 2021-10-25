import java.util.*;

/*
 * An implementation of a binary search tree.
 *
 * This tree stores both keys and values associated with those keys.
 *
 * More information about binary search trees can be found here:
 *
 * http://en.wikipedia.org/wiki/Binary_search_tree
 *
 */
class WordFrequencyBST <K extends Comparable<K>, V>  {

	private static int testPassCount = 0;
	private static int testCount = 0;

	public static final int BST_PREORDER  = 1;
	public static final int BST_POSTORDER = 2;
	public static final int BST_INORDER   = 3;

	private TreeNode<K,V> root;
	private int numElements;

	public WordFrequencyBST(){
		// TODO: complete constructor
		root = null;
		numElements = 0;
	}


	/*
	 * Purpose: Update the BST by handling input word
	 * Parameters: K key - The key to handle
	 * Returns: Nothing
	 * Explanation: If there is no element in the tree
	 *   with the given key, then a new element
	 *   should be created and placed into the correct
	 *   location of the BST (determined by the Binary
	 *   Search Tree property). Otherwise, the existing
	 *   element with the given key should have its
	 *   value incremented by one.
	 */
	public void handleWord(K key) {
		// TODO: complete this method
		if (containsKey(root, key)) {
			TreeNode<K,V> nodeWithKey = findNode(root,key);
			nodeWithKey.incrementValue();
		} else {
			TreeNode<K, V> newNode = new TreeNode(key);
			if (root == null) {
				root = newNode;
			} else {
				insert(newNode, root);
			}
			numElements++;
		}
	}

	private void insert(TreeNode<K, V> newNode, TreeNode<K, V> cur) {
		// System.out.println("I");
		if (newNode.compareTo(cur.key) < 0) {
			if (cur.left == null) {
				cur.left = newNode;
			} else {
				insert(newNode, cur.left);
			}
		} else if (newNode.compareTo(cur.key) > 0) {
			// System.out.println("Checking right")
			if (cur.right == null) {
				cur.right = newNode;
			} else {
				insert(newNode, cur.right);
			}
		}
	}

	private boolean containsKey(TreeNode<K, V> cur, K key) {
		if (cur == null) {
			return false;
		}
		if (cur.compareTo(key) == 0) {
			return true;
		}
		if (cur.compareTo(key) < 0) {
			return containsKey(cur.right, key);
		}

		return containsKey(cur.left, key);
	}

	private TreeNode<K, V> findNode(TreeNode<K, V> cur, K key) {
		// System.out.println(cur);
		if (cur == null) {
			return null;
		}
		if (cur.compareTo(key) == 0) {
			return cur;
		}

		if (cur.compareTo(key) > 0) {
			return findNode(cur.left, key);
		}
		return findNode(cur.right, key);
	}

	// private boolean isLeafNode(TreeNode<K,V> cur) {
	// 	return cur.left == null && cur.right == null;
	// }

	/*
	 * Purpose: Get the value of the given key
	 * Parameters: K key - the key to search for
	 * Returns: int - the key's associated value
	 * Note: Although we are using generic entries
	 *       where the value could be any type, for
	 *       this particular application of the BST
	 *       we will assume the value is an integer.
	 */
	public int getFrequency(K key) {
		// TODO: complete this method
		if (containsKey(root,key)) {
			TreeNode<K,V> keyNode = findNode(root, key);
			if (keyNode.value instanceof Integer) {
				Integer tempValue = ((Integer) keyNode.value);
				return (int) tempValue;
			} else {
				return 0;
			}
		} else {
			return 0;
		}
	}

	/*
	 * Purpose: Get the total number of nodes in the tree
	 * Parameters: None
	 * Returns: int - the total number of nodes in the tree
	 */
	public int size() {
		// TODO: complete this method
		return numElements; // so it compiles
	}

	public void inOrderPrint() {
		inOrderPrint(root);
	}

	private void inOrderPrint(TreeNode<K,V> cur) {
		if (cur == null) {
			return;
		}
		inOrderPrint(cur.left);
		System.out.println(cur);
		inOrderPrint(cur.right);

	}

	/*
	 * Purpose: Return a list of all the key-value entries stored in the tree
	 * Parameters: none
	 * Returns: A list of all key-value entries stored in the tree, constructed
	 *          by performining a level-order traversal of the tree.
	 *
	 * Level-order is most commonly implemented using a queue of nodes.
	 * From Wikipedia, the algorithm is:
	 *
	 * levelorder()
	 *		q = empty queue
	 *		q.enqueue(root)
	 *		while not q.empty do
	 *			node := q.dequeue()
	 *			visit(node)
	 *			if node.left != null then
	 *			      q.enqueue(node.left)
	 *			if node.right != null then
	 *			      q.enqueue(node.right)
	 */
	public List<Entry<K,V>> entryList() {
		List<Entry<K, V>> resultList = new LinkedList<Entry<K,V>>();
		LinkedList<TreeNode<K,V>> queue = new LinkedList<TreeNode<K,V>>();

		queue.add(root);

		while(queue.size() != 0) {
			TreeNode<K,V> n = queue.removeFirst();
			Entry<K,V> e = new Entry(n.key, n.value);
			resultList.add(e);

			if (n.left != null) {
				queue.add(n.left);
			}
			if (n.right != null) {
				queue.add(n.right);
			}
		}

		// TODO: complete this method
		// System.out.println(resultList);

		return resultList;
	}


	/****************************************************
	* Helper functions for Insertion and Search testing *
	****************************************************/

	public List<Entry<K,V>> entryList (int which) {
		List<Entry<K,V>> resultList = new LinkedList<Entry<K,V> >();

		if (which == BST_PREORDER) {
			preOrderRecursive(root, resultList);
		}
		else if (which == BST_INORDER) {
			inOrderRecursive(root, resultList);
		}
		else if (which == BST_POSTORDER) {
			postOrderRecursive(root, resultList);
		}

		return resultList;
	}

	// completed for you
	private void inOrderRecursive (TreeNode<K,V> n, List <Entry<K,V>> resultList) {
		if (n == null) {
			return;
		}
		inOrderRecursive(n.left, resultList);
		resultList.add(new Entry<K,V>(n.key, n.value));
		inOrderRecursive(n.right,resultList);
	}

	// completed for you
	private void preOrderRecursive (TreeNode<K,V> n, List <Entry<K,V>> resultList) {
		if (n == null) {
			return;
		}
		resultList.add(new Entry<K,V>(n.key, n.value));
		preOrderRecursive(n.left, resultList);
		preOrderRecursive(n.right,resultList);
	}

	// completed for you
	private void postOrderRecursive (TreeNode<K,V> n, List <Entry<K,V>> resultList) {
		if (n == null) {
			return;
		}
		postOrderRecursive(n.left, resultList);
		postOrderRecursive(n.right,resultList);
		resultList.add(new Entry<K,V>(n.key, n.value));
	}

	/****************************************************
	* Helper functions to populate a Heap from this BST *
	****************************************************/

	public MaxFrequencyHeap<K,V> createHeapFromTree() {
		MaxFrequencyHeap<K,V> maxHeap = new MaxFrequencyHeap<K,V>();
		addToHeap(maxHeap, root);
		return maxHeap;
	}

	public void addToHeap(MaxFrequencyHeap<K,V> h, TreeNode<K,V> n) {
		if (n != null) {
			addToHeap(h, n.left);
			h.insert(new Entry<K,V>(n.key, n.value));
			addToHeap(h, n.right);
		}
	}

}
