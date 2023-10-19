class Program
{
    static void Main(string[] args)
    {
        List<string> cars = new List<string>();
        Console.WriteLine("How many cars do you want to enter?");
        int size = int.Parse(Console.ReadLine());

        for (int i = 0; i < size; i++)
        {
            Console.Clear();
            Console.WriteLine($"Enter the brand, model and consumption of car {i+1}");
            string input = Console.ReadLine();
            string[] array = input.Split(' ');

            cars.AddRange(array);
        }
        List <float> consumption = new List<float>();

        foreach (string item in cars)
        {
            if (item.All(char.IsDigit))
            {
                consumption.Add(Single.Parse(item));
            }
        }

        Console.Clear();

        for (int i = 0; i < cars.Count; i += 3)
        {
            if (i + 2 < cars.Count)
            {
                Console.WriteLine($"Car: {cars[i]} {cars[i + 1]} \nConsumption: {cars[i + 2]}\n\n");
            }
        }

        float sum = 0;

        foreach (float item in consumption)
        {
            sum += item;
        }

        Console.WriteLine($"\nThe average consumption is: {sum/size}");
    }
}