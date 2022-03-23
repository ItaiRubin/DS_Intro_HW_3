            def read_line(num,file):
    try:
        count = 0
        file1 = open(file)
        if type (num) != int:
            return "invalid input detected"
        for line in file1:
            count = count +1
            if count == num:
                return line
            if num > count:
                return "line" + str(line) + "doesnt exist"
    except:
        return "file not found"


def longest_word(file):
    try:
        list = []
        data = open(file)
        data = data.read()
        data = data.replace('.', ' ')
        data = data.replace('-', ' ')
        data = data.replace(',', ' ')
        split = data.split()
        split = sorted(split, key=len,reverse=True)
        list = data[0:5]
        return list
    except:
        return "file not found"



