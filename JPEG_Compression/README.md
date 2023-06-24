# JPEG Image Compression from Scratch

Spring 2022

[![Made with Python](https://img.shields.io/badge/Made%20with-Python-blue.svg)](https://www.python.org/)

Welcome to JPEG Image Compression, a powerful lossy compression algorithm designed specifically for the human eye. This project aims to optimize image storage while maintaining visual accuracy by leveraging three key features:

1. **Space Redundancy**: Images often contain slowly changing and repeated information, leading to redundant data that can be efficiently compressed.
2. **Frequency Sensitivity**: The human eye is less sensitive to the loss of high frequency components compared to low frequency components. By prioritizing preservation of important visual details, our algorithm achieves high compression ratios without significant loss in perceived image quality.
3. **Color Accuracy**: Our algorithm capitalizes on the fact that human vision excels at distinguishing between black and white, allowing us to allocate resources more efficiently in the compression process.

## JPEG Compression Algorithm Overview

Our JPEG Compression Algorithm follows a series of steps to reduce image size while maintaining visual fidelity:

1. **Image Conversion**: We convert the image from the RGB format to the YCbCr format, enabling efficient processing and compression. We employ chroma subsampling using a 4:2:0 ratio for optimal results.

2. **Discrete Cosine Transform**: The image data is divided into 8x8 blocks, which undergo a mathematical transformation called Discrete Cosine Transform. This step captures and represents frequency information within each block.

3. **Quantization**: After the transformation, we apply quantization to further reduce data redundancy. By discarding less visually significant information, we achieve higher compression ratios without perceptible loss.

4. **Huffman Coding**: We implement the Huffman Coding Algorithm from scratch to efficiently encode the transformed image data. Huffman coding assigns shorter codes to frequently occurring data patterns, enabling more compact representation.

5. **Huffman Coding Applied**: We apply the Huffman coding technique to the transformed image coefficients, reducing their overall size while preserving crucial visual information.

6. **Saving the Encoded Image**: Finally, we save the compressed file.

## Acknowledgments

I would like to express my gratitude to the Teaching Assistants (TAs) of the Multimedia course who provided invaluable inspiration and guidance throughout the development of this project.
