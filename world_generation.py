import numpy as np


def generate_world(width, height, scale):
    def generate_perlin_noise(width, height, scale=100):
        # Generate random gradient vectors
        gradient_vectors = (np.random.randn(width, height, 2))
        gradient_vectors = gradient_vectors / np.linalg.norm(gradient_vectors, axis=2, keepdims=True)

        # Generate grid
        x = np.linspace(0, scale, width, endpoint=False)
        y = np.linspace(0, scale, height, endpoint=False)
        x_grid, y_grid = np.meshgrid(x, y)

        # Rescale grid to integers for indexing
        x_indices = x_grid.astype(int)
        y_indices = y_grid.astype(int)

        # Fractional parts for interpolation
        x_fraction = x_grid - x_indices
        y_fraction = y_grid - y_indices

        # Calculate dot products
        dot_top_left = np.sum(gradient_vectors[x_indices, y_indices] * np.dstack([x_fraction, y_fraction]), axis=2)
        dot_top_right = np.sum(gradient_vectors[x_indices + 1, y_indices] * np.dstack([x_fraction - 1, y_fraction]), axis=2)
        dot_bottom_left = np.sum(gradient_vectors[x_indices, y_indices + 1] * np.dstack([x_fraction, y_fraction - 1]), axis=2)
        dot_bottom_right = np.sum(gradient_vectors[x_indices + 1, y_indices + 1] * np.dstack([x_fraction - 1, y_fraction - 1]), axis=2)

        # Interpolation
        top_interp = interpolate(dot_top_left, dot_top_right, x_fraction)
        bottom_interp = interpolate(dot_bottom_left, dot_bottom_right, x_fraction)
        interpolated_values = interpolate(top_interp, bottom_interp, y_fraction)

        return interpolated_values

    def interpolate(a, b, t):
        w = t * t * (3 - 2 * t)
        return a + w * (b - a)

    noise1 = generate_perlin_noise(width, height, scale)
    noise2 = generate_perlin_noise(width, height, scale)
    noise3 = generate_perlin_noise(width, height, 8)

    tiles = np.zeros([width, height], dtype='object')

    for row in range(height):
        for column in range(width):
            if noise2[row, column] > 0.15:
                tiles[column, row] = 'tree'
            if noise1[row, column] < -0.26:
                tiles[column, row] = 'ore'
            if noise3[row, column] < -0.2:
                tiles[column, row] = 'water'

    return tiles


if __name__ == '__main__':
    pass
    # width = 100
    # height = 100
    # scale = 13
    #
    # generated_world = generate_world(width, height, scale)
    #
    # for row in generated_world:
    #     print(row)
