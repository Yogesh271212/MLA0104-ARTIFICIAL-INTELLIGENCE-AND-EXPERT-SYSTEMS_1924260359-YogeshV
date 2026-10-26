import numpy as np

templates = {
    'Horizontal Line': np.array([
        [0, 0, 0],
        [1, 1, 1],
        [0, 0, 0]
    ]),
    'Vertical Line': np.array([
        [0, 1, 0],
        [0, 1, 0],
        [0, 1, 0]
    ]),
    'Plus Sign': np.array([
        [0, 1, 0],
        [1, 1, 1],
        [0, 1, 0]
    ])
}

def recognize_pattern(input_grid):
    best_pattern = None
    min_diff = float('inf')

    for name, template in templates.items():
        diff = np.sum(np.abs(input_grid - template))
        if diff < min_diff:
            min_diff = diff
            best_pattern = name

    return best_pattern

test_image = np.array([
    [0, 1, 0],
    [1, 1, 1],
    [0, 1, 0]
])

print("Input Grid:")
print(test_image)
print("Recognized Pattern:", recognize_pattern(test_image))
