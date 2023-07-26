# watermark-PyPDF2 Watermarking Script
Description:
This Python script utilizes the PyPDF2 library to add a watermark to every page of a PDF document. 
It provides a simple and efficient way to overlay a watermark PDF on a source PDF, creating 
a new PDF file with watermarks applied to all pages.

Dependencies:
Python 3.x
PyPDF2 library (pip install PyPDF2)
Usage
Place the source PDF (super.pdf) and the watermark PDF (wtr.pdf) in the same directory as the script.

Run the watermark.py script using Python. The script will read the watermark PDF and apply 
it to every page of the source PDF.

The new PDF file with the watermark applied will be saved as PyPDF2-output.pdf in the same directory.

How It Works:
The script opens the watermark PDF and the source PDF using PyPDF2's PdfFileReader.

It then loops through all the pages of the source PDF using a for loop.

For each page, it extracts the corresponding page from the watermark PDF and merges them 
using mergePage to apply the watermark.

The modified page is added to a new PDF writer using addPage.

Once all the pages have been processed, the script saves the 
new document with watermarks on every page as PyPDF2-output.pdf.

Example:
Suppose we have a source PDF super.pdf with multiple pages and a
watermark PDF wtr.pdf. When we run the script, it will overlay the watermark 
on each page of super.pdf, and the resulting PDF with watermarks will be saved as PyPDF2-output.pdf.

The PyPDF2 library is used for simplicity and straightforward watermarking purposes. 
For more complex PDF operations, other libraries like PyMuPDF or PyPDF4 may be more suitable.


Notes:

Please ensure that both the source PDF and watermark PDF are in the correct directory
with the script before running it.

License:
This project is licensed under the MIT License
