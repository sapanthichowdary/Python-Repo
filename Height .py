import java.util.Scanner;
public class Height
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int x,y;
        x=sc.nextInt();
        y=sc.nextInt();
        if(x>y)
        {
            System.out.println(x);
        }
        else
        {
            System.out.println(y);
        }
    }
}