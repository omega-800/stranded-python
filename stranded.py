from adventurelib import start, when, say
from instance import Instance

instance = Instance()

@when("sleep")
def sleep():
    say("""
        You lie down and go to sleep.
    """)

@when("map")
def showmap():
    say("""
        This is the current map.
    """)
    instance.map.display(instance.player.mapCoordinates, instance.player.tileCoordinates)

@when ("go DIRECTION")
def go(direction):
    match direction:
        case "north" | "n":
            list1 = list(instance.player.mapCoordinates)
            list1[3] = str(int(list1[3])+1)
            instance.player.mapCoordinates = ''.join(list1)
        case "east" | "e":
            list1 = list(instance.player.mapCoordinates)
            list1[1] = str(int(list1[1])+1)
            instance.player.mapCoordinates = ''.join(list1)
        case "south" | "s":
            list1 = list(instance.player.mapCoordinates)
            list1[3] = str(int(list1[3])-1)
            instance.player.mapCoordinates = ''.join(list1)
        case "west" | "w":
            list1 = list(instance.player.mapCoordinates)
            list1[1] = str(int(list1[1])-1)
            instance.player.mapCoordinates = ''.join(list1)
        case _:
            say("""invalid direction""")


start()