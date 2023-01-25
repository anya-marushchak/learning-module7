
class Movies:
    def  __init__ (self, name, production_year, genre, viewership):
        self.name = name
        self.production_year = production_year
        self.genre = genre
        self.viewership = viewership


    #property decorator to calculate viewership
    @propуrty
    def play(self, view = 1):
        self.current_viewership+=view


class Series(Movies):
    def __init__ (self, series_number, season_number, *args,**kwargs):
        self.series_number = series_number
        self.season_number= season_number

        # Variables
        self.current_viewership = 0

    #defining method calculating viewership of series
    def play(self, view = 1):
        self.current_viewership+=view



movie_1 = Movies( name = 'The Brave Heart', production_year ='1995', genre ='Drama', viewership ='780')
movie_2 = Movies( name ='Pride and Prejudice', production_year = '2005','genre':'Melodrama','viewership':'650')
movie_3 = Movies (name = 'Lion The King', production_year='2019',genre='Adventures',viewership='550')
            
series_1 = Series (name='Friends',series_number= input() , season_number = input(), production_year='1992',genre='comedy', viewership='11500')
series_2 = Series (name='Sherlok Holmes', series_number=input(), season_number = input(),production_year='2014',genre='detective', viewership='986')
series_3 = Series (name= 'Qeens gambit', series_number=input(), season_number = input(), production_year='2021', genre='drama', viewership='710') 

collecction = [movie_1, movie_2, movie_3, series_1,series_2,series_3]


    while True:    
        print('''
           ==========MOVIES COLLECTION===========
           1. Display Available Movies
           2. Display Available Series
           3. The most popular movies and series of the day
           4.Exit''' 
        )
        break

        
def get_movies():
    for movie in movies:
        print (movie)       


def get_series():
    for serie in series():
        print (serie)


play(self, view = 1)

get_movies()   

get_series()  
        
main_collection()