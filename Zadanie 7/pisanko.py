class Txt():

    def __init__(self, druzyna, druzyn):
        self.druzyna = druzyna
        self.druzyn = druzyn
        

    def Plik(self):
        f = open("Kluby.txt", "w")
        f.write(self.druzyna + "\n")
        f.write(self.druzyn + "\n")
        f.close()
    