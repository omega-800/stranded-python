
from adventurelib import when, say
from stranded import instance


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
    map.display(player.mapCoordinates, player.tileCoordinates)

@when ("go DIRECTION")
def go(direction):
    match direction:
        case "north" | "n":
            list1 = list(player.mapCoordinates)
            list1[3] = str(int(list1[3])+1)
            player.mapCoordinates = ''.join(list1)
        case "east" | "e":
            list1 = list(player.mapCoordinates)
            list1[1] = str(int(list1[1])+1)
            player.mapCoordinates = ''.join(list1)
        case "south" | "s":
            list1 = list(player.mapCoordinates)
            list1[3] = str(int(list1[3])-1)
            player.mapCoordinates = ''.join(list1)
        case "west" | "w":
            list1 = list(player.mapCoordinates)
            list1[1] = str(int(list1[1])-1)
            player.mapCoordinates = ''.join(list1)
        case _:
            say("""invalid direction""")
