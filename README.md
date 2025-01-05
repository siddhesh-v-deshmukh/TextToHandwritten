# TextToHandwritten
Handwritten Text Renderer

Project Overview

This project is a Python-based tool that reads text from a user-provided .txt file and generates a multi-page handwritten-style PDF document. The tool wraps text to fit within specified dimensions, applies a custom font for a handwritten aesthetic, and includes an optional watermark on each page.

Features

Input Handling: Reads text from a user-provided .txt file with error handling for file path issues, permissions, and other exceptions.
Handwritten Style Rendering: Uses custom fonts to simulate handwritten text.
Text Wrapping: Automatically wraps text to fit within the defined canvas width.
Pagination: Supports multi-page PDF creation when the text exceeds the space available on a single page.
Custom Fonts: Includes two font styles for primary text and a watermark.
Watermark: Adds a customizable watermark (e.g., "designed by siddhu") at the bottom-right corner of each page.
Output: Saves the rendered content as a multi-page PDF.

Prerequisites

Ensure you have the following installed on your system:
Python 3.7 or higher
Required libraries:
 Pillow
 fpdf
 numpy
 textwrap

Install the required libraries using pip:

pip install pillow fpdf numpy

Usage Instructions

Clone the repository:

git clone [https://github.com/siddhesh-v-deshmukh/TextToHandwritten)
Prepare your .txt file with the content you want to render.

Customization

Fonts: Replace the Letters for Learners.ttf and Power Calm.otf files with your desired fonts. Update the font file paths in the script accordingly.

Text Wrapping: Adjust the width parameter in the textwrap.wrap() function to modify text line length.

Page Dimensions: Change the canvas_width, canvas_height, and margin variables to customize page size and margins.

Watermark: Edit the watermark text and positioning in the draw.text() method inside the script.
