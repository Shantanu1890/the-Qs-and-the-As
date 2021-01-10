// Code Author : Pranav Viswanathan
#include <stdio.h>
#include <stdlib.h>

int main()
{
  int max =5;
  int arr[max], sum = 0, average = 0;

  printf("Enter the number of accidents : \n");

  for (int i = 0; i < max; i++) {
    scanf("\n%d", &arr[i]);
    sum += arr[i];
  }

  average = sum / max;

  printf("\nAverage : %d\n", average);
  
  for(int i = 0; i < max; i ++) {
    printf("Day %d : %d\n", i + 1, abs(average - arr[i]));
  }

  return 0;
}
