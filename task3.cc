/*Nicholas Logsdon
CIT 330
09/07/2019
Finding the area of a circle for any user given radius
*/

#include <stdio.h>
#define pi 3.14159   //define pi's value for later in formula 

int  main ()
{
   
   double radius, //this is to establish the variable for our radius
          area;   //this is to establish variable for area which will be calculated
        
   printf("Please enter radius of Circle"); //message prompting for radius
   scanf("%lf", &radius); //user will input radius which will define our variable 
 
   //equation for area based on PI and radius previously established
   area = pi * radius * radius;

   printf("\nThe area of the circle is %f", area); //this will output area calculated
   
   return(0);
}

