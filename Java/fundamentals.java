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
        if(input == null || input.length == 0)
        {
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
        return new int [] {count, sum};
    }

    public static int[] invert(int[] array) {
        for (int i = 0; i < array.length; i++) {
            array[i] *= -1;
        }
        return array;
      }
}
