def winner(names: list[str], scores: list[float]) -> str:
    max_score = scores[0]
    winner_index = 0
    for i in range(1, len(scores)):
        if scores[i] > max_score:
            max_score = scores[i]
            winner_index = i
    return names[winner_index]
def average(scores: list[float]) -> float:
    total = 0
    for score in scores:
        total = total + score
    if len(scores) == 0:
        return 0.0
    return total / len(scores)
def ranking(names: list[str], scores: list[float]) -> list[str]:
    result = []
    used = []
    for _ in range(len(scores)):
        best_index = None
        for i in range(len(scores)):
            if i not in used:
                if best_index is None or scores[i] > scores[best_index]:
                    best_index = i
        used.append(best_index)
        result.append(names[best_index])
    return result
def above_average(names: list[str], scores: list[float]) -> list[str]:
    result = []
    avg = average(scores)
    for i in range(len(scores)):
        if scores[i] > avg:
            result.append(names[i])
    return result