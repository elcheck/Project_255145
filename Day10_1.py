class Song:
    def __init__(self, title="", author="", lyrics=(),):
        self.title = title
        self.author = author
        self.lyrics = lyrics
        print(f"New Song made: {self.title} {self.author} {self.lyrics}")
    def sing(self):
        print(self.title)
        print(self.author)
        for line in self.lyrics:
            print(line)
        return(self)
    def yell(self):
        print(self.title)
        print(self.author)
        for line in self.lyrics:
            print(line.upper())
        return (self)
class Rap(Song):
    def break_it(self,max_lines=3,drop='yeah'):
        print(self.title)
        print(self.author)
        for line in self.lyrics[0:max_lines]:
            for word in line.split():
                print(word+" "+drop+" ", end=" ")
            print('')

song1=Song("Ziemeļmeita", "Jumprava", ["Gāju meklēt ziemeļmeitu","Garu, tālu ceļu veicu"])
song1.sing().yell()
rap1=Rap("Ziemeļmeita", "Jumprava", ["Gāju meklēt ziemeļmeitu","Garu, tālu ceļu veicu"])
rap1.break_it()
