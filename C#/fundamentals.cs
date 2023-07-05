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
        static void Main(string[] args)
        {
        }
    }
}