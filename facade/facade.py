# Subsystem components
class TV:
    def turn_on(self):
        print("Turning on the TV")

    def set_input_source(self, source):
        print(f"Setting input source to {source}")


class SoundSystem:
    def turn_on(self):
        print("Turning on the Sound System")

    def set_volume(self, volume):
        print(f"Setting volume to {volume}")


class GamingConsole:
    def turn_on(self):
        print("Turning on the Gaming Console")

    def start_game(self, game_name):
        print(f"Starting {game_name}")


# Facade

class EntertainmentSystemFacade:
    def __init__(self):
        self.tv = TV()
        self.sound_system = SoundSystem()
        self.gaming_console = GamingConsole()

    def watch_tv(self):
        self.tv.turn_on()
        self.tv.set_input_source("Cable TV")
        self.sound_system.turn_on()
        self.sound_system.set_volume(20)

    def play_game(self, game_name):
        self.gaming_console.turn_on()
        self.gaming_console.start_game(game_name)


if __name__ == "__main__":
    entertainment_system = EntertainmentSystemFacade()

    print("=== Watching TV ===")
    entertainment_system.watch_tv()

    print("\n=== Playing a Game ===")
    entertainment_system.play_game("Super Mario")
