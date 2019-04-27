import cv2

def difference(value0, value1):
    return value1 - value0

def find_movement(bild1, bild2):
    bild1 = convert_to_grayscale(bild1)
    bild2 = convert_to_grayscale(bild2)

    bild1 = cv2.GaussianBlur(bild1, (21, 21), 0)
    bild2 = cv2.GaussianBlur(bild2, (21, 21), 0)

    # Differenz zu 2 Bildern berechnen
    diff = difference(bild1, bild2)

    thresh = cv2.threshold(diff, 5, 255, cv2.THRESH_BINARY)[1]
    return thresh

def has_color(bild1):
    return bild1.shape[2] == 3


def convert_to_grayscale(bild1):
    if has_color(bild1):
        bild1 = cv2.cvtColor(bild1, cv2.COLOR_BGR2GRAY)
    return bild1



if __name__ == '__main__':

    camera = cv2.VideoCapture(0) # create camera object

    _, old_frame = camera.read()

    while(True):
        _, current_frame = camera.read()

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
        cv2.imshow("frame", find_movement(old_frame, current_frame))
        old_frame = current_frame

    camera.release()
    cv2.destroyAllWindows()
