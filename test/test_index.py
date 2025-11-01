from src.index import get_tallest_hero_by_gender_and_employment

def test_male_with_job():
    hero = get_tallest_hero_by_gender_and_employment("Male", True)
    assert hero is not None
    assert hero["appearance"]["gender"] == "Male"
    assert hero["work"]["occupation"] != "-"

def test_male_without_job():
    hero = get_tallest_hero_by_gender_and_employment("Male", False)
    assert hero is not None
    assert hero["appearance"]["gender"] == "Male"
    assert hero["work"]["occupation"] == "-"

def test_female_with_job():
    hero = get_tallest_hero_by_gender_and_employment("Female", True)
    assert hero is not None
    assert hero["appearance"]["gender"] == "Female"
    assert hero["work"]["occupation"] != "-"

def test_female_without_job():
    hero = get_tallest_hero_by_gender_and_employment("Female", False)
    assert hero is not None
    assert hero["appearance"]["gender"] == "Female"
    assert hero["work"]["occupation"] == "-"

def test_invalid_gender():
    hero = get_tallest_hero_by_gender_and_employment("Alien", True)
    assert hero is None
