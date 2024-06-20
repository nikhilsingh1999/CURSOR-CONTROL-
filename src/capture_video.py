import cv2

def get_video_capture(source=0):
    return cv2.VideoCapture(source)
