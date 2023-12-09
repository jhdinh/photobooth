import cv2

def display_push_to_start():
    cv2.namedWindow('PushToStart', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('PushToStart', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    image = cv2.imread("assets/PushToStart.png")

    while True:
        cv2.imshow("PushToStart", image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()
