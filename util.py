def proba_to_res(proba, best_threshold):
    if proba < 0.4 * best_threshold:
        return "Отрицательный"
    elif proba < 0.8 * best_threshold:
        return "Вероятно отрицательный"
    elif proba < 1.2 * best_threshold:
        return "Нейтральный"
    elif proba < 1.6 * best_threshold:
        return "Вероятно положительный"
    else:
        return "Положительный"
