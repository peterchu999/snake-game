def get_high_score():
    with open("data.txt",'r') as file:
        score = int(file.read())
        return score

def save_high_score(score):
    with open("data.txt",'w') as file:
        file.write(f"{score}")