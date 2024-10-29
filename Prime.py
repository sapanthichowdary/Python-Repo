import java.util.Scanner;
public class Prime
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int flag=0;
        for(int i=2;i<n;i++)
        {
            if(n%2==0)
            {
                flag=1;
                break;
            }
        }
        if(flag==0)
        {
            System.out.println("Prime");
        }
        else
        {
            System.out.println("Not Prime");
        }
    }
}