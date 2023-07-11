using System;

namespace Solution
{
	class Program
	{
		public static int[] MoveZeroes(int[] arr)
	    {
	        int index = Array.IndexOf(arr, 0);

	        for (int i = 0; i < arr.Length; i++)
	        {
	            if (index != -1)
	            {
	                arr = arr.Where((value, i) => i != index).ToArray();

	                Array.Resize(ref arr, arr.Length + 1);
	                arr[arr.Length - 1] = 0;
	            }
	        }

	        return arr;
	    }
	}
}