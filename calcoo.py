import sys

def main():
    pass

class CalculadoraPadre: 
	def sumar(self):
		return (self.a+self.b)
	def restar(self):
		return (self.a-self.b)
	def introAgmt(self,a,b,op):
		try:
			self.a = int(a)
			self.b = int(b)
			self.op = op
		except ValueError:
			sys.exit("Non numerical parameters");
if __name__ == '__main__':
	Calculadora = CalculadoraPadre();
	Calculadora.introAgmt(sys.argv[1],sys.argv[3],sys.argv[2])
	if Calculadora.op == "sumar" or Calculadora.op =="suma":
		print(Calculadora.sumar())
	if Calculadora.op == "restar" or Calculadora.op =="resta":
		print(Calculadora.restar())

