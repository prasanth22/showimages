import glob
import cv2

from click._compat import raw_input

def showimage(img):
    a = cv2.imread(img)
    cv2.imshow('Color image', a)
    k = cv2.waitKey(0)
    cv2.destroyAllWindows()


while 1:
    user_input = raw_input("do you want to read another folder = ")
    if user_input == 'no':
        break

    else:
        path = 'D:/python/images/'
        file = raw_input("Enter the folder name in which images are present(eg wallpapers,screenshots, etc) = ")
        for img in glob.glob(path + file + '/'+'*.*'):
            print(img)


        type = raw_input("Enter the type of file = ")


        filename = raw_input("Enter the file name = ")
        for img in glob.glob('D:/python/images/' + file + '/'+filename+'.'+type):
            showimage(img)






