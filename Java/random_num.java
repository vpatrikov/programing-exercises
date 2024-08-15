import java.util.Random;

public class random_num {
    public static void main(String[] args) {
        Random random = new Random();
        int a;

        do {
            a = random.nextInt(6) + 1;
            System.out.println("You rolled: "+ a);
        } while (a != 6);

        System.out.println("YOU WIN!");
    }

}
