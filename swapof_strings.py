def swap_values():
    x, y = 25, "Hyd"
    x, y = y, x  # Swapping values without using a third variable
    print(f"After swap: x = {x}, y = {y}")

if __name__ == "__main__":
    swap_values()
