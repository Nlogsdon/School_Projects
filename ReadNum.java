//reading a simple number input from the user
import java.util.Scanner;
public class ReadNum {
	public static void main(String[] args) {
		//create scanner object
		Scanner input = new Scanner(System.in);
		//prompt user
		System.out.print("Please enter a number: ");
		//store user input
		double number1 = input.nextDouble();

		//print user input
		System.out.println("Your number is " + number1);
	}
}
