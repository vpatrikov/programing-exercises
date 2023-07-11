using System;

namespace Solution
{
	class Program
	{
		public static string GetReadableTime(int seconds)
		{
			int hours = seconds / 3600;
			int minutes = (seconds % 3600) / 60;
			int remainingSeconds = (seconds % 3600) % 60;

			return string.Format("{0:D2}:{1:D2}:{2:D2}", hours, minutes, remainingSeconds);

			// TimeSpan result = TimeSpan.FromSeconds(seconds);
			// return result.ToString("hh':'mm':'ss"); -> Doesn't work with 359999 seconds.
		}
	}
}
