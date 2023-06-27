    // Returns the average of the elements in an array.
    // NOTE: Turns out there's an ".Average" method for arrays in C#

    using System;

    class Program
    { 
        public static double FindAverage(double[] array)
        {
            double sum = 0;

            if (array.Length != 0)
            {
                foreach (double item in array)
                {
                    sum += item;
                }

                return sum / array.Length;
            }
            else
            {
                return sum;
            }
        }

    static void Main(string[]args)
        {
            double[] array = new double[] { 17, 16, 16, 16, 16, 15, 17, 17, 15, 5, 17, 17, 16 };
            double average = FindAverage(array);
            Console.WriteLine("Average: " + average);
            Console.ReadKey();
        }
    }