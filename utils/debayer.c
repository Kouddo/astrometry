#include<stdio.h> 

int square(int image, int num_rows, int num_cols){

	/*int num_rows = sizeof(image) / sizeof(image[0]);
	int num_cols = sizeof(image[0]) / sizeof(image[0][0]); */
	
	int r = image;
	int g = image;
	int b = image;

	for(int i = 1; i!= num_rows; i++){
		for(int n = 1; n != num_cols; n++){
			
			
		}
	}
}

int * c_sum(const int * image, int num_rows, int num_cols){
	int r = image;
	int g = image;
	int b = image;

	for(int i = 1; i!= num_rows; i++){
		for(int n = 1; n != num_cols; n++){
			if(i%2 != 0 && n%2 != 0){
				g[i][n] = (image[i-1][n] + image[i+1][n] + image[i][n-1] + image[i][n-1])/4;
                r[i][n] = (image[i-1][n-1] + image[i+1][n-1] + image[i-1][n+1] + image[i+1][n+1])/4;



			}
		}
	}

}