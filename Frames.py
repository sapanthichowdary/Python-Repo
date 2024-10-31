import java.util.Scanner;
public class Rectangle
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int l,b,x;
        l=sc.nextInt();
        b=sc.nextInt();
        x=sc.nextInt();
        int per = 2*(l+b);
        System.out.println(x*per);
    }
}