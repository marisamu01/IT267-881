class Movie:
    def __init__(self) -> None:
        self._title = None
        self._year = None
        self._genre = None

    def add_movie(self,title:str,year:int,genre:str):
        self.title = title
        self.year = year
        self.genre = genre
   
    def _getmovie_detail(self):
        print(f"Title : {self.title}")
        print(f"Year : {self.year}")
        print(f"Genre : {self.genre}")

class Documentary(Movie):
   
    def add_channel(self,channel):
        self.channel =  channel
   
    def print_detail(self):
        super()._getmovie_detail()
        Movie()._getmovie_detail(self)
        print(f"channel = {self.channel}")
       
if __name__== '__main__':
    m1 = Documentary()
    m1.add_movie("My Octopus Teacher",2020,"Documentaty")
    m1.add_channel('NetFlix')
    m1._getmovie_detail()

