from pyzbar.pyzbar import decode
import cv2
import numpy as np


def create_border(barcode_polygon):
    pts = np.array([barcode_polygon], np.int32)
    pts = pts.reshape((-1, 1, 2))
    return [pts]


def main():
    # Initialize videocapture
    cap = cv2.VideoCapture(0)  # 0 = open default camera
    cap.set(3, 640)
    cap.set(4, 680)

    while True:

        # wait for a new frame from camera and store it into 'image_barcode'
        success, image_barcode = cap.read()

        # walk through found barcodes
        for barcode in decode(image_barcode):
            print(barcode)

            # selection by polygon barcode
            cv2.polylines(image_barcode, create_border(barcode.polygon), True, (255, 0, 255), 2)

            # getting data from barcode
            data = barcode.data.decode('utf-8')

            # add data to image_barcode
            cv2.putText(image_barcode, data, (barcode.rect[0], barcode.rect[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.9,
                        (255, 0, 255), 2)

        # result display
        cv2.imshow('Result', image_barcode)
        width = cv2.getWindowImageRect('Result')[2]
        height = cv2.getWindowImageRect('Result')[3]
        cv2.resizeWindow('Result', width, height)

        # exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
