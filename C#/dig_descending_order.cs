// Digits of an integer in descending order.
using System;
using System.Linq;

class Program
{
    public static int DescendingOrder(int num)
    {
        int[] array = num.ToString().Select(o => Convert.ToInt32(o) - 48).ToArray();

        for (int i = 0; i < array.Length; i++)
        {
            for (int n = 0; n < array.Length - i - 1; n++)
            {
                if (array[n] < array[n+1])
                {
                    var temp = array[n];
                    array[n] = array[n + 1];
                    array[n + 1] = temp;
                }
            }
        }

        string arrayAsString = string.Join("", array.Select(num => num.ToString()));
        int resultingInteger = int.Parse(arrayAsString);

        return resultingInteger;
    }


static void Main(string[]args)
    {
        Console.ReadKey();
    }
}