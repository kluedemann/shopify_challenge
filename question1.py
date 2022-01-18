def main():
    data = []

    # Open file
    with open("./shopify_data.csv", "r") as in_file:
        lines = in_file.readlines()
    
    # Read price data
    for line in lines[1:]:
        line = line.strip().split(",")
        data.append(int(line[3]))

    # Calculate median
    data.sort()
    median = data[len(data) // 2]
    print(median)
    
    return


main()
