def solution(genres, plays):
    plays_by_genres = dict()
    for index, genre in enumerate(genres):
        plays_by_genres.setdefault(genre, {}).update({index: plays[index]})
    best_albums = {k: [_k for _k, _v in sorted(v.items(), key=lambda item: item[1], reverse=True)][:2] for k, v in
                   sorted(plays_by_genres.items(),
                          key=lambda i: sum(i[1].values()), reverse=True)}

    return [item for sublist in best_albums.values() for item in sublist]


if __name__ == "__main__":
    case_1_genres = ["classic", "pop", "classic", "classic", "pop", "classic"]
    case_1_plays = [500, 600, 150, 800, 2500, 800]
    assert solution(case_1_genres, case_1_plays) == [4, 1, 3, 5]
