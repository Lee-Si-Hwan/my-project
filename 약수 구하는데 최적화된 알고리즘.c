#include <stdio.h>


int main()
{	
	long long int a, num = 0;
	int i;
	
	scanf("%lld", &a);
	
	for (i = 1 ; i * i < a; i++){
		if (a%i == 0){
			num += 2;
		}

	}
	
	if (i * i == a)
		num++;
		
	printf("%lld", num);

    return 0;
}
