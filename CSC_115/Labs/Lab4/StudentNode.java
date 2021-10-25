public class StudentNode {

  private Student data;
  protected StudentNode next;

  public StudentNode(Student student) {
    data = student;
    next = null;
  }

  public StudentNode(Student student, StudentNode next) {
    data = student;
    this.next = next;

  }

  public StudentNode getNext() {
    return next;
  }

  public void setNext(StudentNode sN) {
    next = sN;
  }

  public Student getData() {
    return data;
  }

  public void setData(Student data) {
    this.data = data;
  }


}
