import requests
import re


def get_tallest_hero_by_gender_and_employment(gender: str, has_job: bool):
    url = "https://akabab.github.io/superhero-api/api/all.json"
    try:
        response = requests.get(url)
        heroes = response.json()
    except requests.RequestException as e:
        print(f"Ошибка: {e}")
        return None

    def get_height_cm(height_list):
        if not height_list or len(height_list) < 2:
            return None
        cm_height = height_list[1]
        match = re.search(r'(\d+)', cm_height)
        if match:
            return int(match.group(1)) if int(match.group(1)) > 0 else None
        return None

    filtered = []
    for hero in heroes:
        hero_gender = hero.get("appearance", {}).get("gender")
        if hero_gender != gender:
            continue

        occupation = hero.get("work", {}).get("occupation")
        if has_job and occupation == "-":
            continue
        if not has_job and not (occupation == "-"):
            continue

        height_cm = get_height_cm(hero.get("appearance", {}).get("height", []))
        if height_cm is None:
            continue

        filtered.append((height_cm, hero))

    if not filtered:
        return None
    
    tallest = max(filtered, key=lambda x: x[0])
    return tallest[1]
