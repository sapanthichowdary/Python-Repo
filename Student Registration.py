import java.util.Scanner;
public class Register
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        for(int i=1;i<=t;i++)
        {
            int n,m,k;
            n=sc.nextInt();
            m=sc.nextInt();
            k=sc.nextInt();
            if((m-k)>=n)
            {
                System.out.println("YES");
            }
            else
            {
                System.out.println("NO");
            }
        }
    }
}