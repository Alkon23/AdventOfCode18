if __name__ == "__main__":
    inputData = ""

    with open('Day1\input-1.txt', 'r') as myfile:
        inputData = myfile.read().replace('\n', ',')
    
    print(sum(map(int, inputData.split(','))))