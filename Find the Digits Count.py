import java.util.Scanner;
public class DigitCount
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int sum=0;
        while(n!=0)
        {
           int  r=n%10;
            sum = sum+1;
            n=n/10;
        }
        System.out.println(sum);
    }
}