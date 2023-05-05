class Gatto:
    specie = "felix_domesticus"

    def __init__(self, private, n="kitty"):
        self.nome = n
        self.__nick = private

    # def getNick(self):
    #     return f"My Nick is: {self.__nick}"
    #
    # def setNick(self, newNick):
    #     self.__nick = newNick


tom = Gatto(n="Tom", private="t")
felix = Gatto(n="Felix", private="f")
print(tom.nome)
print(felix.nome)
print(Gatto.specie, ' - ', tom.specie, ' - ', felix.specie)
# print(tom.__nick, ' - ', felix.__nick)  # NO
# print(tom.getNick(), ' - ', felix.getNick())
# tom.__nick = "T!"  # NO
# tom.setNick("T!")
# print(tom.getNick())
print(tom._Gatto__nick)
tom._Gatto__nick = "T!!!"
print(tom._Gatto__nick)



