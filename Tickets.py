import java.util.Scanner;
public class Concert
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int x;
        x=sc.nextInt();
        if(x*4<=1000)
        {
            System.out.println("YES");
        }
        else
        {
            System.out.println("NO");
        }
    }
}