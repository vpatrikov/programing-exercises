import java.lang.Math;

public class fundamentals {

    public static int[] between(int a, int b) {
        int size = b - a + 1;
        int[] numbers = new int[size];
        for (int i = 0; i < size; i++) {
            numbers[i] = a + i;
        }
        return numbers;
    }

    public static int[] countPositivesSumNegatives(int[] input) {
        if (input == null || input.length == 0) {
            return new int[0];
        }
        int sum = 0;
        int count = 0;
        for (int i : input) {
            if (i > 0) {
                count++;
            } else {
                sum += i;
            }
        }
        return new int[] { count, sum };
    }

    public static int[] invert(int[] array) {
        for (int i = 0; i < array.length; i++) {
            array[i] *= -1;
        }
        return array;
    }

    public int countSheeps(Boolean[] arrayOfSheeps) {
        int count = 0;
        for (Boolean boolean1 : arrayOfSheeps) {
            if (boolean1 != null && boolean1) {
                count++;
            }
        }
        return count;
    }

    public static boolean isDivisible(long n, long x, long y) {
        return n % x == 0 && n % y == 0;
    }

    public static int[] digitize(long n) {
        char[] n_char_arr = (Long.toString(n)).toCharArray();
        int[] n_array = new int[n_char_arr.length];
        for (int i = n_char_arr.length - 1; i >= 0; i--) {
            n_array[n_char_arr.length - 1 - i] = Character.getNumericValue(n_char_arr[i]);
        }

        return n_array;
    }

    public static int[] countBy(int x, int n) {
        int[] array = new int[n];

        for (int i = 0; i < array.length; i++) {
            array[i] = x * (i + 1);
        }
        return array;
    }

    static int round_up(double number, double division){
        return (int)Math.round(number/division);
    }

    static boolean IsInteger(double number){
        if (number % 1 == 0){
            System.out.println(number % 1);
            return true;
        }else{
            return false;
        }
    }

    public static boolean zeroFuel(double distanceToPump, double mpg, double fuelLeft) {
        return (mpg*fuelLeft) >= distanceToPump;
    }

    public static int expressionsMatter(int a, int b, int c) {
        return Math.max(
                Math.max(
                        Math.max(a + b + c, a * b * c),
                        Math.max((a + b) * c, a * (b + c))
                ),
                Math.max(
                        a + (b * c),
                        (a * b) + c
                )
        );
    }
    public static void main(String[] args) {

    }

    public static boolean getXO(String str) {

        int count_x = 0;
        int count_o = 0;

        char[] chars = str.toLowerCase().toCharArray();
        for (char item : chars) {
            if (item == 'x') {
                count_x++;
            } else if (item == 'o') {
                count_o++;
            }
        }
        return count_x == count_o;
    }
}
