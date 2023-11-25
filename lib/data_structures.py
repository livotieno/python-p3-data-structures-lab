spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]


def get_names(spicy_foods):
    pass
    return [food["name"] for food in spicy_foods]

# Function to get spiciest foods (heat level greater than 5)


def get_spiciest_foods(spicy_foods):
    pass
    return [food for food in spicy_foods if food["heat_level"] > 5]

# Function to print spicy foods with heat level emojis


def print_spicy_foods(spicy_foods):
    pass
    for food in spicy_foods:
        print(
            f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")

# Function to get spicy food by cuisine


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    pass
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food

# Function to print spiciest foods with heat level emojis


def print_spiciest_foods(spicy_foods):
    pass
    spiciest_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods)

# Function to get average heat level

def get_average_heat_level(spicy_foods):
    pass

def create_spicy_food(spicy_foods, spicy_food):
    pass
def average_heat_level(spicy_foods):
    total_heat = sum(food["heat_level"] for food in spicy_foods)
    num_foods = len(spicy_foods)
    return total_heat // num_foods if num_foods > 0 else 0