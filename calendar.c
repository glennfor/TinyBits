
#include <stdio.h>

int main(){
	
	int year;
	printf("|=|PSEUDO CALENDAR|=|\n\n");
	
	do{
		printf("Enter a year[range 0-32000]: ");
		scanf("%d", &year);
	}while(year<0 || year > 32000);
	
	int isLeapYear = ((year%100!=0 && year%4==0)||((year%100==0 && year%4==0) && year%400!=0));
	
	//index wise days per month: 0-jan, 1-feb, ..., 11-dec
	int monthDays[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30,31};
	
	//set days in feb  to 29 if leap years
	if(isLeapYear)monthDays[1] = 29;
	
	char* months[] = {"January", "February", "March", "April",
			  "May", "June", "July", "August",
			   "September", "October", "November", "December"
			 };
					
	char overhead[] =
	 "\nSun Mon Teu Wed Thu Fri Sat\n"
	   "--- --- --- --- --- --- ---";
	   
	printf("\n\nMonths of the year %d", year);
	int i, j;
	int printStartPoint = 0;
	
	for(i= 0; i < 12; i++)
	{
		
		printf("\n\nMonth of [%s]\n", months[i]);
		printf("%s\n", overhead);
		
		for(j = 1; j <= printStartPoint; j++)
			printf("    ");
			
		for(j = 1; j<=monthDays[i]; j++)
		{
			printf("%-3d ", j);
			printStartPoint = (printStartPoint+1)%8;
			
			if(printStartPoint==7)
			{
				printStartPoint = 0;
				printf("\n");
			}
		}
	}					
}
