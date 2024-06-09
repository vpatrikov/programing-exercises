import java.util.Scanner;

public class add_compare_num {

    static int get_input(Scanner scanner) {
        return scanner.nextInt();
    }

    public static void main(String[]args){
        Scanner scanner = new Scanner(System.in);
        
        int a;
        int b;

        System.out.print("Enter a: ");
        a = get_input(scanner);
        System.out.print("Enter b: ");
        b = get_input(scanner);
        
        System.out.println("a + b = " + (a+b));
    
        if (a > b) {
            System.out.println("a > b");
        }else if (a < b){
            System.out.println("a < b");
        }else{
            System.out.println("a = b");
        }
    }
}