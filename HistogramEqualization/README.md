# Image Contrast Enhancement using Histogram Equalization (from Scratch)
Spring 2022
[![Made with Python](https://img.shields.io/badge/Made%20with-Python-blue.svg)](https://www.python.org/)

This project utilizes multimedia science and the power of histogram equalization to enhance the contrast of digital images. By applying this method, we aim to increase the overall contrast of the images and distribute repeating colors more evenly, resulting in visually appealing and vibrant images. This technique works particularly well for images with a more compact and limited color range.

## Algorithm Overview

1. **Read the Image and Save Pixel Colors**: The first step is to read the image and extract the colors of each pixel. This provides the initial data for the contrast enhancement process.

2. **Create a Histogram**: Next, we create a histogram to analyze the distribution of pixel intensities in the image. This histogram provides insights into the current contrast and helps us identify areas for improvement.

4. **Calculate the Cumulative Sum**: Using the histogram, we calculate the cumulative sum of pixel intensities. This step allows us to determine the desired mapping function for contrast enhancement.

5. **Create a Map**: Based on the cumulative sum, we create a mapping function that maps the original pixel intensities to their enhanced counterparts. This mapping ensures a more even distribution of colors throughout the image. In order to better distribute colors with different number of occurrences, it is necessary to map each color to its rounded sum normalized value.

6. **Apply the Mapping and Save the Final Image**: Finally, we apply the mapping function to each pixel in the image, effectively increasing the contrast. The resulting image is then saved, showcasing the enhanced visual appeal.
## Example

**Original Image**
 <br> <img align="center" alt="Original Image" width="80%" src="https://github.com/negarK2000/Multimedia/blob/master/HistogramEqualization/image.png" /> <br>

**Equalized Image**
 <br> <img align="cnter" alt="Equalized Image" width="80%" src="https://github.com/negarK2000/Multimedia/blob/master/HistogramEqualization/EqualizedImage.png" /> <br>

![Original Histogram](https://github.com/negarK2000/Multimedia/blob/master/HistogramEqualization/original_histogram.jpg)
![Original Image Cumulative Summation](https://github.com/negarK2000/Multimedia/blob/master/HistogramEqualization/transfer_func.jpg)

![Equalized Histogram](https://github.com/negarK2000/Multimedia/blob/master/HistogramEqualization/equalized_histogram.jpg)
![Equalized Image Cumulative Summation](https://github.com/negarK2000/Multimedia/blob/master/HistogramEqualization/sum.jpg)
 <br> <img align="cnter" alt="Result" width="50%" src="https://github.com/negarK2000/Multimedia/blob/master/HistogramEqualization/res.png" /> <br>

## Acknowledgments:

I would like to express my gratitude to the Teaching Assistants (TAs) of the Multimedia course who inspired and guided me in the development of this project.
