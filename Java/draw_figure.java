import java.util.Scanner;

public class draw_figure {

    static void print_square(int rows, int columns, String symbol) {
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < columns; j++) {
                System.out.print(symbol);
            }
            System.out.println();
        }
    }

    static void print_triangle(int size, String symbol) {
        for (int i = 1; i <= size; i++) {
            for (int j = 0; j < i; j++) {
                System.out.print(symbol);
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String symbol;
        System.out.println("Enter the symbol you want to use: ");
        symbol = scanner.next();

        scanner.nextLine();

        String choice;
        System.out.println("What do you want to print? \n\nsquare\ntriangle\n\n");
        choice = scanner.nextLine();

        switch (choice) {
            case "square":
                int rows;
                System.out.println("Enter number of rows: ");
                rows = scanner.nextInt();

                int columns;
                System.out.println("Enter number of columns: ");
                columns = scanner.nextInt();

                print_square(rows, columns, symbol);
                break;
            case "triangle":
                int size;
                System.out.println("Enter the size of the triangle: ");
                size = scanner.nextInt();

                print_triangle(size, symbol);
                break;
            default:
                System.out.println("Invalid choice!");
                break;
        }
        scanner.close();
    }
}