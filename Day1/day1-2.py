if __name__ == "__main__":
    inputData = []
    frequencyList = []
    frequency = 0

    with open('Day1\input-1.txt', 'r') as myfile:
        inputData = [int(i) for i in myfile.read().replace('\n',' ').split(' ')]

    i = 0
    while not frequencyList.__contains__(frequency):
        frequencyList.append(frequency)
        frequency += inputData.__getitem__(i)

        if i == len(inputData)-1:
            i = 0
        else:
            i += 1
    print(frequency)
            