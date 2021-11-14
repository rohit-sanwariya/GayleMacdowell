import java.util.HashSet;

public class HashLearTest {


    public static void main(String[] args) {
        int array[] = {7,98,123,43,7,7,7,7,98};
        HashSet<Integer> h = new HashSet<Integer>();
        for(int a: array){
            h.add(a);
        }for(int a: h){
            System.out.println(a);
        }

    }



}
