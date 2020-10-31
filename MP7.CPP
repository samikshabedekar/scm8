#include<iostream.h>
#include<conio.h>
#include<string.h>
int getValue(char);
int getAscii(int);
void shiftLeft(int,int,int,int,int);
void shiftRight(int,int,int,int,int);
void main()
{
clrscr();
int c,rl1,rl2,rh1,rh2,rh,rl,n;
int i;
char r[5];
cout<<"Enter number: ";
cin>>r;
rh1 = getValue(r[0]);
rh2 = getValue(r[1]);
rl1 = getValue(r[2]);
rl2 = getValue(r[3]);
cout<<"1) Left Shift\n2) Right Shift";
cout<<"\n";
cin>>c;
cout<<"Enter number of bits: ";
cin>>n;
switch(c)
{
case 1:
shiftLeft(rh1,rh2,rl1,rl2,n);
break;
case 2:
shiftRight(rh1,rh2,rl1,rl2,n);
break;
default:
cout<<"Incorrect Choice!";
}
getch();
}
int getValue(char s)
{
int r1;
r1 = s;
if(r1>=48 && r1<=57)
{
r1 = r1 - 48;
}
if(r1>=65 && r1<=70)
{
r1 = r1 - 55;
}
return r1;
}
int getAscii(int d)
{
if(d<10)
{
d = 48 + d;
}
else
{
d = 55 + d;
}
return d;
}
void shiftLeft(int rh1,int rh2, int rl1,
int rl2,int n)
{
int rh,rl,i;
char o[5];
for(i = 0;i<n;i++)
{
int f1;
f1 = 0;
asm mov ax,rl2;
asm mov cl,1;
asm shl ax,cl;
asm mov rl2,ax;
asm mov ax,rl1;
asm mov cl,1;
asm shl ax,cl;
asm mov rl1,ax;
//cout<<"\nrl1 = "<<rl1;
asm mov ax,rh2;
asm mov cl,1;
asm shl ax,cl;
asm mov rh2,ax;
asm mov ax,rh1;
asm mov cl,1;
asm shl ax,cl;
asm mov rh1,ax;
rh = (16*rh1)+rh2;
rl = (16*rl1)+rl2;
//cout<<"\nrl: "<<rl;
if(rl>=256)
{
rl = rl%16;
//cout<<"\nrl: "<<rl;
rh = rh+1;
}
o[0] = getAscii(rh/16);
o[1] = getAscii(rh%16);
o[2] = getAscii(rl/16);
o[3] = getAscii(rl%16);
}
cout<<"\n";
cout<<"Left Shift:
"<<o[0]<<o[1]<<o[2]<<o[3]<<"H";
}
void shiftRight(int rh1,int rh2, int
rl1, int rl2,int n)
{
int rh,rl,i;
char o[5];
int f1,f2,f3;
for(i=0;i<n;i++)
{
f1 = 0;
f2 = 0;
f3 = 0;
if(rh1%2 == 1)
{
f1 = 1;
}
if(rh2%2 == 1)
{
f2 = 1;
}
if(rl1%2 == 1)
{
f3 = 1;
}
asm mov ax,rh1;
asm mov cl,1;
asm shr ax,cl;
asm mov rh1,ax;
asm mov ax,rh2;
asm mov cl,1;
asm shr ax,cl;
asm mov rh2,ax;
if(f1 == 1)
{
rh2 = rh2 + 8;
}
asm mov ax,rl1;
asm mov cl,1;
asm shr ax,cl;
asm mov rl1,ax;
if(f2 == 1)
{
rl1 = rl1 + 8;
}
asm mov ax,rl2;
asm mov cl,1;
asm shr ax,cl;
asm mov rl2,ax;
if(f3 == 1)
{
rl2 = rl2 + 8;
}
rh = (16*rh1)+rh2;
rl = (16*rl1)+rl2;
}
o[0] = getAscii(rh/16);
o[1] = getAscii(rh%16);
o[2] = getAscii(rl/16);
o[3] = getAscii(rl%16);
cout<<"\n";
cout<<"Right Shift:
"<<o[0]<<o[1]<<o[2]<<o[3]<<"H";
}
