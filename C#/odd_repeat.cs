namespace Solution
{
    class Kata
    {
        public static int find_it(int[] seq)
        {
            Dictionary<int, int> countDictionary = new Dictionary<int, int>();

            foreach (int item in array)
            {
                if (countDictionary.ContainsKey(item))
                {
                    countDictionary[item]++;
                }
                else
                {
                    countDictionary[item] = 1;
                }
            }

            foreach (var kvp in countDictionary)
            {
                if (kvp.Value % 2 == 1)
                {
                    return kvp.Value;
                    break;
                }
            }

        }
    }
}