import java.util.Scanner;
public class Search
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for(int i=0;i<n;i++)
        {
            arr[i]=sc.nextInt();
        }
        int key = sc.nextInt();
        int flag=0;
        for(int i=0;i<n;i++)
        {
            if(arr[i]==key)
            {
                flag=1;
                break;
            }
        }
        if(flag==1)
        {
            System.out.println("True");
        }
        else
        {
            System.out.println("False");
        }
    }
}