file1 = open('train.char.bmes','r')
file2 = open('dev.char.bmes','r')
file3 = open('test.char.bmes','r')

file4 = open('train','w')
file5 = open('dev','w')
file6 = open('test','w')

sentences = []
sen = []

for line in file1.readlines():
	if line.strip() !='':
		sen.append(line.strip().split()[0])
	else:
		sentences.append(sen)
		sen = []
for i in sentences:
	file4.write(''.join(i)+'\n')
sentences = []
sen = []

for line in file2.readlines():
	if line.strip() !='':
		sen.append(line.strip().split()[0])
	else:
		sentences.append(sen)
		sen = []
for i in sentences:
	file5.write(''.join(i)+'\n')
sentences = []
sen = []

for line in file3.readlines():
	if line.strip() !='':
		sen.append(line.strip().split()[0])
	else:
		sentences.append(sen)
		sen = []
for i in sentences:
	file6.write(''.join(i)+'\n')
sentences = []
sen = []
