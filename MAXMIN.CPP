<!--- Test the changes in a branch named Akash---->

#include<stdio.h>
#include<conio.h>
#include<math.h>
void main()
{
int a,b,c;
clrscr();
printf("Enter 3 numbers");
scanf("%d%d%d",&a,&b,&c);
if(a>b&&a>c)
{
	if(b>c)
	{
		printf("%d",(a*a+b*b));
	}
	else
	{
		printf("%d",(a*a+c*c));
	}
}
else if(b>a&&b>c)
{
		if(a>c)
	{
		printf("%d",(a*a+b*b));
	}
	else
	{
		printf("%d",(b*b+c*c));
	}
}
else
{
		if(a>b)
	{
		printf("%d",(a*a+c*c));
	}
	else
	{
		printf("%d",(b*b+c*c));
	}
}
getch();
}