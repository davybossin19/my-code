public class QueueRefBased<T> implements Queue<T> {

    private QueueNode<T> front;
    private QueueNode<T> back;
    private int count;

    public QueueRefBased() {
        front = null;
        back = null;
    }

    public int size() {
        // TODO: complete
        return count;
    }


    public boolean isEmpty() {
        // TODO: complete
        if (count == 0) {
          return true;
        } else {
          return false;
        }
    }


    public void enqueue (T element) {
        // TODO: complete
        QueueNode<T> n = new QueueNode<T>(element);

        if (count == 0) {
          front = n;
          back = n;
        } else {
          back.setNext(n);
          back = n;
        }
        count++;
    }

    public T dequeue() {
        // TODO: complete
        T val = front.getValue();
        if (count == 1) {
          front = null;
          back = null;
        } else {
          front = front.getNext();
        }
        count--;
        return val;
    }

    public T peek() {
        // TODO: complete

        return front.getValue();
    }

    public void makeEmpty() {
        // TODO: complete
        front = null;
        back = null;
        count = 0;
    }
}
