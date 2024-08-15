public class highest_scoring_word {
    public static String high(String s) {
        String[] words = s.split(" ");

        int highest_score = 0;
        String highest_word = "";

        for (String word : words) {
            int sum = 0;
            for (int i = 0; i < word.length(); i++) {
                sum += (int) word.charAt(i) - 96;
            }
            if (sum > highest_score) {
                highest_score = sum;
                highest_word = word;
            }
        }
        return highest_word;
    }
    public static void main(String[] args) {
        System.out.println(high("man i need a taxi up to ubud"));
    }
}