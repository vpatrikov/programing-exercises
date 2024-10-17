public class single_line_return {
    public static String greet(String name) {
        return name.equals("Johnny") ? "Hello, my love!" : String.format("Hello, %s!", name);
        
      }
}
