import sys

def draw_histogram():
    # Read tuples from standard input
    lines = sys.stdin.readlines()
    
    # Split each line into label and frequency
    entries = [(line.split()[0], int(line.split()[1])) for line in lines]
    
    # Sort entries based on frequency
    entries.sort(key=lambda x: x[1], reverse=True)
    
    # Print histogram
    for label, freq in entries:
        print(f"{label}: {'#' * freq}")

if __name__ == "__main__":
    draw_histogram()
