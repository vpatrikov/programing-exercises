// Takes 10 numbers as paramether and prints them out as a phone number

using System;
using System.Collections.Generic;

namespace ConsoleApp1
{

    class Program
    {
        public static string CreatePhoneNumber(int[] numbers)
        {
            Queue<string> phone_number = new Queue<string>();

            phone_number.Enqueue("(");

            for (int i = 0; i < 3; i++)
            {
                phone_number.Enqueue(numbers[i].ToString());
            }

            phone_number.Enqueue(")");
            phone_number.Enqueue(" ");

            for (int i = 3; i < 6; i++)
            {
                phone_number.Enqueue(numbers[i].ToString());
            }

            phone_number.Enqueue("-");

            for (int i = 6; i < numbers.Length; i++)
            {
                phone_number.Enqueue(numbers[i].ToString());
            }

            string phone_number_str = string.Join("", phone_number);

            return phone_number_str;
        }
        
    }
}