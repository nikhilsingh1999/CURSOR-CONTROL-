import pyautogui

class GestureControl:
    def __init__(self):
        self.screen_w, self.screen_h = pyautogui.size()

    def move_cursor(self, lm, frame_shape):
        h, w, _ = frame_shape
        cursor_x = int(lm.x * self.screen_w)
        cursor_y = int(lm.y * self.screen_h)
        pyautogui.moveTo(cursor_x, cursor_y)

    def click_if_pinch(self, lm_thumb, lm_index, frame_shape):
        h, w, _ = frame_shape
        thumb_x, thumb_y = int(lm_thumb.x * w), int(lm_thumb.y * h)
        index_x, index_y = int(lm_index.x * w), int(lm_index.y * h)

        if abs(index_x - thumb_x) < 20 and abs(index_y - thumb_y) < 20:
            pyautogui.click()
