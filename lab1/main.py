import random

criteria = {
    "Clothes color": ["light", "dark", "transparent", "multicolored"],
    "Accent": ["german", "american", "indian", "french"],
    "Gait type": ["confident", "unconfident", "waddle"],
    "Height": ["tall", "small", "average"],

    "View on politics": ["liberal", "conservative", "monarchical", "democratic"],
    "Nose type": ["snub", "straight", "humped"],
    "Number of arms": ["2", "3", "4", "5"],
    "Face shape": ["round", "oval", "square", "triangle"]

}

galaxies = {
    "Milky Way": {
        "Number of arms": ["2", "3"],
        "Face shape": ["round", "triangle"],
    },
    "Alpha": {
        "Number of arms": ["4", "5"],
        "Face shape": ["round", "oval", "square", ],
    },
    "Betta": {
        "Number of arms": ["2"],
        "View on politics": ["liberal", "democratic"],
    },
    "Andromeda": {
        "Number of arms": ["5"],
        "View on politics": ["monarchical", "democratic"],
    }
}

constellations = {
    "Gemini": {
        "Nose type": ["snub", "humped"],
    },
    "Lion": {
        "Nose type": ["straight"],
    }
}

planets = {
    "Mars": {
        "Clothes color": ["dark", "multicolored", "transparent"],
        "Accent": ["indian", "german", "french"],
        "Gait type": ["waddle", "confident"],
        "Height": ["small", "tall"],
        "galaxy": ["Milky Way"],
        "constellation": ["Gemini"],
    },
    "Earth": {
        "Clothes color": ["dark", "multicolored"],
        "Accent": ["french", "american", "indian"],
        "Gait type": ["confident", "waddle", "unconfident"],
        "Height": ["average", "small"],
        "galaxy": ["Milky Way"],
        "constellation": ["Lion"],
    },
    "Nibiru": {
        "Clothes color": ["transparent", "dark"],
        "Accent": ["german", "indian"],
        "Gait type": ["unconfident", "confident"],
        "galaxy": ["Alpha"],
        "constellation": ["Gemini"],
    },
    "Mercury": {
        "Accent": ["french", "german"],
        "Gait type": ["waddle", "unconfident"],
        "Height": ["small", "average"],
        "galaxy": ["Alpha"],
        "constellation": ["Lion"],
    },
    "Pluto": {
        "Clothes color": ["transparent", "light"],
        "Accent": ["american", "french"],
        "Height": ["average", "tall"],
        "galaxy": ["Betta"],
    },
    "Luna": {
        "Clothes color": ["light", "multicolored"],
        "Accent": ["german", "american", "indian"],
        "Gait type": ["unconfident"],
        "Height": ["tall", "small", "average"],
        "galaxy": ["Andromeda"],
    }

}


def resolve(characteristic):
    print("\n\nCharacteristic - " + characteristic)
    print('Choose one of the following:')
    for i, answer in enumerate(criteria[characteristic]):
        print(i, ") ", answer)

    while True:
        user_selection = input("Selected answer: ")
        if not user_selection.isnumeric() or int(user_selection) >= len(criteria[characteristic]):
            print("Invalid option")
        else:
            user_selection = int(user_selection)
            break

    planets_to_remove = []

    for planet in planets:
        if characteristic in planets[planet] \
                and criteria[characteristic][user_selection] not in planets[planet][characteristic]:
            planets_to_remove.append(planet)

    for planet in planets_to_remove:
        planets.pop(planet, None)
    print("Certainly not from: ", planets_to_remove)
    print("Possibly from: ", list(planets.keys()))

    return list(planets.keys())


if __name__ == "__main__":
    print("Please provide information based on the following criteria:")
    while True:
        _characteristic = random.choice(list(criteria.keys()))
        _planet = resolve(_characteristic)
        criteria.pop(_characteristic, None)
        if len(_planet) == 1:
            print("The citizen is from", _planet.pop())
            break
        if len(_planet) == 0:
            print("No data match. Citizen is from unknown planet")
            break
