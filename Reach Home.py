import java.util.Scanner;
public class Petrol
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        int x,y;
        x=sc.nextInt();
        y=sc.nextInt();
        if(x*5>=y)
        {
            System.out.println("YES");
        }
        else
        {
            System.out.println("NO");
        }
    }
}