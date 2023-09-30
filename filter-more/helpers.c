#include "helpers.h"
#include <math.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct
{
    int rgbtBlue;
    int rgbtGreen;
    int rgbtRed;
} __attribute__((__packed__)) RGBTRIPLE1;

void swap(RGBTRIPLE *image1, RGBTRIPLE *image2);
void addtoaverage(RGBTRIPLE image, RGBTRIPLE1 *ave, int *count, int8_t gxy);
void replaceimage(RGBTRIPLE *image, RGBTRIPLE1 *ave, int count);
void sobel(int height, int width, RGBTRIPLE1 imagex[height][width], RGBTRIPLE1 imagey[height][width],
           RGBTRIPLE image[height][width]);

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    int average;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // calculate average RGB
            average = round((image[i][j].rgbtRed + image[i][j].rgbtBlue + image[i][j].rgbtGreen) / 3.0);
            // set all colours to average
            image[i][j].rgbtRed = average;
            image[i][j].rgbtBlue = average;
            image[i][j].rgbtGreen = average;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    // half width making sure to round down
    uint16_t halfwidth = (width + 1) / 2;
    // loop for every pixel
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < halfwidth; j++)
        {
            swap(&image[i][j], &image[i][width - j - 1]);
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // placeholder pixels & counts
    RGBTRIPLE1(*ave)[width] = calloc(height, sizeof(RGBTRIPLE1) * width);
    int(*count)[width] = calloc(height, sizeof(int) * width);

    // check for too much memory
    if (ave == NULL || count == NULL)
    {
        // does not check50 unless 2
        exit(2);
    }

    // initialise values to prevent garbage memory
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            ave[i][j].rgbtRed = 0;
            ave[i][j].rgbtGreen = 0;
            ave[i][j].rgbtBlue = 0;
            count[i][j] = 0;
        }
    }
    // for every pixel in image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // calculate average of surrounding pixels
            for (int k = -1; k < 2; k++)
            {
                // check if current pixel is off the edge
                if (i + k < 0 || i + k > height - 1)
                    continue;
                for (int l = -1; l < 2; l++)
                {
                    if (j + l < 0 || j + l > width - 1)
                        continue;
                    else
                        addtoaverage(image[i + k][j + l], &ave[i][j], &count[i][j], 1);
                }
            }
        }
    }

    // calculate average of every pixel and assign to original image address
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            replaceimage(&image[i][j], &ave[i][j], count[i][j]);
        }
    }
    free(ave);
    free(count);
    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    // new images placeholder for changed values
    RGBTRIPLE1(*newimagex)[width] = calloc(height, width * sizeof(RGBTRIPLE1));
    RGBTRIPLE1(*newimagey)[width] = calloc(height, width * sizeof(RGBTRIPLE1));

    // check for enough memory
    if (newimagex == NULL || newimagey == NULL)
    {
        // does not check50 until 2
        exit(2);
    }
    // initialise values of placeholders - not needed with calloc?
    // for (int i = 0; i < height; i++)
    //{
    //     for (int j = 0; j < width; j++)
    //     {
    //         newimagex[i][j].rgbtRed = 0;
    //         newimagex[i][j].rgbtGreen = 0;
    //         newimagex[i][j].rgbtBlue = 0;
    //       newimagey[i][j].rgbtRed = 0;
    //        newimagey[i][j].rgbtGreen = 0;
    //         newimagey[i][j].rgbtBlue = 0;
    //     }
    // }

    // make black pixel for beyond edgy & initialise values
    RGBTRIPLE black;
    black.rgbtRed = 0;
    black.rgbtGreen = 0;
    black.rgbtBlue = 0;

    // make array for G(x) & G(y)
    const int8_t gx[9] = {-1, 0, 1, -2, 0, 2, -1, 0, 1};
    const int8_t gy[9] = {-1, -2, -1, 0, 0, 0, 1, 2, 1};

    // loop for every pixel
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // counter for place in gx & gy
            int counterx = 0;
            int countery = 0;

            // loop for adjacent pixels
            for (int k = -1; k < 2; k++)
            {
                for (int l = -1; l < 2; l++)
                {
                    // if beyond edgy --> substitute black, otherwise --> use original image
                    if (i + k < 0 || i + k > height - 1 || j + l < 0 || j + l > width - 1)
                    {
                        // add gx and gy modified values to corresponding placeholders
                        addtoaverage(black, &newimagex[i][j], &counterx, gx[counterx]);
                        addtoaverage(black, &newimagey[i][j], &countery, gy[countery]);
                    }
                    else
                    {
                        // add gx and gy modified values to corresponding placeholders
                        addtoaverage(image[i + k][j + l], &newimagex[i][j], &counterx, gx[counterx]);
                        addtoaverage(image[i + k][j + l], &newimagey[i][j], &countery, gy[countery]);
                    }
                }
            }
        }
    }

    // combine gx and gy values through formula and store into newimage x
    sobel(height, width, newimagex, newimagey, image);

    free(newimagex);
    free(newimagey);
    return;
}

void swap(RGBTRIPLE *image1, RGBTRIPLE *image2)
{
    RGBTRIPLE temp;

    temp.rgbtGreen = image1->rgbtGreen;
    temp.rgbtRed = image1->rgbtRed;
    temp.rgbtBlue = image1->rgbtBlue;

    image1->rgbtRed = image2->rgbtRed;
    image1->rgbtBlue = image2->rgbtBlue;
    image1->rgbtGreen = image2->rgbtGreen;

    image2->rgbtRed = temp.rgbtRed;
    image2->rgbtBlue = temp.rgbtBlue;
    image2->rgbtGreen = temp.rgbtGreen;

    return;
}

void addtoaverage(RGBTRIPLE image, RGBTRIPLE1 *ave, int *count, int8_t gxy)
{
    ave->rgbtRed += (image.rgbtRed * gxy);
    ave->rgbtBlue += (image.rgbtBlue * gxy);
    ave->rgbtGreen += (image.rgbtGreen * gxy);
    *count = *count + 1;
    return;
}

void replaceimage(RGBTRIPLE *image, RGBTRIPLE1 *ave, int count)
{
    image->rgbtRed = round((float) ave->rgbtRed / count);
    image->rgbtGreen = round((float) ave->rgbtGreen / count);
    image->rgbtBlue = round((float) ave->rgbtBlue / count);
    return;
}

void sobel(int height, int width, RGBTRIPLE1 imagex[height][width], RGBTRIPLE1 imagey[height][width],
           RGBTRIPLE image[height][width])
{
    // loops for every pixel
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // replace imagex according to sobel operator
            imagex[i][j].rgbtRed = round(sqrt(pow(imagex[i][j].rgbtRed, 2.0) + pow(imagey[i][j].rgbtRed, 2)));
            imagex[i][j].rgbtGreen = round(sqrt(pow(imagex[i][j].rgbtGreen, 2.0) + pow(imagey[i][j].rgbtGreen, 2)));
            imagex[i][j].rgbtBlue = round(sqrt(pow(imagex[i][j].rgbtBlue, 2.0) + pow(imagey[i][j].rgbtBlue, 2)));

            // make sure values are between 0 and 255
            if (imagex[i][j].rgbtRed < 0)
                imagex[i][j].rgbtRed = 0;
            else if (imagex[i][j].rgbtRed > 255)
                imagex[i][j].rgbtRed = 255;
            if (imagex[i][j].rgbtGreen < 0)
                imagex[i][j].rgbtGreen = 0;
            else if (imagex[i][j].rgbtGreen > 255)
                imagex[i][j].rgbtGreen = 255;
            if (imagex[i][j].rgbtBlue < 0)
                imagex[i][j].rgbtBlue = 0;
            else if (imagex[i][j].rgbtBlue > 255)
                imagex[i][j].rgbtBlue = 255;

            // replace into original image
            replaceimage(&image[i][j], &imagex[i][j], 1);
        }
    }
    return;
}