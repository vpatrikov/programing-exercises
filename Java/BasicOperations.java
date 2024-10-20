public class BasicOperations {
    public static Integer basicMath(String op, int v1, int v2)
    {
        return switch(op){
            case "+"-> v1 + v2;
            case "-"-> v1 - v2;
            case "*"-> v1 * v2;
            case "/" -> {
                if (v2 == 0){
                    throw new IllegalArgumentException("Division by zero");
                }else{
                   yield v1 / v2;
                }
            }
            default-> throw new IllegalArgumentException("Inlvaid operator: " + op);
        };
    }
}
