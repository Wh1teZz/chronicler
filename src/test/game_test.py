from util.gameActions import *
from util.config import *
from util.playerActions import *

if __name__ == "__main__":
    f = deleteTownSquare()
    assert f == False

    ts1 = initTownSquare("Town 1", "DiscordChannel1")
    ts2 = initTownSquare("Town 2", "DiscordChannel2")

    assert ts1 == True
    assert ts2 == False

    ts = getTownSquare()
    assert ts.name == "Town 1"

    day = nextDay()
    assert day == 2

    day = prevDay()
    assert day == 1

    t = deleteTownSquare()
    assert t == True

    addChannels(["channel 1", "channel 2", "channel 3"])

    channels = getAllChannels()
    assert len(channels) == 3
    assert isChannel("channel 1") == True
    assert isChannel("no channel") == False