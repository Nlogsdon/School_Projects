/* Nicholas Logsdon
CIT330
09/14/2019
finding the sum for given values a + b with function 
*/

//program #1
#include <stdio.h>
//function for gathering sum for given integers a and b and ouputting results
void sum(int a, int b){
   int result = a+b;
   printf("The sum is = %d\n", result);
}
/*main body that allows user to input integers a and b 
which then runs above function to find sum and out put results
*/
int main(){
   int a,b;
   printf("Please enter two numbers\n");
   scanf("%i %i",&a,&b);
   sum(a,b);
   
   return 0;
}
/*
after supplying the input "5 2" the output was correct of 7.
*/