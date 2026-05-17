import matplotlib.pyplot as plt


def plot_route(route):

    x = [point[0] for point in route]
    y = [point[1] for point in route]

    plt.plot(x, y, marker="o")

    for i, point in enumerate(route):
        plt.text(point[0], point[1], str(i))

    plt.show()
