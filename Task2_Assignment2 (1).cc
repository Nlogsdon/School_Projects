/* Nicholas Logsdon
CIT 330
09/14/2019
Program for finding integer sum for sums a and b
*/

//program #1
#include <stdio.h>
//function to find sum of two integers and store the result as variable sum 
int sum(int a, int b){
   int sum = a+b;
   return sum;
}
/*body of program prompting for user for input, running the sum function above,
and then outputting the result
*/
int main(){
   int a,b;
   printf("Please enter two number\n");
   scanf("%i %i",&a,&b);
   int result = sum(a,b);
   printf("The sum is = %d\n",result);
   
   return 0;
}
/*
when inputting 5 and 2 just as the first task it returned the result of 7.
This function did less than the first function, this function would only be used
to find and store a sum. the previous program would find a sum and output said
sum.
*/