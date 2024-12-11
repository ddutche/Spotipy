# Spotipy
Lets you get a csv on the artists you have across all your playlists by using the Spotipy and Spotify for Developers libraries

To use this, you'll need a "Spotify For Developers" account (https://developer.spotify.com/), along with the client ID and the client secret it gives you), along with the User ID of the spotify account you're looking at.
I think the only way to get this ID is by going to the profile page on the spotify website, and looking at the numbers at the end of the website url. So for example, the link to my profile is https://open.spotify.com/user/gaayf3eanokb5m14swk5qbol6, which makes my USER ID "gaayf3eanokb5m14swk5qbol6"

Running this code will give you back a CSV File containing information such as

**PlaylistName** - The name of the playlist

**CollaborativePlaylist** - Says whether the playlist is collaborative or not

**SongName** - The name of the Song

**AddedBy** - What user added it to the playlist (Returns Unknown if the user who added it isn't known)

**Artist** - The Artist that created the song 

**Feature1** - **Feature5** - The Features on the song (Returns NA once the number of feature columns exceeds the number of features)

The "Functions" folder contains 3 items

1) Discography.csv - Where the data will be saved

2) Main.py - Where you call the Function

3) Line.py - Where the Function is stored

As of now, the class in Line.py is also in Main.py for easier downloadability, so this Line.py file is optional
