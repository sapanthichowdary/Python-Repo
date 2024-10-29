import java.util.Scanner;
public class Number
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int n;
        int flag = 0;
        n=sc.nextInt();
        for(int i=0;i<n;i++)
        {
            if (i*(i+1)==n)
            {
                flag = 1;
                break;
            }
        }
        if(flag==1)
        {
            System.out.println("YES");
        }
        else
        {
            System.out.println("NO");
        }
    }
}