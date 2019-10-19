# importing required modules 
import PyPDF2 
# creating a pdf file object 
pdfFileObj = open('tsmcCSR.pdf', 'rb') 

# creating a pdf reader object 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
# printing number of pages in pdf file 

num_pages = pdfReader.numPages
print(num_pages)
count = 0
text = ''
data = []
max_count = 0
max_count_word = None
total_word_count = 0 
count = 0
length = 0
Total_length = 0
#The while loop will read each page
while count < num_pages:
	pageObj = pdfReader.getPage(count)
	text += pageObj.extractText()
	count +=1
file1 = open('tsmcCSR.txt', 'w')#write mode 
file1.write(text) 
file1.close()

data = []
text = ''
with open('tsmcCSR.txt', 'r') as f:
	for line in f:
		text += str(line.strip())
		
	#for d in data:
	#	text += d 
file1 = open('tsmcCSR1.txt', 'w')#write mode 
file1.write(text) 
file1.close()