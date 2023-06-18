// Returns the amount of smileys in an array
using System;
using System.Collections.Generic;

namespace ConsoleApp1
{

    class Program
    {
        public static int CountSmileys(string[] smileys)
        {
            int count = 0;
            foreach (string item in smileys)
            {
                if (item == ":D" || item == ":)" || item == ";-D" ||
                    item == ":~)" || item == ";~D" || item == ":-)" ||
                    item == ";)" || item == ";-)" || item == ";D" ||
                    item == ":~D" || item == ";~)" || item == ":-D")
                {
                    count++;
                }
            }
            return count;
        }

    }
}