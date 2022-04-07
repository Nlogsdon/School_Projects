/* Nicholas Logsdon
CIT 330
09/14/19
Finding area of circle for a given radius using functions
*/
#include <stdio.h>
#define PI 3.14159
//function that will calculate area for given radius and output result
void circleArea(int radius){
   double area = PI * radius * radius;
   printf("the area of the circle is %lf\n", area);
}
// main body to prompt for radius, take radius input, and run above function.  
int main(){
   int radius;
   printf("Please enter the radius\n");
   scanf("%d", &radius);
   //function call for previously established function.
   circleArea(radius);
      
   return 0;
}