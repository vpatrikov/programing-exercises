import java.util.Scanner;

public class draw_figure {

    void print_square(int rows, int columns, String symbol){
        for(int i = 0; i < rows; i++)
        {
            for (int j = 0; j < columns; j++) {
                System.out.print(symbol);
            }
            System.out.println();
        }
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int rows;
        int columns;
        String symbol;
        System.out.println("Enter number of rows: ");
        rows = scanner.nextInt();
        System.out.println("Enter number of columns: ");
        columns = scanner.nextInt();
        System.out.println("Enter the symbol you want to use: ");
        symbol = scanner.next();
        
        scanner.close();
    }
}