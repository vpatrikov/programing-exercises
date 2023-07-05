using System;

namespace ConsoleApp1
{
    class Program
    {
        public static long RowSumOddNumbers(long n)
        {
            long startNumber = (n * (n - 1)) + 1;
            long sum = 0;

            for (int i = 0; i < n; i++)
            {
                sum += startNumber + (2 * i);
            }

            return sum;
        }
    }
}