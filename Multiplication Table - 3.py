import java.util.Scanner;
public class Multiplication
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int n,a,b;
        n=sc.nextInt();
        a=sc.nextInt();
        b=sc.nextInt();
        for(int i=a;i<=b;i++)
        {
            System.out.println(n+" x "+i+" = "+(n*i));
        }

    }
}