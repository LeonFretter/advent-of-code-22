from dataclasses import dataclass
from enum import Enum


class Hand(Enum):
    ROCK = "A"
    PAPER = "B"
    SCISSORS = "C"


class Result(Enum):
    LOSE = 0
    DRAW = 1
    WIN = 2


@dataclass
class RockPaperScissors:
    hand: Hand

    def result(self, other: "RockPaperScissors") -> Result:
        if self.hand == other.hand:
            return Result.DRAW
        else:
            return Result.WIN if self.hand == Hand.ROCK and other.hand == Hand.SCISSORS or \
                self.hand == Hand.PAPER and other.hand == Hand.ROCK or \
                self.hand == Hand.SCISSORS and other.hand == Hand.PAPER else Result.LOSE

    def __eq__(self, other: "RockPaperScissors") -> bool:
        return self.hand == other.hand

    def symbol_score(self) -> int:
        match self.hand:
            case Hand.ROCK:
                return 1
            case Hand.PAPER:
                return 2
            case Hand.SCISSORS:
                return 3

    def result_score(self, other: "RockPaperScissors") -> int:
        match self.result(other):
            case Result.LOSE:
                return 0
            case Result.DRAW:
                return 3
            case Result.WIN:
                return 6

    def score(self, other: "RockPaperScissors") -> int:
        return self.symbol_score() + self.result_score(other)


type Game = tuple[RockPaperScissors, RockPaperScissors]
type Games = list[Game]


def readLine(line: str) -> Game:
    hand1, hand2 = line.split()
    hand2 = hand2.replace("X", "A").replace("Y", "B").replace("Z", "C")
    return RockPaperScissors(Hand(hand1)), RockPaperScissors(Hand(hand2))


def readLines(txt: str) -> list[Game]:
    return [readLine(line) for line in txt.splitlines() if line.strip() != ""]


def scoreGames(games: Games) -> int:
    return sum([game[1].score(game[0]) for game in games])


def readIntendedResult(txt: str) -> Result:
    match txt:
        case "Z":
            return Result.WIN
        case "Y":
            return Result.DRAW
        case "X":
            return Result.LOSE
    raise ValueError(f"Invalid intended result: {txt}")


def readNewGame(line: str) -> tuple[RockPaperScissors, Result]:
    hand, intended_result = line.split()
    return RockPaperScissors(Hand(hand)), readIntendedResult(intended_result)


def readNewGames(txt: str) -> list[tuple[RockPaperScissors, Result]]:
    return [readNewGame(line) for line in txt.splitlines() if line.strip() != ""]


def newGamesToGames(new_games: list[tuple[RockPaperScissors, Result]]) -> Games:
    return [(game[0], chooseHand(game[0], game[1])) for game in new_games]


def scoreNewGames(new_games: list[tuple[RockPaperScissors, Result]]) -> int:
    return scoreGames(newGamesToGames(new_games))


def chooseHand(opponent: RockPaperScissors, intended_result: Result) -> RockPaperScissors:
    symbols = [Hand.ROCK, Hand.PAPER, Hand.SCISSORS]

    if intended_result == Result.DRAW:
        return opponent
    elif intended_result == Result.WIN:
        return RockPaperScissors(symbols[(symbols.index(opponent.hand) + 1) % 3])
    else:
        return RockPaperScissors(symbols[(symbols.index(opponent.hand) - 1) % 3])


if __name__ == "__main__":
    txt = """\
A Y
B X
C Z\
"""
    games = readLines(txt)
    assert scoreGames(games) == 15

    new_games = readNewGames(txt)
    games2 = newGamesToGames(new_games)
    res2 = scoreNewGames(new_games)
    assert res2 == 12
