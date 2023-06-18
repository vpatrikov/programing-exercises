using System;

namespace Solution
{
  public static class Program
  {
    public static int binToDec(string s)
    {
      int binary;
      int.TryParse(s, out binary);
      int decimalNum = Convert.ToInt32(binary.ToString(), 2);
      return decimalNum;
    }
  }
}