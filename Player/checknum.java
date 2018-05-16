import java.util.*;
import java.lang.*;
import java.io.*;

class Ideone
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner sc=new Scanner(System.in);
		int a=sc.nextInt();
		if(a==0)
		{
			System.out.println("Zero");
		}
		else if((a>=1)&&(a<=100000))
		{
			System.out.println("Positive");
		}
		else
		{
			System.out.println("Negative");
		}
	}
}
