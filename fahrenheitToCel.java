import java.util.Scanner;
public class fahrenheitToCel {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        //initalize celsius and fahrenheit variables
        double fahrenheit;
        
        //prompt user for Celsius
        System.out.print("Please enter celsius ");
        double celsius = input.nextDouble();
        
        fahrenheit = (9.0 / 5) * celsius + 32;
        
        System.out.println("\n" + celsius + " is " + fahrenheit + " degrees fahrenheit");
    }
}