import java.util.HashSet;
import java.util.LinkedList;

public class RemoveDuplicateLinkedList {
    public static void main(String[] args) {

        LinkedList<Integer> list = new LinkedList<Integer>();
        HashSet<Integer> set = new HashSet<>();
        for (int i = 0; i < 10 ; i++) {
            list.add((int)Math.floor(Math.random()*(9)+1));

        }
        System.out.println(list);
        for (int i = 0; i < list.size(); i++) {
            set.add(list.get(i));
        }
        for (int i = 0; i < list.size(); i++) {
            if (set.contains(list.get(i))){
                list.remove(i);
            }
        }
        System.out.println(list);

    }

}
