package Learning_Classes;
import java.util.Scanner;
public class LearnMain {
    public static void main(String[]args){
        Scanner scanner = new Scanner(System.in);
        System.out.println("Hello World!");
        String name;
        name = scanner.nextLine();
        System.out.println("Hello " + name);

        Car car_1 = new Car();
        Car car_2 = new Car(2004, "Skoda", "Fabia");
        
        System.out.println(car_1.age);
        System.out.println(car_2.age);
        
        scanner.close();
    }
}
