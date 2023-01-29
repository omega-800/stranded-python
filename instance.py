from player import Player
from map import Map
from room import Room

class Instance():
    GREY = "\033[37m"
    YELLOW = "\033[93m"
    BROWN = "\033[90m"
    BLUE = "\033[34m"
    LIGHTBLUE = "\033[36m"
    GREEN = "\033[32m"
    RED = "\033[31m"

    stone = Room("""stone""", GREY)
    sand = Room("""sand""", YELLOW)
    dirt = Room("""dirt""", BROWN)
    water = Room("""water""", BLUE)
    shallowwater = Room("""shallow water""", LIGHTBLUE)
    forest = Room("""forest""", GREEN)
    lava = Room("""lava""", RED)

    player = Player("x1y2","x1y1")

    """map = Map({
        1:water,
        2:water,
        3:water,
        4:water,
        5:water,
        6:water,
        7:water,
        8:water,
        9:water,
        10:shallowwater,
        11:sand,
        12:sand,
        13:sand,
        14:sand,
        15:shallowwater,
        16:water,
        17:water,
        18:sand,
        19:dirt,
        20:dirt,
        21:forest,
        22:sand,
        23:shallowwater,
        24:water,
        25:water,
        26:sand,
        27:dirt,
        28:forest,
        29:forest,
        30:sand,
        31:sand,
        32:water,
        33:water,
        34:sand,
        35:forest,
        36:forest,
        37:stone,
        38:stone,
        39:sand,
        40:water,
        41:water,
        42:shallowwater,
        43:sand,
        44:forest,
        45:stone,
        46:lava,
        47:stone,
        48:water,
        49:water,
        50:shallowwater,
        51:sand,
        52:sand,
        53:stone,
        54:stone,
        55:stone,
        56:water,
        57:water,
        58:water,
        59:water,
        60:water,
        61:water,
        62:water,
        63:water,
        64:water
    })"""

    """map = Map({
        "x1y1":water,
        "x1y2":water,
        "x1y3":water,
        "x1y4":water,
        "x1y5":water,
        "x1y6":water,
        "x1y7":water,
        "x1y8":water,
        "x2y1":water,
        "x2y2":shallowwater,
        "x2y3":sand,
        "x2y4":sand,
        "x2y5":sand,
        "x2y6":sand,
        "x2y7":shallowwater,
        "x2y8":water,
        "x3y1":water,
        "x3y2":sand,
        "x3y3":dirt,
        "x3y4":dirt,
        "x3y5":forest,
        "x3y6":sand,
        "x3y7":shallowwater,
        "x3y8":water,
        "x4y1":water,
        "x4y2":sand,
        "x4y3":dirt,
        "x4y4":forest,
        "x4y5":forest,
        "x4y6":sand,
        "x4y7":sand,
        "x4y8":water,
        "x5y1":water,
        "x5y2":sand,
        "x5y3":forest,
        "x5y4":forest,
        "x5y5":stone,
        "x5y6":stone,
        "x5y7":sand,
        "x5y8":water,
        "x6y1":water,
        "x6y2":shallowwater,
        "x6y3":sand,
        "x6y4":forest,
        "x6y5":stone,
        "x6y6":lava,
        "x6y7":stone,
        "x6y8":water,
        "x7y1":water,
        "x7y2":shallowwater,
        "x7y3":sand,
        "x7y4":sand,
        "x7y5":stone,
        "x7y6":stone,
        "x7y7":stone,
        "x7y8":water,
        "x8y1":water,
        "x8y2":water,
        "x8y3":water,
        "x8y4":water,
        "x8y5":water,
        "x8y6":water,
        "x8y7":water,
        "x8y8":water
    })"""

    map = Map({
        "x1y1":sand,
        "x1y2":sand,
        "x1y3":shallowwater,
        "x1y4":water,
        "x2y1":stone,
        "x2y2":dirt,
        "x2y3":sand,
        "x2y4":shallowwater,
        "x3y1":stone,
        "x3y2":forest,
        "x3y3":dirt,
        "x3y4":sand,
        "x4y1":stone,
        "x4y2":lava,
        "x4y3":forest,
        "x4y4":sand
    })

    def __init__(self) -> None:
        pass