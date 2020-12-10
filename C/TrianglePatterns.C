// Code Author : Pranav Viswanathan
#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
void invertedTop(int n)
{
    system("cls");
    for(int i = 0; i < n; i++)
   {
       for (int j = 0; j < n; j++)
       {
           if(i + j <= (n - 1))
           {
                printf("*");
           }
           else
           {
               printf(" ");
           }
       }
       printf("\n");
   }
}

void lowerHalf(int n)
{
    system("cls");
    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j < n; j++)
        {
            if(i >= j)
            {
                printf("*");
            }
            else
            {
                printf(" ");
            }
        }
        printf("\n");
    }
}
void lowerRightTriangle (int n)
{
    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j < n; j++)
        {
            if(i + j == (n - 1) || i + j >= n)
            {
                printf("*");
            }
            else
            {
                printf(" ");
            }
        }
        printf("\n");
    }
}
void upperRightTriangle  (int n)
{
    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j < n; j++)
        {
            if(i == j || i <= j)
            {
                printf("*");
            }
            else
            {
                printf(" ");
            }
        }
        printf("\n");
    }
}
int main()
{
   int choice = 0, n = 0;

   printf("Enter the number of rows and columns : ");
   scanf("%d", &n);

   printf("1. Upper upside down\n2. Lower topside up\n3. Lower Right Triangle\n4. Upper Right Triangle \nEnter your choice[1 - 4] :");
   scanf("%d", &choice);

   switch (choice)
   {
    case 1:
       invertedTop(n);
       break;
    case 2:
        lowerHalf(n);
        break;
    case 3:
        lowerRightTriangle(n);
        break;
    case 4:
        upperRightTriangle(n);
        break;
    default:
        printf("Invalid input");
    }
   return 1;
}
