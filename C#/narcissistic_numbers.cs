using System;
using System.Collections.Generic;

namespace ConsoleApp1
{
    class MainClass
    {
        public static bool Narcissistic(int value)
        {
            string valueString = value.ToString();

            List<int> list = new List<int>();

            int sum = 0;

            foreach (char item in valueString)
            {
                if (char.IsDigit(item))
                {
                    list.Add(int.Parse(item.ToString()));
                }
            }

            for (int i = 0; i < list.Count; i++)
            {
                list[i] = (int)Math.Pow(list[i], list.Count);
            }

            foreach (var item in list)
            {
                sum += item;
            }

            return sum == value;
        }
        public static void Main(string[] args)
        {
            Console.WriteLine(Narcissistic(153));
            Console.WriteLine(Narcissistic(153819084)); 
        }
    }
}
