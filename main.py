def main():
   state = "Practica els problemes de list comprehensions per a ser més Pythonic!"

   espai =  [i for i in state if i in ' ']
   print(len(espai))
if __name__ == '__main__':
   main()

