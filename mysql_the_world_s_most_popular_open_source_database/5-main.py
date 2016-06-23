import mysql.connector

class Show:
    ''' Defines a TV show object '''

    def __init__(self, show_id, show_name):
        ''' Instantiates the class with and sets up lists to manage seasons '''
        self.__id = show_id
        self.__name = show_name
        self.__season_ids = []
        self.__season_list = []

    def __str__(self):
        ''' Responds to string and print calls '''
        return self.__name + ":"

    def add_season(self, season):
        ''' Adds a season to the id list and object list '''
        self.__season_ids.append(season.get_id())
        self.__season_list.append(season)

    def get_season_ids(self):
        ''' Returns list of season ids '''
        return self.__season_ids

    def get_seasons(self):
        ''' Returns list of season objects '''
        return self.__season_list

    def get_id(self):
        ''' Returns the id of the TV show '''
        return self.__id

class Season:
    ''' Defines a Season object '''

    def __init__(self, season_id, season_number, tvshow_id):
        ''' Instantiates class and creates list to manage episodes '''
        self.__id = season_id
        self.__number = season_number
        self.__tvshow_id = tvshow_id
        self.__episode_list = []

    def __str__(self):
        ''' Responds to string and print calls '''
        return "\tSeason " + str(self.__number) + ":"

    def add_episode(self, episode):
        ''' Adds an episode object to the class '''
        self.__episode_list.append(episode)

    def get_id(self):
        ''' Returns the id of the season '''
        return self.__id

    def get_episodes(self):
        ''' Returns the list of episode objects '''
        return self.__episode_list

class Episode:
    ''' Defines an Episode object '''

    def __init__(self, episode_id, episode_name, episode_number, season_id):
        ''' Instantiates an episode object '''
        self.__id = episode_id
        self.__name = episode_name
        self.__number = episode_number
        self.__season_id = season_id

    def __str__(self):
        ''' Responds to string and print calls '''
        return "\t\t" + str(self.__number) + ": " + self.__name

''' Establishes a connection to the SQL server '''
cnx = mysql.connector.connect(user='student',
                              password='aLQQLXGQp2rJ4Wy5',
                              host='173.246.108.142',
                              port='3306',
                              database='Project_169')

''' Creates a list of TV show objects from data in db '''
tvshow_list = []
cursor = cnx.cursor()
tvshow_query = ("SELECT id, name FROM TVShow ORDER BY name ASC")
cursor.execute(tvshow_query)
for (show_id, show_name) in cursor:
    new_show = Show(show_id, show_name)
    tvshow_list.append(new_show)
cursor.close()

''' Associates each season in db to TV show object '''
cursor = cnx.cursor()
season_query = ("SELECT id, number, tvshow_id FROM Season ORDER BY number")
cursor.execute(season_query)
for (season_id, season_number, tvshow_id) in cursor:
    new_season = Season(season_id, season_number, tvshow_id)
    for tvshow in tvshow_list:
        if tvshow_id == tvshow.get_id():
            tvshow.add_season(new_season)
cursor.close()

''' Associates each episode to the season object and TV show object '''
cursor = cnx.cursor()
episode_query = ("SELECT id, name, number, season_id FROM Episode ORDER BY number")
cursor.execute(episode_query)
for (episode_id, episode_name, episode_number, season_id) in cursor:
    new_episode = Episode(episode_id, episode_name, episode_number, season_id)
    for tvshow in tvshow_list:
        if season_id in tvshow.get_season_ids():
            for season in tvshow.get_seasons():
                if season_id == season.get_id():
                    season.add_episode(new_episode)
cursor.close()

''' Closes connect to db '''
cnx.close()

''' Prints each element in the TV show list '''
for tvshow in tvshow_list:
    print tvshow
    for season in tvshow.get_seasons():
        print season
        for episode in season.get_episodes():
            print unicode(episode)
