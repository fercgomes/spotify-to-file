from SwSpotify import spotify, SpotifyNotRunning
from time import sleep
import argparse

default_path = "/tmp/spotify_current"
default_refresh_time = 2.5 # seconds

def get_track():
    try:
        title, artist = spotify.current()
    except SpotifyNotRunning as e:
        return e
    else:
        return f"{artist} - {title}"

def main():
    parser = argparse.ArgumentParser(description="Outputs Spotify current song to a file.")
    parser.add_argument('--output', '-o', default=default_path, help="Path to file. Defaults to " + default_path)
    parser.add_argument('--refresh', '-r', type=float, default=default_refresh_time, help="Refresh interval. Defaults to " + str(default_refresh_time))
    parser.add_argument('-v', help="Outputs info to stdout.", action="store_true")
    args = parser.parse_args()

    while True:
        track = get_track()

        if(args.v):
            print(track)

        with open(args.output, 'w') as fp:
            fp.write(track)
        
        sleep(args.refresh)

if __name__ == "__main__":
    main()
