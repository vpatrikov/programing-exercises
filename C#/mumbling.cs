using System;
using System.Collections.Generic;
using System.Linq;

namespace ConsoleApp1
{
    class Program
    {
        public static string Accum(string s)
        {
            string output = "";
            for (int i = 0; i < s.Length; i++)
            {
                char c = s[i];

                for (int n = 0; n < i + 2; n++)
                {
                    if (n == 0)
                    {
                        output += char.ToUpper(c);
                    }
                    else if (n == i + 1 && i != s.Length - 1)
                    {
                        output += '-';
                    }
                    else if (n != i + 1)
                    {
                        output += char.ToLower(c);
                    }
                }      
            }

            return output;
        }
        static void Main(string[] args)
        {
            string test_1 = Accum("abcd");
            string test_2 = Accum("RqaEzty");

            Console.WriteLine(test_1);
            Console.WriteLine(test_2);

        }
    }
}