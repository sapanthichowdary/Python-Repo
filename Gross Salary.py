import java.util.Scanner;
public class GrossSalary
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int bs;
        bs=sc.nextInt();
        double da,hra;
        if(bs<=10000)
        {
            da=bs*0.8;
            hra=bs*0.2;
        }
        else if(bs<=20000)
        {
            da=bs*0.9;
            hra=bs*0.25;
        }
        else{
            da=bs*0.95;
            hra=bs*0.3;
        }
        double gs=bs+da+hra;
        System.out.printf("%.2f",gs);
    }
}