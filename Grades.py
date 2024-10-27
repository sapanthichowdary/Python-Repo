import java.util.Scanner;
public class Percentage
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int s1,s2,s3,s4,s5;
        s1=sc.nextInt();
        s2=sc.nextInt();
        s3=sc.nextInt();
        s4=sc.nextInt();
        s5=sc.nextInt();
        int per = ((s1+s2+s3+s4+s5)*100)/500;
        if (per>=90)
        {
            System.out.println("Grade A");
        }
        else if(per>=80)
        {
            System.out.println("Grade B");
        }
        else if(per>=70)
        {
            System.out.println("Grade C");
        }
        else if(per>=60)
        {
            System.out.println("Grade D");
        }
        else if(per>=40)
        {
            System.out.println("Grade E");
        }
        else
        {
            System.out.println("Grade F");
        }
    }
}