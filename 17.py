#!/usr/bin/env python

num = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen', 20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety'}

def ans():
    count = 0
    for i in range(1,1000):
        if i < 21:
            count += len(num[i])
        if 20 < i < 100:
            if i % 10 == 0:
                count += len(num[i])
            else:
                count += len(num[10 * int(str(i)[0])] + num[int(str(i)[1])])
        if 99 < i < 1000:
            if i % 100 == 0:
                count += len(num[int(str(i)[0])] + 'hundred')
            else:
                if i % 100 < 21:
                    count += len(num[int(str(i)[0])] + 'hundredand' + num[int(str(i)[1:])])
                elif i % 10 == 0:
                    count += len(num[int(str(i)[0])] + 'hundredand' + num[10 * int(str(i)[1])])
                else:
                    count += len(num[int(str(i)[0])] + 'hundredand' + num[10 * int(str(i)[1])] + num[int(str(i)[2])])
    count += len('onethousand')
    return count
print(ans())
