def extract_text(pdf_path):
    doc = pymupdf.open(pdf_path)      # open the PDF
    text = ""
    for page in doc:               # combine text from every page
        text += page.get_text()
    return text

text = extract_text("Placement Policy 2027_B.Tech_MCA.pdf")   # put your PDF path/name here
print(len(text), "characters extracted")
