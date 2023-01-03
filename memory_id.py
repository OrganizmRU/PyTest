
def append_score(score, scores=[]):
    scores.append(score)
    print(f'scores:{scores} & id:{id(score)}')


print(append_score.__defaults__)
print(id(append_score.__defaults__[0]))
append_score(95)
append_score(98)

