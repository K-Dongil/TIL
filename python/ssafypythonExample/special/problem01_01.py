# 전체 점수 중 최고점을 반환
import json

# def max_score(scores):
#     return max(scores)

# def max_score(scores):
#     bestScore = 0
#     for score in scores:
#         if bestScore < score:
#             bestScore = score
#     return bestScore

def max_score(scores):
    bestScore = 0
    for i in range(len(scores)):
        for j in range(i, len(scores)):
            if scores[i] < scores[j]:
                bestScore = scores[i]
                scores[i] = scores[j]
                scores[j] = bestScore
    return scores[0]


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    scores_json = open('problem01_data.json', encoding='UTF8')
    scores = json.load(scores_json)
    print(max_score(scores)) 
    # => 90