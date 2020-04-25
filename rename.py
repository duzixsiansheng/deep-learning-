import os

detect = 'input/detection-results/'
truth = 'input/ground-truth/'
image = 'input/images-optional/'

a = 0
for file in os.listdir(detect):
    a = a + 1
    name = os.path.splitext(file)[0]

    print(file + '   '   + name)
    os.rename(detect + name + '.txt', detect + str(a) + '.txt')
    os.rename(truth + name + '.txt', truth + str(a) + '.txt')
    os.rename(image + name + '.jpg', image + str(a) + '.jpg')