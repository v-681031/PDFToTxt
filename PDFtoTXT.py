trash = 'AppendixSustainable GovernanceOur Focuses and Progress Ethical ManagementInnovation and Service Responsible Supply ChainGreen Manufacturing Common GoodOur BusinessInclusive Workplace'
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
textBuffer =''
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
	textBuffer = pageObj.extractText()
	if '\n' in textBuffer:
		textBuffer = textBuffer.replace('\n', ' ')
	if trash in textBuffer:
		textBuffer = textBuffer.replace(trash, ' ')
	text += textBuffer
	textBuffer = ''
	count +=1
file = open('tsmcCSR.txt', 'w')#write mode 
file.write(text) 
file.close()


count = 0
text = ''
textBuffer =''
data = []
max_count = 0
max_count_word = None
total_word_count = 0 
count = 0
length = 0
Total_length = 0
while count < num_pages:
	pageObj = pdfReader.getPage(count)
	text += pageObj.extractText()
	count +=1
file1 = open('tsmcCSR1.txt', 'w')#write mode 
file1.write(text) 
file1.close()

data = []
text = ''
with open('tsmcCSR1.txt', 'r') as f:
	for line in f:
		data.append(line.strip('\n'))
	for d in data:
		text += d 
file1 = open('tsmcCSR1-1.txt', 'w')#write mode 
file1.write(text) 
file1.close()


data = []
with open('tsmcCSR.txt', 'r') as f:
	for line in f:
		data.append(line.strip())
	
words_dict = {}

for d in data:
	words = d.split()
	for word in words:
		if word in words_dict:
			words_dict[word] += 1
		else:
			words_dict[word] = 1
		total_word_count += 1

for word in words_dict:
	if words_dict[word] > 100000000000:
		print(word, ' ', words_dict[word])
	if words_dict[word] > max_count:
		max_count = words_dict[word]
		max_count_word = word			
print('maximun wording is "',max_count_word, '" by ', max_count, ' times!')
print('Total words count =', total_word_count)

while True:
	i = input('input a word! or Q123 to quit ')
	if i == 'Q123':
		break
	elif i in words_dict:
		print(i, ' is in words_dict for', words_dict[i], ' times')
	else:
		print(i, ' is not in words_dict!')