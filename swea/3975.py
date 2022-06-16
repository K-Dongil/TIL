tc = int(input())

result = [0] * tc

for t in range(0, tc):
    elice_win, elice_play, bob_win, bob_play = map(int, input().split())
    result[t] = "#" + str(t+1) + " DRAW"
    if elice_win / elice_play == bob_win / bob_play:
        continue
    elif elice_win / elice_play > bob_win / bob_play:
        result[t] = "#" + str(t+1) + " ALICE"
    elif elice_win / elice_play < bob_win / bob_play:
        result[t] = "#" + str(t+1) + " BOB"
    
for s in result:
    print(s)