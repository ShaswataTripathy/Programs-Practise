using System;

static int FindMajority(int[] arr,int n)
{
    int maxCount =0;
    int index = -1;

    for (int i = 0; i < n; i++)
    {
        int count =0 ;
        for (int j = 0; j < n; j++)
        {
            if(arr[i] == arr[j])
                count++;

        }
        if (count > maxCount)
        {
            maxCount = count;
            index = i ;

        }
    }

    if( maxCount > n/2)
    {
        return arr[index];
    }
    else
    {
        return -1;
    }
}

static public void Main (){

        int []arr = {1, 1, 2, 1, 3, 5, 1};
        int n = arr.Length;

        Console.WriteLine(findMajority(arr, n));
        Console.ReadLine();
    }
}
