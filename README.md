
# Protect your file using python

Protect your PDF file using Python is a project aimed at securing sensitive information contained in PDF files by adding password protection. The program uses the PyPDF2 module to encrypt and password-protect the PDF files. This Python script allows users to enter the password and the path to the PDF file, and then creates a new PDF file with the same name and path, but with password protection.

The program uses the RC4 encryption algorithm, which is a stream cipher encryption algorithm known for its simplicity and speed. The password is first hashed using the MD5 hash function, and then used as the key to encrypt the PDF file.

This project is useful for individuals and organizations that need to secure their confidential PDF files, such as financial reports, legal documents, or personal information. With this Python script, users can easily add password protection to their PDF files and prevent unauthorized access.

let's start...............

To make this project you need to follow this step:-










## Installation

Install package with pip

```bash
  pip install pikepdf

```
    
## Deployment

To deploy this project run

```bash
import pikepdf

old_PDF = pikepdf.Pdf.open("yourOldPDFname.pdf")

allow_key = pikepdf.Permissions(extract=False)

old_PDF.save("yourNewPDFname.pdf", encryption = pikepdf.Encryption(user= "yourPassword", owner= "Problem solve with Ridoy", allow= allow_key ))

print("new PDF created successfuly with password")
```


## Output



![protect your file](https://user-images.githubusercontent.com/123636419/220564806-dbd0f8d4-c97c-4fa0-b8f1-23b1bdb157e5.png)



## You can follow me

Facebook:- https://www.facebook.com/problemsolvewithridoy/

Linkedin:- https://www.linkedin.com/in/ridoyhossain/

YouTube:- https://www.youtube.com/@problemsolvewithridoy

Gmail:- entridoy2@gmail.com

If you have any confusion, please feel free to contact me. Thank you

