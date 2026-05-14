import fitz


def txt_to_pdf(position, text):
    doc = fitz.open()
    page = doc.new_page()
    page.insert_text(position, text)
    doc.save("final_doc.pdf")
    doc.close()
