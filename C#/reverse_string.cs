using System;
namespace Solution
{
    class Program
    {
        public static string ReverseWords(string str)
        {
            List<string> output = new List<string>();
            string[] words = str.Split(' ');

            foreach (var word in words)
            {
                char[] charArray = word.ToCharArray();
                Array.Reverse(charArray);
                string reversedWord = new string(charArray);
                output.Add(reversedWord);
            }

            string rev_str = string.Join(" ", output);

            return rev_str;
        }
    }
}