package Learning_Classes;

public class Car {
    int age;
    String brand;
    String model;

    public Car(){
        this.age = 0;
        this.brand = "Unknown";
        this.model = "Unknown";
    }

    public Car(int age, String brand, String model){
        this.age = age;
        this.brand = brand;
        this.model = model;
    }
}
