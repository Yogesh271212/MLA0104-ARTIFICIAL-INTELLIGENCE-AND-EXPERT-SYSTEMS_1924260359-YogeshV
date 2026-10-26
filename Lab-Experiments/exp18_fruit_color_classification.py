fruit_rules = {
    'red': ['Apple', 'Strawberry', 'Cherry', 'Pomegranate'],
    'yellow': ['Banana', 'Mango', 'Lemon', 'Pineapple'],
    'green': ['Watermelon', 'Guava', 'Kiwi', 'Green Apple'],
    'orange': ['Orange', 'Papaya', 'Peach'],
    'purple': ['Grapes', 'Plum', 'Blackberry']
}

def identify_fruits_by_color(color):
    return fruit_rules.get(color.lower(), ['No fruit found for this color'])

def find_color_of_fruit(fruit_name):
    for color, fruits in fruit_rules.items():
        if fruit_name.capitalize() in fruits:
            return color
    return "Unknown"

print("Fruits with Yellow color:", identify_fruits_by_color('yellow'))
print("Fruits with Red color:", identify_fruits_by_color('red'))
print("Color of Mango:", find_color_of_fruit('Mango'))
