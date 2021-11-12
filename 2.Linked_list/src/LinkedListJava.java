public class LinkedListJava {
    Node head;

    //append
    public void append(int data){
        if(head == null) {
            head = new Node(data);
            return;
        }
        Node current = head;

        while (current.next != null) {
        current = current.next;

        }
        current.next = new Node(data);
        }

        /**
         * prepend
         */
        public void prepend(int data){
        if(head == null){
            Node head = new Node(data);

        }
        Node newHead = new Node(data);
        newHead.next = head;
        head = newHead;
        }

        //delete with value
    public void deleteWithValue(int value){
        if(head == null) return;
        if (head.data == value){
            head = head.next;
        }
        Node current = head;
        while (current.next != null){
            if(current.next.data == value){
                current.next = current.next.next;
                return;
            }
            current = current.next;
        }
    }
    public void displayLinkedList(){
        if(head == null) return;
        Node current = head;
        while (current != null){
            System.out.println(current.data);
            current = current.next;
        }
    }

    public static void main(String[] args) {
            LinkedListJava list = new LinkedListJava();
            list.prepend(25);
            list.prepend(29);
            list.prepend(39);
            list.append(27);
            list.displayLinkedList();
    }
}
