import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="e529057e79b24a59b014c609de627786",
                                                                client_secret="0fdc9dc95be8436daf5577238c21545c"))
lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'

results = spotify.artist_top_tracks(lz_uri)

for track in results['tracks'][:10]:
    print('track    : ' + track['name'])
    print('audio    : ' + track['preview_url'])
    print('cover art: ' + track['album']['images'][0]['url'])
    print()
