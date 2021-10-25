public class StudentLinkedList implements StudentList{
  private StudentNode head;
  private int count;


  public StudentLinkedList() {
    head = null;
    count = 0;
  }


  public void add(Student s) {
    StudentNode sNode = new StudentNode(s);
    if (count == 0) {
      head = sNode;
    } else {
      StudentNode cur = head;
      while (cur.getNext() != null) {
        cur = cur.getNext();
      }
      cur.setNext(sNode);
    }
    count++;
  }

  public String toString() {
    String result = "";
    StudentNode cur = head;

    while (cur != null) {
      result += cur.getData() + "\n";
      cur = cur.getNext();
    }
    return result;
  }

  public void removeFront() {
    if (count > 0) {
      head = head.getNext();
      count--;
    }
  }

  public boolean contains(Student s) {
    boolean result = false;
    StudentNode cur = head;
    while (cur != null) {
      if (cur.getData().equals(s)) {
        result = true;
      }
      cur = cur.getNext();
    }
    return result;
  }

  public int size(){
    return count;
  }
}
