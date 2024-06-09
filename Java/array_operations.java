import java.util.Scanner;
import java.util.Random;

public class array_operations {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n;

        while (true) {
            System.out.println("Enter n: ");

            try {
                n = scanner.nextInt();
            } catch (Exception e) {
                System.out.println("An exception occured: " + e);
                scanner.next();
                continue;
            }

            if (n < 15 || n > 35) {
                System.out.println("Input out of range (should be between 15 and 35.\n");
            } else {
                break;
            }
        }
        scanner.close();

        Random rand = new Random();

        int arr[] = new int[n];

        for (int i = 0; i < n; i++) {
            arr[i] = rand.nextInt(300);
        }

        System.out.println("The elements of the array:");
        for (int i = 0; i < n; i++) {
            System.out.print(arr[i] + " ");
        }

        int count = 0;

        for (int i = 0; i < n; i++) {
            if (arr[i] % 3 == 0) {
                count++;
            }
        }

        System.out.println("\nElements divisible by 3 are " + count);

        int min_index = 0;
        for (int i = 0; i < n; i++) {
            if (arr[min_index] > arr[i]) {
                if (arr[i] % 6 == 4) {
                    min_index = i;
                }
            }
        }

        System.out.println("Index of the smallest element: " + min_index);

        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    int temp = arr[j + 1];
                    arr[j + 1] = arr[j];
                    arr[j] = temp;
                }
            }
        }

        System.out.println("Sorted array: ");
        for (int k : arr) {
            System.out.print(k + " ");
        }
    }
}
