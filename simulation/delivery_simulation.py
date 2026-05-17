import time


def simulate_delivery(route):

    for stop in route:
        print(f"Delivering to {stop}")

        time.sleep(1)

    print("All deliveries completed")
