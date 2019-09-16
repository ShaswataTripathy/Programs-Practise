
using System;
using System.Collections.Generic;

namespace CharFreuency
{
 public class Program
    {
        public static void Main(string[] args)
        {

         int[] c = new int[(int)char.MaxValue];
         string s = "shaswata Tripathy";

        foreach (char t in s)
        {
            c[(int)t]++;
        }

        for (int i = 0; i < (int)char.MaxValue; i++)
        {
            if (c[i] > 0 && char.IsLetter((char)i))
            {
                Console.Write("{0}{1}",(char)i,c[i]);
            }
        }
        }
    }
}