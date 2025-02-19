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
    names =[]
    for food in spicy_foods:
        names.append(food["name"])
    return(names)
    print(get_names(spicy_foods))

def get_spiciest_foods(spicy_foods):
    spiciest_foods = []
    for food in spicy_foods:
    
        if food["heat_level"] > 5:
            spiciest_foods.append(food)
    return spiciest_foods
    print (get_spiciest_foods(spicy_foods))
    

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = food["heat_level"]

        heat_level_str= "🌶" * heat_level
        output =f"{name} ({cuisine}) | Heat Level: {heat_level_str}"
        print(output)
      
    

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"].lower() == cuisine.lower():
            return food
    return None
    pass

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food["heat_level"] > 5:
            heat_level_emojis = "🌶" * food["heat_level"]
            output = f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_emojis}"
            print(output)
    pass

def get_average_heat_level(spicy_foods):
    total_heat = 0
    count = 0
    
    for food in spicy_foods:
        total_heat += food["heat_level"]
        count += 1

    average_heat = total_heat // count
    return average_heat

average_heat = get_average_heat_level(spicy_foods)
print(f"The average heat level is : {average_heat}")


pass

def create_spicy_food(spicy_foods, new_spicy_food):
    spicy_foods.append(new_spicy_food)
    return spicy_foods
new_spicy_food = {
    'name': 'Griot',
    'cuisine': 'Haitian',
    'heat_level': 10,
}
updated_spicy_foods = create_spicy_food(spicy_foods, new_spicy_food)
print(updated_spicy_foods)
