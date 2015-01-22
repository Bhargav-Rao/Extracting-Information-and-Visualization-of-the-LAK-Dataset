import os

#x = input("Do you want the output as PDF? 1-Yes:  ")
x = '1'
if (x=='1'):
	os.system("python readCSV.py > output.txt")
	os.system("echo 'Converting to PDF'")
	os.system("python Convert.py output.txt > fo")
	os.system("rm fo")
	os.system("echo 'Conversion over'")
	os.system("mv output.txt.pdf output.pdf")
	os.system("gnome-open ./output.pdf")

