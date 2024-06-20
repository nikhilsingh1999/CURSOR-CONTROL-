import cv2
import mediapipe as mp

class HandDetector:
    def __init__(self, detection_confidence=0.7, tracking_confidence=0.7):
        self.hands = mp.solutions.hands.Hands(min_detection_confidence=detection_confidence,
                                              min_tracking_confidence=tracking_confidence)
        self.mp_draw = mp.solutions.drawing_utils

    def find_hands(self, frame):
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(frame_rgb)
        return results

    def draw_hands(self, frame, results):
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                self.mp_draw.draw_landmarks(frame, hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS)
        return frame
