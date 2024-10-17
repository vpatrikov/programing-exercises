import java.lang.String;
import java.lang.StringBuilder;

public class strings {
    public String remove_char(String word, char a){
        StringBuilder result = new StringBuilder();
        char[] wordArr = word.toCharArray();
        
        for(int i = 0; i < wordArr.length; i++)
        {
            if (wordArr[i] != a) {
                result.append(wordArr[i]);
            }
        }

        return result.toString();
    }
}
