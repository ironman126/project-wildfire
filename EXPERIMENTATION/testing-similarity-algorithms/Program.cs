using System;
using System.Collections.Generic;
/*



DO NOT USE THIS SCRIPT. DUE TO ME BEING LAUGHABLY AWFUL AT C# I AM REMAKING IN PYTHON. IT DOESN'T WORK.



*/
namespace testing_similarity_algorithms
{
    class Program
    {
        static void Main(string[] args)
        {
          int [,] wildfires = new int [5,4] { // [row, column]
             {80, 9, 2, 178} ,
             {97, 5, 15, 345} ,  //  Pretend first column is heat, second humidity, third cloud cover, fourth wind direction. */
             {300, 1, 7, 50} ,
             {150, 4, 3, 20} ,
             {120, 5, 30, 120} ,
            };

            int [,] CurrentData = new int [1, 4] {
              {140, 3, 8, 50}
            };

            foreach(int i in wildfires) {
              Console.WriteLine("DEPRECATED");
            }

        }
    }
}
