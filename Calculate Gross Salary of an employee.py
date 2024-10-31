import java.util.Scanner;
public class GrossSalary
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        double bs,hra,da;
        bs = sc.nextDouble();
        hra = sc.nextDouble();
        da = sc.nextDouble();
        double pf = 0.12*bs;
        System.out.printf("%.2f\n",pf);
        double gs = bs+hra+da+pf;
        System.out.printf("%.2f",gs);
    }
}