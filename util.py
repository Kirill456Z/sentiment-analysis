def proba_to_res(proba):
    if proba < 0.2:
        return "Отрицательный"
    elif proba < 0.4:
        return "Вероятно отрицательный"
    elif proba < 0.6:
        return "Нейтральный"
    elif proba < 0.8:
        return "Вероятно положительный"
    else:
        return "Положительный"
