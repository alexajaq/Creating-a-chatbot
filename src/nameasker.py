import json
from typing import Any


def give_user_the_third_degree() -> dict[str, Any]:
    print("What is your name?")
    my_name: str = input()

    print("Nice to meet you " + my_name + "!")
    thank_you = input()

    print("What is your favorite food, " + my_name + "?")
    favorite_food: str = input()
    print("Ah, your favorite food is " + favorite_food + ", mine too!")

    res: str
    while (res := input("Do you want to hear a story? (Enter y/n)").lower()) not in {"y", "n"}:
        pass

    tell_story: bool = res == 'y'

    if tell_story:
        print("""
            There was once a goddess birthed from a volcano.
            She travelled far and wide, she even met death.
            Eventually, she went back to the volcano,
            believing herself to be enough company.
            """)
    else:
        print("Maybe next time then. Thank you.")

    summary: dict[str, Any] = {
        'name': my_name,
        'food': favorite_food,
        'story_told': tell_story,
    }

    return summary


if __name__ == "__main__":
    result: dict[str, Any] = give_user_the_third_degree()
    print(f'User Summary: {json.dumps(result)}')
