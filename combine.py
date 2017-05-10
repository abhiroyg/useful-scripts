import json
import sys

def merge(data1, data2):
    data = []
    l = min(len(data1), len(data2))
    i = 0
    j = 0
    while i < len(data1) and j < len(data2):
        if data1[i][0] < data2[j][0]:
            data.append(data1[i])
            i += 1
        elif data1[i][0] == data2[j][0]:
            x = data1[i]
            x[1] = str(int(x[1]) + int(data2[j][1]))
            x[4] = json.dumps(json.loads(x[4]) + json.loads(data2[j][4]))
            data.append(x)
            i += 1
            j += 1
        else:
            data.append(data2[j])
            j += 1
    while i < len(data1):
        data.append(data1[i])
        i += 1
    while j < len(data2):
        data.append(data2[j])
        j += 1
    print data1
    print '-----------'
    print data2
    print '-----------'
    print data
    print '-----------'

    data[0][2] = str(int(data[0][1]))
    for i in range(1, len(data)):
        data[i][2] = str(int(data[i][1]) + int(data[i-1][2]))

    return data

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        count = 0
        data1 = []
        data2 = []
        data = data1
        for line in f:
            # There has to be a new line at the end of the file
            # Otherwise next if condition will not execute
            if line.startswith('===='):
                count += 1
                continue
            if count == 2:
                print "final merge"
                data = merge(data1, data2)

                data1 = []
                data2 = []
                print '-----------'
                print '-----------'
                print '\n'.join(' '.join(x) for x in data)
                break

            if count == 1:
                print "switched"
                if data2:
                    data1 = merge(data1, data2)
                    data2 = []
                data = data2

            # reset
            count = 0

            # read
            data.append(line.strip().split(' ', 4))
