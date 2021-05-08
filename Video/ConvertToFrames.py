import cv2

# Will give an error when runs out of frames. That's normal. Too lazy to add an try/except
def convert_to_frames():
    print("Starting Conversion...")
    vc = cv2.VideoCapture('./video.mp4')
    c = 1

    if vc.isOpened():
        rval, frame = vc.read()
    else:
        rval = False

    while rval:
        print("Frame %s started" % rval)
        rval, frame = vc.read()

        cv2.imwrite('./frames/' + str(c) + '.png', frame)
        c = c + 1
        cv2.waitKey(1)
    vc.release()


convert_to_frames()
