class Program
{
    public static int FindSmallestInt(int[] args)
    {
        int smallest_value = args[0];

        foreach (var item in args)
        {
            if (item < smallest_value)
            {
                smallest_value = item;
            }
        }
        
        return smallest_value;
    }

    static void Main(string[] args)
    {
        int[] array = { 78, 56, 232, 12, 11, 43 };
        Console.WriteLine(FindSmallestInt(array));
    }
}