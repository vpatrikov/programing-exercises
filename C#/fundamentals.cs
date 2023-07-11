using System;
using System.Collections.Generic;
using System.Linq;

namespace ConsoleApp1
{
    class Program
    {
        public static string AbbrevName(string name)
        {
            string[] names_split = name.Split(new char[] { ' ' }, 2);

            string fname = names_split[0];
            string lname = names_split[1];

            string abbreviature = fname[0] + "." + lname[0];

            return abbreviature;
        }

        public static double basicOp(char operation, double value1, double value2)
        {
            switch (operation)
            {
                case '+':
                    return value1 + value2;
                case '-':
                    return value1 - value2;
                case '*':
                    return value1 * value2;
                case '/':
                    return value1 / value2;
                default:
                    return 0;
            }
        }

        public static string SwitchItUp(int number)
        {
            string output = "";
            switch (number)
            {
                case 0: output = "Zero"; break;
                case 1: output = "One"; break;
                case 2: output = "Two"; break;
                case 3: output = "Three"; break;
                case 4: output = "Four"; break;
                case 5: output = "Five"; break;
                case 6: output = "Six"; break;
                case 7: output = "Seven"; break;
                case 8: output = "Eight"; break;
                case 9: output = "Nine"; break;
            }
            return output;
        }

        public static string AddBinary(int a, int b)
        {
            int decimalSum = a + b;
            Console.WriteLine($"Decimal Sum: {decimalSum}");
            string binarySum = Convert.ToString(decimalSum, 2);
            return binarySum;
        }   

        public static int summation(int num)
        {
            List<int> list = new List<int>();

            for (int i = 0; i < num + 1; i++)
            {
                list.Add(i);
            }

            int sum = 0;

            foreach (int item in list)
            {
                sum += item;
            }

            return sum;
        }

        public static string Bmi(double weight, double height)
        {
            double bmi = weight / (height*height);

            if (bmi <= 18.5) return "Underweight";
            else if (bmi <= 25) return "Normal";
            else if (bmi <= 30.0) return "Overweight";
            else return "Obese";
        }

        public static int СenturyFromYear(int year)
        {
            double century = ((year - 1) / 100) + 1;
            return Convert.ToInt32(century);
        }
        
        static void Main(string[] args)
        {
        }
    }
}