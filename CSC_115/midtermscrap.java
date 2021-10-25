public boolean find(String data) {
  if (root == null) {
    return false;
  } else if (root.data.equals(data)) {
    return true;
  } else {
    find(data, root);
  }
}

private boolean find(String data, TreeNode cur);
if (cur == null) {
  return false;
} else {
  if {}
  return find(data, cur.left) || cur.data.equals(data) || find(data, cur.right);
}

public int imbalance(TreeNode n) {
  if (n == null) {
    return 0;
  } else if (height(n.left) == height(n.right) {
    return 0;
  } else {
    return height(n.right) - height(n.left);
  }
}

private int height(TreeNode cur) {
  if (cur == null) {
    return -1;
  } else {
    return 1 + Math.max(height(cur.right), height(cur.left));
  }
}

public int sizeOfSubTree(K key) {
  TreeNode n = find(key);
  if (n = null) {
    return 0;
  } else {
    return sizeOfSubTree(n)
  }

private int sizeOfSubTree(TreeNode n) {
  if (n == null) {
    return 0;
  } else {
    return 1 + sizeOfSubTree(n.left) + sizeOfSubTree(n.right);
  }
}

}
public TreeNode find(K key) {
  if (root.key == key) {
    return root;
  } else {
    find(key, root);
  }
}

private TreeNode find(K key, TreeNode cur) {
  if (cur == null) {
    return null;
  } else if (cur.key.compareTo(key)) {
    return cur;
  } else if (cur.key.compareTo(key) < 0) {
    return find(key, cur.right);
  } else if (cur.key.compareTo(key) > 0) {
    return find(key, cur.left);
  }
}

public boolean contains(K key) {
  if (root == null) {
    return false;
  } else if (root.key.compareTo(key)) {
    return true;
  } else {
    contains(key, root);
  }
}

private boolean contains(K key, TreeNode cur) {
  if (cur == null) {
    return false;
  } else if (cur.key.compareTo(key)) {
    return true;
  } else if (cur.key.compareTo(key) < 0) {
    return contains(key, cur.right);
  } else if (cur.key.compareTo(key)) {
    return contains(key, cur.left);
  }
}

public int largestList() {
  int max = 0;
  Iterator<List<Integer>> iter = table.iterator();

  while (iter.hasNext()) {
    List<Integer> l = iter.next();
    if (l.size() > max) {
      max = l.size();
    }
  }
  // for (int i = 0;i<m;i++) {
  //   if (table.get(i).size() > max) {
  //     max = table.get(i).size()
  //   }
  // }
  return max;
}

public int totalCollison() {
  int totalCollisions = 0;
  for (int i = 0; i < m;i++) {
    if (table.get(i).size() > 1) {
      totalCollison += table.get(i).size() - 1;
    }
  }
  return totalCollisions;
}

public TreeNode<K> getSibling(K key) {
  if (root == null) {
    return null;
  }
  else if (root.key.compareTo(key) == 0) {
    return null;
  }
  else {
    getSibling(key, root);
  }
}

private TreeNode<K> getSibling(K key, TreeNode cur) {
  if (cur == null) {
    return null;
    // Key is bigger than key of cur
  } else if (cur.key.compareTo(key) < 0) {
    if (cur.right.key.compareTo(key) == 0) {
      return cur.left;
    } else {
      getSibling(key, cur.right);
    }
  } else {
    if (cur.left.key.compareTo(key) == 0) {
      return cur.right;
    } else {
      getSibling(key, cur.left);
    }
  }
}
