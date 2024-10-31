import java.util.Scanner;
public class Hpotenuse
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int x,y;
        x=sc.nextInt();
        y=sc.nextInt();
        double sq = Math.sqrt((x*x)+(y*y));
        System.out.printf("%.2f",sq);
    }
}