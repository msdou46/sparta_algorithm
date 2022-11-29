
print('--------------------------- 3-9 숙제 3. 멜론 베스트 앨범 뽑기 ---------------------------')


def get_melon_best_album(genre_array, play_array):

    genre_n = len(genre_array)
    all_genre_played = {}
    genre_index_played_dict = {}
    last_result = []

    for n in range(genre_n):
        name = genre_array[n]
        played = play_array[n]
        if name in all_genre_played:
            all_genre_played[name] += played
            genre_index_played_dict[name].append([n, played])
        else:
            all_genre_played[name] = played
            genre_index_played_dict[name] = [[n, played]]

    sorted_all_genre_played = sorted(all_genre_played.items(), key=lambda item: item[1], reverse=True)
                                    # 정렬하고자 하는 객체의 아이템, 무엇을 기준으로 정렬할 것인가, 내림차순인가 오름차순인가.
                                    # 여기서 장르별 전체 플레이 횟수에 따라서 장르가 정렬됐어.

    for genre, played in sorted_all_genre_played:
        index_played = genre_index_played_dict[genre]
        sorted_index_played = sorted(index_played, key=lambda item: item[1], reverse=True) # 여기서 동일 장르별 플레이 횟수가 정렬.
        print("sorted_index_played : ", sorted_index_played)
        for i in range(len(sorted_index_played)):
            if i > 1:   # 장르별로 최대 2개만 플레이 횟수를 보여주고 싶거든.
                 break
            last_result.append(sorted_index_played[i][0])   # 인덱스만

    print('all_genre_played : ', sorted_all_genre_played)
    print("genre_index_played : ", genre_index_played_dict)

    return last_result


print("정답 = [4, 1, 3, 0] / 현재 풀이 값 = ",
      get_melon_best_album(["classic", "pop", "classic", "classic", "pop"],
                           [500, 600, 150, 800, 2500]))
'''
print("정답 = [0, 6, 5, 2, 4, 1] / 현재 풀이 값 = ",
      get_melon_best_album(["hiphop", "classic", "pop", "classic", "classic", "pop", "hiphop"],
                           [2000, 500, 600, 150, 800, 2500, 2000]))
                           '''



'''
규칙은 다음과 같아.
    1. 속한 노래가 많이 재생된 장르를 먼저 수록한다.(단, 각 장르에 속한 노래의재생 수 총합은 모두 다르다.)
    2. 장르 내에서 많이 재생된 노래를 먼저 수록한다.
    3. 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록한다.
이를 통해서 해야 할 일을 정리해 보자.

1) 우선 가장 많이 재생된 장르의 순서를 알아야 해. 
    어떻게 할 까...
    {"clsssic" : 500 } 이런 식으로 정리해 보자고.
    만약에 해당 키 이름이 딕셔너리 안에 없다면 새로 선언해주고, 있다면 해당 키의 값에 플레이 횟수를 더해주는 걸로.
    이렇게 완성된 장르 : 재생횟수 속성 상태에서, 가장 재생 횟수가 높은 키를 뽑아야 해. 
    이러면... 
'''