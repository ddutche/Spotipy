
import spotipy
import pandas as pd
import csv
from spotipy.oauth2 import SpotifyOAuth
class Artists:
    def __init__(self, account_name,client_id,client_secret):
        self.account_name = str(account_name)
        self.csv_file = open("Discography.csv","w", newline = "", encoding = "utf-8")
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri="http://localhost:8888/callback",
        scope="playlist-read-private"))
        
        self.initialize()

    def initialize(self): #Writing start to csv
        csv_writer = csv.writer(self.csv_file)
        csv_writer.writerow(["PlaylistName", "CollaborativePlaylist", "SongName","AddedBy", "Artist", "Feature1","Feature2","Feature3","Feature4","Feature5"])
        self.csv_writer = csv_writer
        self.write()
    
    def write(self):
        playlists = self.sp.user_playlists(self.account_name)["items"]
         
        for playlist in playlists: #Iterating through playlists
            colab = playlist["collaborative"]
            playlist_id = playlist["id"]
            playlist_info = self.sp.playlist(playlist_id, fields="tracks.items(added_by.id,track.name,track.artists.name)")
            playlist_name = playlist["name"]

            for item in playlist_info["tracks"]["items"]: #looking at each song in the playlist
                artists = []
                song = item["track"]["name"]
                #addedby = item["track"]["added_by"]
                addedby = item["added_by"]["id"] if item.get("added_by") else "Unknown"

                for i in item["track"]["artists"]: #looking at each artist on each song
                    artists.append(i["name"])
                
                while len(artists) <= 5: #Standardizing artist list length
                    artists.append("NaN")
                self.csv_writer.writerow([playlist_name, colab, song, addedby, artists[0],artists[1],artists[2],artists[3],artists[4],artists[5]])
        self.sheet = self.edit()
    
    def edit(self):
        self.sheet = pd.read_csv("Discography.csv")
        for i in self.sheet["AddedBy"].unique():
            try:
                user_info = self.sp.user(str(i))["display_name"]
                self.sheet["AddedBy"] = self.sheet["AddedBy"].replace(i, user_info)
            except Exception as e:
                user_info = "Unknown"
                self.sheet["AddedBy"] = self.sheet["AddedBy"].replace(i, user_info)
        self.csv_file.close()
        self.render()

    def render(self):
        return self.sheet



