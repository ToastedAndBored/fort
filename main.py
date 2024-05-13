"""
+ - сложить
: - новое слово
; - конец нового слова
+3 - 2
+2 - 7
+5 - 13

стек данных :
стек вызовов:


: +3 3 + ; : +2 2 + ; : +5 +3 +2 ; 1 +5 0
0 1  2 3 4 5 6  7 8 9 1 1  1  1  1 1 1  1
                      0 2  3  4  5 6 7  8


def new(p, prog):
	pass


[]

stackA.append(1)

a = stackA[-1]
stackA = stackA[:-1]


["" , "", "", ""]

{
	"+": plus,
	"+3": 2,
}
"""
def word2value(word):
	if word.isnumeric():
		return int(word)
	try:
		return float(word)
	except:
		pass
	return word

class Interpretter:
	def __init__(self, prg):
		self.prog = prg
		self.pointer = 0
		self.stackL = [] #стек данных
		self.stackR = [] #стек вызова
		self.dic = {}
	#If definition is int => pointer; If definition is function => call function 
	def define(self, name, definition): 
		self.dic[name] = definition
	def step(self):
		if self.pointer>= len(self.prog):
			return False
		word = self.prog[self.pointer]
		if word not in self.dic:
			self.stackL.append(word2value(word))
			self.pointer += 1
		else:
			if isinstance(self.dic[word],int):
				self.stackR.append(self.pointer+1)
				self.pointer = self.dic[word]
			else:
				self.dic[word](self)
				self.pointer+=1
		return True


def plus(inter):
	a = inter.stackL[-1]
	b = inter.stackL[-2]
	inter.stackL = inter.stackL[:-2]
	inter.stackL.append(a+b)





inp = Interpretter(["3.5", "2", "+"])

inp.define("+",plus)

while inp.step():
	print("Данные",inp.stackL)
	print("Вызов",inp.stackR)