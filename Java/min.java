public class min {
    public static int findSmallestInt(int[] args) {
        if (args == null || args.length == 0) {
            throw new IllegalArgumentException("Array must not be null or empty");
        }
            int min = args[0];
            for (int i = 1; i < args.length; i++) {
                if (args[i] < min)
                {
                    min = args[i];
                }
            }
            return min;
        }
}
