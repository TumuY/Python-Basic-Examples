class App():
    artists = []
    def __init__(self,name):
        self.name = name

    @classmethod
    def showartists(cls):
        for item in App.artists :
            print("{} -->   {}".format(item.name, item.music))

class Artist():
    def __init__(self,name,musics):
        self.name = name
        self.music = [musics.split(",")]
        App.artists.append(self)

    @classmethod
    def pickmusic(cls, pickmusic, pickartist):
        i,l = 0,0
        for item in App.artists:
            i += 1
            if pickartist == item.name:
                for item in item.music:
                    if pickmusic in item:
                        print("Listening --> {} by {}".format(pickmusic,pickartist))
                        i += 2
                    else:
                        print("Wrong Song")
                        i += 2

            elif i ==3:
                print("Wrong Artist")

# region Data
app1 = App("MusicPlayerApp")
a1 =Artist("Kenny G","Forever In Love,Songbird,The Joy Of Life")
a2 =Artist("The Beatles","Never Let Me Down,Yesterday,Come Together")
a3 =Artist("Pink Floyd","Time,Breathe,Sorrow")
# endregion

if __name__ == "__main__":
    print("Our List: ")
    App.showartists()
    print("\nPlease Choose a Music and Artist")
    Artist.pickmusic(input("Music: "),input("Artist: "))
