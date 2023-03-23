import cv2 as cv2

# // в самом низу уберите коммент с соотв. задания

# Задание 1 (Картинка №8)
def viewImage():
    img = cv2.imread(cv2.samples.findFile("variant-8.jpg"))
    width = int(img.shape[1])//2
    height = int(img.shape[0])//2
    cropped = img[height-200:height+200, width-200:width+200] # // вырезал прямоугольник в середине размером 400х400
    cv2.imshow('Cat', cropped)
    cv2.waitKey(27)
    cv2.destroyAllWindows()


# Задание №2
def video_processing():
    cap = cv2.VideoCapture(0)

    point = cv2.imread('ref-point.png', 0)
    fly = cv2.imread('fly64.png')

    ret, thresh = cv2.threshold(point, 127, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, 2, 1)
    contours_count = [contours[0], contours[1]]

    down_points = (640, 480)
    while True:
        ret, frame = cap.read()
        frame = cv2.resize(frame, down_points, interpolation=cv2.INTER_LINEAR)
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (7, 7), 0)
        ret, video_thresh = cv2.threshold(gray, 130, 255, 0)
        contours, hierarchy = cv2.findContours(video_thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        x, y, h, w = [], [], [], []
        for contour in contours:
            for i in range(len(contours_count)):
                ret = cv2.matchShapes(contours_count[i], contour, 1, 0.0)
                if (ret < 0.1) & (len(contour) > 20):
                    x.append(cv2.boundingRect(contour)[0])
                    y.append(cv2.boundingRect(contour)[1])
                    h.append(cv2.boundingRect(contour)[2])
                    w.append(cv2.boundingRect(contour)[3])
                    break
        # нашли метку - находим координаты
        height = 0
        width = 0
        if len(x) == 2:
            coord_x = min(x)
            coord_y = min(y)
            for i in range(len(h)):
                height += h[i]
                width += w[i]

            fly_resized = cv2.resize(fly, (width, height))
            for i in range(height):
                for j in range(width):
                    if (fly_resized[i, j, 0] < 250) & (fly_resized[i, j, 1] < 250) & (fly_resized[i, j, 2] < 250):
                        frame[coord_y + i, coord_x + j] = fly_resized[i, j]

        cv2.imshow('point_frame', frame)

        if cv2.waitKey(30) == 27:
            # ESC чтобы выйти
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':

    # Задание 1
    # viewImage()

    # Задание 2, 3 + доп
    # video_processing()

    pass

