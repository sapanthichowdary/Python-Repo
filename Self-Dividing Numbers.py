import java.util.Scanner;
public class Self
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int a,b,i,t,r,f=0;
        a=sc.nextInt();
        b=sc.nextInt();
        for(i=a;i<=b;i++)
        {
            f=0;
            t=i;
            while(t!=0)
            {
                r=t%10;
                if(r==0 || i%r!=0)
                {
                    f=1;
                }
                t=t/10;
            }
            if(f==0)
            {
                System.out.print(i+" ");
            }
        }
    }
}