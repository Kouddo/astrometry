import numpy as np

def simple_debayer(image, pattern = "rggb"):
   
    r = image
    g = image
    b = image

    for i in range(1, len(image)-1):
        for n in range(1, len(image[0])-1):
            if i%2 != 0 and n%2 != 0:
                #indicates it is a blue value
                g[i][n] = (image[i-1][n] + image[i+1][n] + image[i][n-1] + image[i][n-1])/4
                r[i][n] = (image[i-1][n-1] + image[i+1][n-1] + image[i-1][n+1] + image[i+1][n+1])/4

            elif i%2 == 0 and n%2 == 0:
                #indicates it is a red value
                g[i][n] = (image[i-1][n] + image[i+1][n] + image[i][n-1] + image[i][n-1])/4
                b[i][n] = r[i][n] = (image[i-1][n-1] + image[i+1][n-1] + image[i-1][n+1] + image[i+1][n+1])/4
            elif i%2 == 0 and n%2 != 0:
                #indicates it is a green value with red on lef and right and blue up down 
                r[i][n] = (image[i-1][n] + image[i+1][n])/2
                b[i][n] = (image[i][n-1] + image[i][n+1])/2
            else:
                #indicates it is other type of green value
                b[i][n] = (image[i-1][n] + image[i+1][n])/2
                r[i][n] = (image[i][n-1] + image[i][n+1])/2
        




    return [r,g,b]

