// Breaks cammel case.
using System;
using System.Text.RegularExpressions;

namespace ConsoleApp1
{

    class Program
    {
        public static string BreakCamelCase(string str)
        {
            string[] words = Regex.Split(str, @"(?<!^)(?=[A-Z])");
            return string.Join(" ", words);
        }

        static void Main(string[] args)
        {

            BreakCamelCase("camelCasing");
        }
    }
}