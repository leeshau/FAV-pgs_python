import sys
# has arguments
def check_input():
    if sys.argv[1] != "-i" or sys.argv[3] != "-o":
        print("Wrong arguments")
        exit(1)
# arguments are in right formats
    for i in range(2, 5, 2):
        length = len(sys.argv[i])
        end = sys.argv[i][length - 4: length]
        if i == 2:
            result = end
        if end != ".txt" and end != ".xml":
            print("Wrong extensions of inputed files, must be either .txt or .xml")
            exit(2)
    return result