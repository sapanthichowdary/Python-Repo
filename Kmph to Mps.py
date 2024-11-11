import java.util.Scanner;
public class Kilometers
{
    public static void main(String[] args)
    {
        Scanner sc =new Scanner(System.in);
        int n = sc.nextInt();
        double m = n*0.27777778;
        System.out.printf("%.2f",m);
    }
}