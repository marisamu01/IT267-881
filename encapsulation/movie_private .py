class Movie:
    def __init__(self) -> None:
        self.__title = None
        self.__year = None
        self.__genre = None
        self.__rating = 6

    def add_movie(self,title:str,year:int,genre:str,rating=5):
        self.__title = title
        self.__year = year
        self.__genre = genre
        self.__rating = rating
   
    def _getmovie_detail(self):
        print(f"Title : {self.__title}")
        print(f"Year : {self.__year}")
        print(f"Genre : {self.__genre}")
        print(f"Rating : {self.__rating}")

    def print_detail(self):
        self._getmovie_detail()

class Documentary(Movie):
    def __init__(self) -> None:
        Movie().__init__()
   
    def add_channel(self,ch:str):
        self.channel =  ch

    def print_detail(self):
        super().print_detail()
        print(f"channel = {self.channel}")
       

if __name__== '__main__':
    m1 = Documentary()
    m1.add_movie("My Octopus Teacher",2020,"Documentaty")
    m1.add_channel('NetFlix')
    #m1._getmovie_detail()
    #m1._Moving__getmovie_detail()
    m1.print_detail()
   