
# Protect your file using python

In this project, you will protect your file just write a 3 line of code.
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

