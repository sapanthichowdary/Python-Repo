import java.util.Scanner;
public class Inches
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        double cm = n*2.54;
        System.out.printf("%.2f",cm);
    }
}