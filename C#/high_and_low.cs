// Gets the highest and lowest numbers and prints them

using System;

public static class Kata
{
    public static string HighAndLow(string numbers)
    {
        string[] numberStrings = numbers.Split(' ');
        int size = numberStrings.Length;
        int[] array = new int[size];

        for (int i = 0; i < size; i++)
        {
            array[i] = int.Parse(numberStrings[i]);
        }

        for (int i = 0; i < array.Length; i++)
        {
            for (int n = 0; n < array.Length - i - 1; n++)
            {
                if (array[n] > array[n + 1])
                {
                    var temp = array[n];
                    array[n] = array[n + 1];
                    array[n + 1] = temp;
                }
            }
        }

        string low = array[0].ToString();
        string high = array[array.Length - 1].ToString();
        
        return high + " " + low;
    }
}