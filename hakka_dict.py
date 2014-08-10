#!/usr/bin/env python
#-*-coding-*-:utf8

source_file = r"C:\Users\XIAO\Desktop\客家词汇.txt"
dest_file = r"C:\Users\XIAO\Desktop\客語字典.csv"
class Dict:
	"""A dictionary class
"""
	def __init__(self, word, chinese, hakka_pinyin, example, translate):
		self.word = word
		self.chinese = chinese
		self.hakka_pinyin = hakka_pinyin
		self.example = example
		self.translate = translate

	def setWord(self, word):
		self.word = word

	def setChinese(self, chinese):
		self.chinese = chinese

fi = open(source_file, encoding="utf-8")
fo = open(dest_file,'w')
c = fi.readlines()
hakka_dict = []
hakka_word = {}
size = 6
for i in range(len(c)//size):
	for line in c[i*size:(i+1)*size]:
		x = line.split("：")
	#	print(x)
	#	if x[0] == u"客語":
	#		hakka_word.append(x[1])
	#	else if x[0] == u"國語":
	#		hakka_word.append(x[1])
		if len(x) == 2:
			hakka_word[x[0]] = x[1].strip()
	#print(hakka_word)
	fo.write(hakka_word['國語']+','+hakka_word['客語']+','+hakka_word['音標']+','+hakka_word['造句']+','+hakka_word['備註']+'\n')
	hakka_dict.append(hakka_word)	#好奇怪，為何hakka_dict列表的元素最終都相同，為最後一個元素？引用？
fi.close()
fo.close()

#for word in hakka_dict:
#	fo.writelines(word['國語']+','+word['客語']+','+word['音標']+','+word['造句']+','+word['備註']+'\n')
#fo.close()
