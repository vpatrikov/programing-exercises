using System;

namespace Solution
{
	class Program
	{
		public static int binaryArrayToNumber(int[] BinaryArray)
	    {
	        int decimalNum = 0;
	        int length = BinaryArray.Length;

	        for (int i = length - 1; i >= 0; i--)
	        {
	            int binaryDigit = BinaryArray[i];
	            int decimalDigit = binaryDigit * (int)Math.Pow(2, length - i - 1);
	            decimalNum += decimalDigit;
	        }

	        return decimalNum;
	    }
	}
}