using System;
using System.Collections.Generic;
using System.Linq;

namespace ConsoleApp1
{
    class Program
    {
        public static int SquareDigits(int n)
        {
            int[] digitArray = n.ToString().Select(digit => int.Parse(digit.ToString())).ToArray();
            List<int> numbersList = new List<int>();

            foreach (int digit in digitArray)
            {
                numbersList.Add(digit*digit);
            }

            int result = int.Parse(string.Join("", numbersList));

            return result;
        }
        static void Main(string[] args)
        {
            int a = SquareDigits(9119);
            Console.WriteLine("\n" + a);
        }
    }
}