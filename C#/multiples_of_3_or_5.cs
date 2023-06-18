// Gets the sum of all numbers bellow a given integer that are multiples of 3 or 5

public static class Kata
{
  public static int Solution(int value)
  {
    int sum = 0;

    for (int i = 0; i < value; i++)
    {
      if (i % 3 == 0 || i % 5 == 0 || i % 15 == 0)
      {
        sum += i;
      }
    }
    
    return sum;
  }
}