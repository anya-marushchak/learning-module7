
class Movies:
    def  __init__ (self, name, production_year, genre, viewership):
        self.name = name
        self.production_year = production_year
        self.genre = genre
        self.viewership = viewership

        # Variables
        self.current_viewership = 0

    #defining method calculating viewership of series
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

    def main_collection():

        movies = Movies( { name = 'The Brave Heart', production_year ='1995', genre ='Drama', viewership ='780'},
            { name ='Pride and Prejudice', production_year = '2005','genre':'Melodrama','viewership':'650'},
            { name = 'Lion The King', 'production_year':'2019','genre':'Adventures','viewership':'550'})
            

    series = [{'name':'Friends','series_number': input() , 'season_number:': input(), 'production_year':'1992','genre':'comedy', 'viewership':'11500'},
              {'name':'Sherlok Holmes', 'series_number:':input(), 'season_number:': input(),'production_year':'2014','genre':'detective', 'viewership':'986'}]
    


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