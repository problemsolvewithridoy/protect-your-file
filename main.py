import pikepdf

old_PDF = pikepdf.Pdf.open("yourpdf.pdf")

allow_key = pikepdf.Permissions(extract=False)
old_PDF.save("bd.pdf", encryption = pikepdf.Encryption(user= "aaZ$",
                                                         owner= "Problem solve with Ridoy",
                                                         allow= allow_key ))
print("new PDF created successfuly with password")