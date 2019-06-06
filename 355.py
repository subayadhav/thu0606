import java.util.*;
import java.lang.*;
import java.io.*;
class Main
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner sc = new Scanner(System.in);
		String g = sc.nextLine();
		g=g.toLowerCase();
		g=g.replaceAll("\\s+","");
		String s1 = "";
		String s2 = "";
		int count;
		if(g.length()==0){
			System.out.println("invalid");
		}
		else{
		if(g.length()>=1 && g.length()<=100000){
		char[] ch = g.toCharArray();
		for(int i=0;i<ch.length;i++){
			if(s1.indexOf(ch[i])==-1){
				s1+=ch[i];
			}
		}
		char[] c = s1.toCharArray();
		for(int i=0;i<c.length;i++){
			count=0;
			for(int j=0;j<ch.length;j++){
			if(c[i]==ch[j]){
				count++;
			}	
			}
			if(count==1){
				System.out.print(c[i]);
				if(i<c.length-1){
					System.out.print(" ");
				}
			}
		}
		}
		}
	}
}
