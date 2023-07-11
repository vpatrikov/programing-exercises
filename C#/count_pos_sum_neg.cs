using System;

namespace Soliton
{
    class Program
    {
        public static int[] CountPositivesSumNegatives(int[] input)
            {
                if (input == null || input.Length == 0)
                {
                    return new int[0];
                }

                int count = 0;
                int negativeSum = 0;

                foreach (int item in input)
                {
                    if (item > 0)
                    {
                        count++;
                    }
                    else if (item < 0)
                    {
                        negativeSum += item;
                    }
                }

                return new int[] { count, negativeSum };
            }
    }
}