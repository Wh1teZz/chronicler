class TownSquare():
    def __init__(self):
        self.players = []
        self.day = 1
        self.playerMessageMatrix = None
        self.messageScoreMatrix = None

    def addPlayer(self, playerName):
        if playerName not in self.players:
            self.players.append(playerName)
            return True
        else:
            return False

    def listPlayers(self):
        return self.players

    # generates the matricies after all players are added
    def generateTownSquare():
        pass

    def nextDay():
        pass

    def prevDay():
        pass

    def parseWhisper(message):
        pass

    def whisper(p1, p2):
        pass

    def getPlayerWhisper(p):
        pass

    def getAllWhispers():
        pass

    def _getPlayerWhisperAdmin(p):
        pass

    def _getAllWhispersAdmin():
        pass
