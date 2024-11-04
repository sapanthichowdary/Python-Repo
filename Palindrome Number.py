import java.util.Scanner;
public class Palindrome
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        for(int i=1;i<=t;i++)
        {
            int n = sc.nextInt();
            int p = n;
            int rev = 0;
            while(n!=0)
            {
                int r=n%10;
                rev=rev*10+r;
                n=n/10;
            }
            if(rev==p)
            {
                System.out.println("True");
            }
            else
            {
                System.out.println("False");
            }
        }
    }
}