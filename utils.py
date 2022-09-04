import json

def load_candidates():
    with open("candidates.json", "r", encoding="utf-8") as file:
        return json.load(file)

def get_candidates_all():
    return load_candidates()

def get_candidates_by_pk(pk):
    candidates = load_candidates()
    for candidate in candidates:
        if candidate['pk'] == pk:
            return candidate
    return 'Not Found'

def get_candidates_by_skill(skill_name):
    result = []
    candidates = load_candidates()
    for candidate in candidates:
        if skill_name in candidate['skills'].lower():
            result.append(candidate)
    return result