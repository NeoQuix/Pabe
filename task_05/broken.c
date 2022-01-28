#include <stdbool.h> // For bool Type (is not standard in C)
#include <stdio.h> // For printf
#include <string.h> // For strncpy

#define BUFFER_SIZE 64 // Defines BUFFER_SIZE as 64 ("Präprozessor")

/*	
	Defined the Functions before filling them with Code 
	Looks cleaner :-)
*/
void check_passed();
void check_failed();
void (*check_functions[2]) (int); // return = void; one argument: int; saves two Function Pointers
bool check_input(char *input);

int main(int argc, char *argv[]){ //should be an Array of String ==> Double Pointer (Strings in C = Array of Chars)
	if (argc != 2){
		puts("Please provide an argument!");
		return 1;
	}

	char buffer[BUFFER_SIZE] = {0}; //missing ; added

	strncpy(buffer, argv[1], BUFFER_SIZE - 1); // missing string.h added on the Top

	printf("your input: %s\n", buffer); //missing stdio.h added on the Top
	
	if (check_input(buffer)){
		return 1;
	}
	else{
		return 0;
	}
}

void check_passed(){ //nothing to do here, Functions just prints two Lines on STDOUT
	puts("check passed!");
	puts("the secret is 'PABE is fun' ;)");
}

void check_failed(){ //nothing to do here, Functions just prints two Lines on STDOUT
	puts("check failed!");
	puts("try again ;)");
}

void (*check_functions[2]) (int) = {check_passed, check_failed}; // here the function gets filled with two Function Pointers

bool check_input(char *input){
	if (!strncmp(input, "PABE", strlen("PABE"))) // added ! because if input == Pabe strncmp will return 0, so the if statement would be false
	{
		check_functions[0](69); //missing argument (Integer ~the function check_functions does not care what the integer is; -69 because Nice)
		return true;
	}
	else
	{
		check_functions[1](420); //missing argument (Integer ~the function check_functions does not care what the integer is; 420 because reasons)
		return false;
	}
}