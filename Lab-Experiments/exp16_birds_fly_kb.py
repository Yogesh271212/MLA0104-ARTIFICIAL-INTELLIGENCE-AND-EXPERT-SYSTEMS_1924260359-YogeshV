knowledge_base = {
    'sparrow': {'is_bird': True, 'has_wings': True, 'is_flightless': False},
    'eagle': {'is_bird': True, 'has_wings': True, 'is_flightless': False},
    'penguin': {'is_bird': True, 'has_wings': True, 'is_flightless': True},
    'ostrich': {'is_bird': True, 'has_wings': True, 'is_flightless': True},
    'bat': {'is_bird': False, 'has_wings': True, 'is_flightless': False},
    'dog': {'is_bird': False, 'has_wings': False, 'is_flightless': True}
}

def can_fly(animal):
    props = knowledge_base.get(animal.lower())
    if not props:
        return "Unknown animal"
    if props['has_wings'] and not props['is_flightless']:
        return f"{animal.capitalize()} can fly."
    return f"{animal.capitalize()} cannot fly."

for animal in ['sparrow', 'penguin', 'eagle', 'ostrich', 'bat', 'dog']:
    print(can_fly(animal))
