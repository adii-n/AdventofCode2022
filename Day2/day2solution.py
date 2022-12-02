text = (open("day2.txt")).read()

# initializing list
moves = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
    "X": "Rock",
    "Y": "Paper",
    "Z": "Scissors",
    "Rock": 1,
    "Paper": 2,
    "Scissors": 3,
    "Win": 6,
    "Tie": 3,
    "Loss": 0
}

sum = 0
matches = text.split("\n")

for match in matches:
    oppMove = moves[match[0]]
    myMove = moves[match[2]]
    oppMoveScore = moves[oppMove]
    myMoveScore = moves[myMove]
    roundResult = ""
    matchScore = 0
    if myMove == oppMove:
        roundResult = "Tie"
    elif (myMove == "Rock" and oppMove == "Scissors") or (myMove == "Paper" and oppMove == "Rock") or (myMove == "Scissors" and oppMove == "Paper"):
        roundResult = "Win"
    else:
        roundResult = "Loss"
    matchScore += myMoveScore
    matchScore += moves[roundResult]
    sum += matchScore

print(sum)

moves2 = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
    "X": "Loss",
    "Y": "Tie",
    "Z": "Win",
    "Rock": 1,
    "Paper": 2,
    "Scissors": 3,
    "Win": 6,
    "Tie": 3,
    "Loss": 0
}

sum2 = 0
for match in matches:
    oppMove = moves2[match[0]]
    oppMoveScore = moves[oppMove]
    matchScore = 0
    outcome = moves2[match[2]]
    arr = [1, 2, 3, 1, 2]
    if outcome == "Loss":
        myMoveScore = arr[arr.index(oppMoveScore) + 2]

    elif outcome == "Tie":
        myMoveScore = oppMoveScore
    else:
        myMoveScore = arr[arr.index(oppMoveScore) + 1]
    matchScore += myMoveScore
    matchScore += moves2[outcome]
    sum2 += matchScore
print(sum2)