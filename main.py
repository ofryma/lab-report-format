import os
import urllib.request
 
filename = "lab report format"

url = "https://github.com/ofryma/lab-report-format/blob/main/format.docx"
print ("download start!")
filename, headers = urllib.request.urlretrieve(url, filename=f"{filename}.docx")
print ("download complete!")
print ("download file location: ", f"{os.getcwd()}\\{filename}.docx")
    









