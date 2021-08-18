tc = int(input())

for t in range(tc):
    student, student_n = map(int, input().split())
    score_lst = [list(map(int, input().split())) for _ in range(student)]
    grade_lst = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    total_score_lst = []
    ranking = 0

    for scores in score_lst:
        total_score = scores[0] * 0.35 + scores[1] * 0.45 + scores[2] * 0.2
        total_score_lst.append(total_score)

    for total_socre in total_score_lst:
        if total_score_lst[student_n -1] < total_socre:
            ranking += 1

    # if ranking < student/10:
    #     ranking = 0
    # else:
    #     ranking = ranking // (student//10)

    ranking = ranking // (student//10)

    print('#{} {}'.format(t+1, grade_lst[ranking]))


    # # 아래와 같이 학생수에 따른 겹치는 학점을 고려하여 리스트를 새로 만들어 접근할 수도 있음
    # new_grade_lst = []
    # for grade in grade_lst:
    #     for i in range(student//10):
    #         new_grade_lst.append(grade)
    # 20 19 18 17