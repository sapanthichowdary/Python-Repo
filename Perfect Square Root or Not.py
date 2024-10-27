import java.util.Scanner;
public class Perfect
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int flag = 0;
        for (int i=1;i<=n/2;i++)
        {
            if(i*i==n)
            {
                flag=1;
            }
        }
        if (flag==0)
        {
            System.out.println("False");
        }
        else
        {
            System.out.println("True");
        }
    }
}