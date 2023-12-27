public static Dictionary<char, int> Count(string str)
        {
            Dictionary<char, int> dict = new Dictionary<char, int>();
            int count = 0;
            if (str.Length == 1)
            {
                dict.Add(Convert.ToChar(str), 1);
            }
            else
            {
                for (int i = 0; i < str.Length; i++)
                {
                    if (i > 0)
                    {
                      if (!dict.ContainsKey(str[i-1]))
                      {
                        dict.Add(str[i - 1], count);
                      }
                    }
                    if (i == str.Length - 1)
                    {
                      if (!dict.ContainsKey(str[i]))
                      {
                        dict.Add(str[i], 1);
                      }
                    }

                    count = 0;

                    foreach (char character in str)
                    {
                        if (character == str[i])
                        {
                            count++;
                        }
                        else
                        {
                            continue;
                        }
                    }
                }
            }
            return dict;
        }