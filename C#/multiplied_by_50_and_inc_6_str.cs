using System;

public class Kata
{
  public static string Problem(String a)
    {
        double number;
        if (double.TryParse(a, out number))
        {
            double calc = (number * 50) + 6;
            return calc.ToString();
        }
        else
        {
            return "Error";
        }
    }
}