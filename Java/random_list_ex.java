import java.util.ArrayList;
import java.util.Scanner;
import java.util.Collections;

public class random_list_ex {
    public static void main(String[]args){
        ArrayList<Integer> list = new ArrayList<Integer>();
        System.out.println("Enter the amount of elements you want to have in your list: ");
        Scanner scanner = new Scanner(System.in);
        int size = scanner.nextInt();
        int sum = 0;
        for (int i =0; i < size; i++){
            int temp = 0;
            while (true) {
                try {
                    System.out.println("Enter element #" + (i+1));
                    temp = scanner.nextInt();
                    break;
                } catch (Exception e) {
                    System.out.println("Invalid Input. Please enter an Integer.");
                    scanner.nextLine();
                }

            }
            list.add(temp);
            sum += temp;
        }
        scanner.close();
        System.out.println("list sum: " + sum);

        System.out.print("\nelements of list in order of input:" );
        for(int number : list){
            System.out.print(" " + number);
        }

        Collections.reverse(list);
        System.out.print("\nelements of the list reversed:");
        for(int number : list){
            System.out.print(" " + number);
        }

    }

}
