using System;

namespace ConsoleApp1
{
    class MainClass
    {
        public int Min(int[] list)
            {
                if (list.Length == 0)
                {
                    throw new ArgumentException("The array cannot be empty.");
                }

                int min = int.MaxValue;

                for (int i = 0; i < list.Length; i++)
                {
                    if (list[i] < min)
                    {
                        min = list[i];
                    }
                }

                return min;
            }

            public int Max(int[] list)
            {
                if (list.Length == 0)
                {
                    throw new ArgumentException("The array cannot be empty.");
                }

                int max = int.MinValue;

                for (int i = 0; i < list.Length; i++)
                {
                    if (list[i] > max)
                    {
                        max = list[i];
                    }
                }

                return max;
            }
        }

    }
