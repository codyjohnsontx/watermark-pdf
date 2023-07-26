from PyPDF2 import PdfFileReader, PdfFileWriter

# Read the watermark
watermark_pdf = "wtr.pdf"
watermark = PdfFileReader(watermark_pdf)

# Read the source PDF
source_pdf = "super.pdf"
reader = PdfFileReader(source_pdf)

# Create a new PDF writer
writer = PdfFileWriter()

# Loop through all pages of the source PDF
for i in range(reader.getNumPages()):
    # Get the page from the source PDF
    page = reader.getPage(i)

    # Merge the watermark with the current page
    page.mergePage(watermark.getPage(0))

    # Add the modified page to the writer
    writer.addPage(page)

# Finally, write the new document with watermarks on every page
output_pdf = "watermarked_output.pdf"
with open(output_pdf, "wb") as output_pdf:
    writer.write(output_pdf)
