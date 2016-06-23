import time
import BaseHTTPServer
import mysql.connector
import json


class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    ''' Class defines the HTTP request handler '''

    def do_GET(s):
        ''' Function handles incoming get requests '''
        data_id = None
        query_string = None
        path_array = s.path.split('/')

        ''' Determines path and sets data_id and query_string '''
        if len(path_array) == 2 and path_array[1] == 'tvshows':
            data_id = 0
            query_string = ("SELECT id, name, poster "
                            "FROM TVShow "
                            "ORDER BY name ASC")
        elif len(path_array) == 3 and path_array[1] == 'tvshow':
            url_id = path_array[-1]
            data_id = 1
            query_string = ("SELECT TVShow.id, TVShow.name, TVShow.poster, "
                                "TVShow.overview, Network.name, "
                                "GROUP_CONCAT(Genre.name) "
                            "FROM TVShow "
                            "JOIN Network "
                                "ON TVShow.network_id = Network.id "
                            "JOIN TVShowGenre "
                                "ON TVShow.id = TVShowGenre.tvshow_id "
                            "JOIN Genre "
                                "ON TVShowGenre.genre_id = Genre.id "
                            "WHERE TVShow.id = {}".format(url_id))
        elif len(path_array) == 4 and s.path.startswith('/tvshow/') \
            and s.path.endswith('/actors'):
                url_id = path_array[-2]
                data_id = 2
                query_string = ("SELECT Actor.id, Actor.name "
                                "FROM TVShowActor "
                                "JOIN Actor "
                                    "ON TVShowActor.actor_id = Actor.id "
                                "WHERE TVShowActor.tvshow_id = {} "
                                "ORDER BY Actor.name ASC".format(url_id))
        elif len(path_array) == 4 and s.path.startswith('/tvshow/') \
            and s.path.endswith('/seasons'):
                url_id = path_array[-2]
                data_id = 3
                query_string = ("SELECT id, number "
                                "FROM Season "
                                "WHERE Season.tvshow_id = {} "
                                "ORDER BY number ASC".format(url_id))
        elif len(path_array) == 6 and path_array[1] == 'tvshow' \
            and path_array[3] == 'season' and path_array[5] == 'episodes':
                tvshow_id = path_array[2]
                season_id = path_array[4]
                data_id = 4
                query_string = ("SELECT Episode.id, Episode.number, "
                                    "Episode.name "
                                "FROM TVShow "
                                "JOIN Season "
                                    "ON TVShow.id = Season.tvshow_id "
                                "JOIN Episode "
                                    "ON Season.id = Episode.season_id "
                                "WHERE TVShow.id = {} "
                                "AND Season.id = {} "
                                "ORDER BY Episode.number ASC"
                                    .format(tvshow_id, season_id))
        elif len(path_array) == 7 and path_array[1] == 'tvshow' \
            and path_array[3] == 'season' and path_array[5] == 'episode':
                tvshow_id = path_array[2]
                season_id = path_array[4]
                episode_id = path_array[6]
                data_id = 5
                query_string = ("SELECT Episode.id, Episode.number, "
                                    "Episode.name, Episode.overview "
                                "FROM TVShow "
                                "JOIN Season "
                                    "ON TVShow.id = Season.tvshow_id "
                                "JOIN Episode "
                                    "ON Season.id = Episode.season_id "
                                "WHERE TVShow.id = {} "
                                "AND Season.id = {} "
                                "AND Episode.id = {} "
                                "ORDER BY Episode.number ASC"
                                    .format(tvshow_id, season_id, episode_id))

        if data_id != None and query_string != None:
            ''' Returns 200 with data if found '''
            data = s.get_data(data_id, query_string)
            s.send_response(200)
            s.send_header("Content-type", "application/json")
            s.end_headers()
            s.wfile.write(data)
        else:
            ''' Returns 404 if not URL path was not found '''
            new_dict = {}
            new_dict['status'] = 404
            new_dict['response'] = "Requested URL was not found."
            s.send_response(404)
            s.send_header("Content-type", "application/json")
            s.end_headers()
            data = json.dumps(new_dict)
            s.wfile.write(data)

    def get_data(self, data_id, query_string):
        ''' Establishes connection to SQL server and queries data '''
        USER = 'student'
        PASSWORD = 'aLQQLXGQp2rJ4Wy5'
        MYSQL_HOST = '173.246.108.142'
        MYSQL_PORT = '3306'
        MYSQL_DB = 'Project_169'

        cnx = mysql.connector.connect(user=USER,
                                      password=PASSWORD,
                                      host=MYSQL_HOST,
                                      port=MYSQL_PORT,
                                      database=MYSQL_DB)
        cursor = cnx.cursor()
        cursor.execute(query_string)
        data = self.process_data(data_id, cursor)
        cursor.close()
        cnx.close()
        data = json.dumps(data)
        return data

    def process_data(self, data_id, cursor):
        ''' Processes the returned data based on request '''
        if data_id == 0:
            new_list = []
            for (show_id, show_name, show_poster) in cursor:
                new_dict = {}
                new_dict['name'] = show_name
                new_dict['id'] = show_id
                new_dict['poster'] = show_poster
                new_list.append(new_dict)
            return new_list
        elif data_id == 1:
            new_dict = {}
            for (id, name, poster, overview, network, genres) in cursor:
                new_dict['name'] = name
                new_dict['id'] = id
                new_dict['poster'] = poster
                new_dict['overview'] = overview
                new_dict['network'] = network
                new_dict['genres'] = genres.split(',')
            return new_dict
        elif data_id == 2:
            new_list = []
            for (id, name) in cursor:
                new_dict = {}
                new_dict['id'] = id
                new_dict['name'] = name
                new_list.append(new_dict)
            return new_list
        elif data_id == 3:
            new_list = []
            for (id, number) in cursor:
                new_dict = {}
                new_dict['id'] = id
                new_dict['number'] = number
                new_list.append(new_dict)
            return new_list
        elif data_id == 4:
            new_list = []
            for (id, number, name) in cursor:
                new_dict = {}
                new_dict['id'] = id
                new_dict['number'] = number
                new_dict['name'] = name
                new_list.append(new_dict)
            return new_list
        elif data_id == 5:
            new_dict = {}
            for (id, number, name, overview) in cursor:
                new_dict['id'] = id
                new_dict['number'] = number
                new_dict['name'] = name
                new_dict['overview'] = overview
            return new_dict


if __name__ == '__main__':
    ''' Initializes the HTTP server to handles API requests '''
    HOST_NAME = 'localhost'
    PORT_NUMBER = 9898

    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class(("", PORT_NUMBER), MyHandler)
    print time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER)
