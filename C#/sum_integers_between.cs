using System;

namespace Solution
{
    class Program
    {
        public static int GetSum(int a, int b)
        {
            int sum = 0;

            if (a == b)
            {
                return a;
            }
            else if (a < b) 
            {
                for (int i = a; i <= b; i++)
                {
                    sum += i;
                }
            }
            else
            {
                for (int i = b; i <= a; i++)
                {
                    sum += i;
                }
            }

            return sum;
        }

        static void Main(string[] args)
        {
            Console.WriteLine(GetSum(1, 1));
            Console.WriteLine(GetSum(-1, 0));
            Console.WriteLine(GetSum(1, 2));
        }
    }
}