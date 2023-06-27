// A method that (if the name of the person starts with the letter 'r') will return that the person is
// playing banjo. Else it will return that the person is not playing banjo
class Program
{
    public static string AreYouPlayingBanjo(string name)
    {
        if (name[0] == 'r' || name[0] == 'R')
        {
            // Console.WriteLine($"{name} plays banjo");
            return name + " plays banjo";
        }
        else
        {
            // Console.WriteLine($"{name} does not play banjo");
            return name + " does not play banjo";
        }
    }

    static void Main(string[]args)
    {
        AreYouPlayingBanjo("Bravo");
        AreYouPlayingBanjo("John");
        AreYouPlayingBanjo("Ron");
        Console.ReadKey();
    }
}