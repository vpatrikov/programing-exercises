import java.lang.String;
import java.lang.StringBuilder;

public class words_scramble {
    public String spinWords(String sentence) {
        StringBuilder sbuilder = new StringBuilder();
        String[] sent_arr = sentence.split(" ");
        for (int i = 0; i < sent_arr.length; i++) {
                if (sent_arr[i].length() >= 5){
                    sbuilder.append(sent_arr[i]);
                    sbuilder.reverse();
                    sent_arr[i] = sbuilder.toString();
                    sbuilder.setLength(0);
                }
        }
        return String.join(" ", sent_arr);
    }
}
