file1 = open('test_seg','r')
file2 = open('test','r')
file3 = open('test_dataset','w')

sentences = []
for line in file1.readlines():
	sen = line.strip().split()
	sentences.append(sen)

labels = []
for sen in sentences:
	for word in sen:
		if len(word)==1:
			labels.append('S')
		elif len(word) ==2:
			labels.extend(['B','E'])
		else:
			labels.append('B')
			labels.extend(['M']*(len(word)-2))
			labels.append('E')

i = 0
for line in file2.readlines():
	characters = line.strip()
	for char in characters:
		file3.write(char + ' ' + labels[i] + '\n')
		i += 1
	file3.write('\n')