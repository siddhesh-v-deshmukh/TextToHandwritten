from PIL import Image, ImageDraw, ImageFont
from fpdf import FPDF
import numpy as np
import textwrap

# Input handling module

file_path = input("Please enter path to your .txt file: ").strip()
try:
    with open(file_path, 'r') as file:
        text = file.read()
        print("File Content:")
except FileNotFoundError:
    print("File not found. Please check the path and ensure the file exists.")
except PermissionError:
    print("Permission denied. Ensure you have read access to the file.")
except Exception as e:
    print(f"An error occurred: {e}")

# Render Handwritten Text

# Define Canvas Dimension
canvas_width,canvas_height=800,1200
margin=50
max_width=canvas_width-2*margin
line_spacing = 50

# Load Your Font
font1=ImageFont.truetype('Letters for Learners.ttf',35)
font2=ImageFont.truetype('Power Calm.otf',20)


# Wrap text to fit the specified width
wrapped_text = textwrap.wrap(text, width=60)  # Adjust width for the text block

# variable to track page and y-margin
page_number=1
y=margin

# List to store pages

pages=[]

# Loop through lines and create pages

page = Image.new("RGB", (canvas_width, canvas_height), "white")  # First page
draw = ImageDraw.Draw(page)

for line in wrapped_text:
    draw.text(
        (canvas_width - 200, canvas_height - 40),  # Bottom-right corner
        "designed by siddhu", font=font2, fill="gray"
    )
    if y+line_spacing>canvas_height-margin:
        pages.append(page)
        page_number+=1
        page = Image.new("RGB", (canvas_width, canvas_height), "white")  # First page
        draw = ImageDraw.Draw(page)
        y=margin
    # Draw text on the current page
    draw.text((margin, y), line, font=font1, fill="black")
    y += line_spacing

# save the pages
pages.append(page)

# Save pages as PNGs

pdf_path="Output.pdf"
pages[0].save(pdf_path,save_all=True,append_images=pages[1:],resolution=100.0)


# Save or display the result
print(f'Pdf created successfully: {pdf_path}')








