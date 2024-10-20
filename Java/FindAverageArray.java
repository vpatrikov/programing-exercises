import java.util.Scanner;
public class FindAverageArray {
    public static int [] get_input_array(int[] array, int size, Scanner scanner){
        if (array.length != 0 ){
            throw new IllegalArgumentException("Array is not empty!");
        }else{
            for (int i = 0; i < array.length; i++){
                array[i] = scanner.nextInt();
            }
        }
        return array;
    }
    public static double find_average(int[] array) {
        if (array.length == 0) {
            return 0;
        }else{
            int sum = 0;
            for (int item : array) {
                sum += item;
            }
            return sum / array.length;
        }
    }
}
