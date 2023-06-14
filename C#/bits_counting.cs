// Converts a decimal number into binary and then counts the ones

using System;

public class Kata
{
    public static int CountBits(int n)
    {
        string binary = Convert.ToString(n, 2);

        int count = 0;

        foreach (var item in binary)
        {
            if (item == '1')
            {
                count++;
            }
        }

        return count;
    }
}