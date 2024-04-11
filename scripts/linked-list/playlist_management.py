from linked_list import LinkedList


class Playlist(LinkedList):
    def __init__(self):
        super().__init__()

    def add_song(self, song):
        self.insert_tail(song)

    def play_song(self):
        if self.head is not None:
            print(f"Playing {self.head.data}")
            self.remove_head()
        else:
            print("No songs in the playlist.")

    def skip_song(self):
        if self.head is not None and self.head.next is not None:
            print(f"Skipping {self.head.data}")
            self.remove_head()
        else:
            print("No songs in the playlist.")

    def show_playlist(self):
        songs = []
        curr = self.head
        while curr is not None:
            songs.append(curr.data)
            curr = curr.next
        return " -> ".join(songs)


# Example usage.
my_playlist = Playlist()
my_playlist.add_song("Song 1")
my_playlist.add_song("Song 2")
my_playlist.add_song("Song 3")

print(f"\nPlaylist: {my_playlist.show_playlist()}")
print("Now playing: ")
my_playlist.play_song()

print(f"\nPlaylist: {my_playlist.show_playlist()}")
print("Skipping >> ")
my_playlist.skip_song()

print(f"\nPlaylist: {my_playlist.show_playlist()}")
