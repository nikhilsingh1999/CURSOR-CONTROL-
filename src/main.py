import cv2
import mediapipe as mp
import pyautogui

class HandGestureController:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.screen_width, self.screen_height = pyautogui.size()
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.5)
        self.mp_draw = mp.solutions.drawing_utils

    def run(self):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break

            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = self.hands.process(frame_rgb)

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    self.mp_draw.draw_landmarks(frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)
                    self.control_cursor(hand_landmarks)

            cv2.imshow("Hand Gesture Control", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()

    def control_cursor(self, hand_landmarks):
        thumb_tip = hand_landmarks.landmark[4]
        index_tip = hand_landmarks.landmark[8]

        thumb_x, thumb_y = int(thumb_tip.x * self.screen_width), int(thumb_tip.y * self.screen_height)
        index_x, index_y = int(index_tip.x * self.screen_width), int(index_tip.y * self.screen_height)

        # Calculate the distance between thumb and index finger
        distance = ((thumb_x - index_x) ** 2 + (thumb_y - index_y) ** 2) ** 0.5

        # Threshold for considering the fingers as pinched
        pinch_threshold = 50

        if distance < pinch_threshold:
            pyautogui.click()

        # Move the cursor to the position of the index finger
        pyautogui.moveTo(index_x, index_y)

if __name__ == "__main__":
    gesture_controller = HandGestureController()
    gesture_controller.run()
