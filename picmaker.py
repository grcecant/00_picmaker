import random


def main():
    add = ''

    for i in range(25):
        if i > 0:
            add+='\n'
        r = random.randint(0,256)
        g = random.randint(0,256)
        b = random.randint(0,256)

        for j in range(10000):
            if j%5<3:
                add += str((r+j)%256) + ' ' + str((g+j)%256) + ' ' + str((b+j)%256) + '\n'
            else:
                add += str((r+i)%256) + ' ' + str((g+i)%256) + ' ' + str((b+i)%256) + '\n'

    pic = open('image.ppm', 'w+')
    #header
    pic.write('P3\n500 500\n255\n')
    #ppm body
    pic.write(add)
    pic.close()

main()
