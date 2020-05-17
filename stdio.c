#include <stdio.h>

void func(const char* s) {
	s++;
}

int main() {
	char* hello  = "hello";
	func(hello);
	printf("%s", hello)
}