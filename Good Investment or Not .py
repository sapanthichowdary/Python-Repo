import java.util.Scanner;
public class Investement
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int x,y;
        x=sc.nextInt();
        y=sc.nextInt();
        if (x>=y*2)
        {
            System.out.println("YES");
        }
        else
        {
            System.out.println("NO");
        }
    }
}