import cv2
import pyautogui
import time
from hand_tracking import HandTracker

# Screen size
screen_w, screen_h = pyautogui.size()

# Camera
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(3, 640)
cap.set(4, 480)

tracker = HandTracker()

# Smoothening
smoothening = 5
prev_x, prev_y = 0, 0

# Click cooldown
last_click_time = 0

print("Starting Air OS...")

while True:
    try:
        success, frame = cap.read()

        if not success:
            continue

        frame = cv2.flip(frame, 1)

        frame, results = tracker.find_hands(frame)
        landmarks = tracker.get_landmarks(frame, results)

        if landmarks:
            fingers = tracker.fingers_up(landmarks)

            # Index finger tip
            x, y = landmarks[8][1], landmarks[8][2]

            # Convert to screen coords
            screen_x = int(x * screen_w / frame.shape[1])
            screen_y = int(y * screen_h / frame.shape[0])

            # Smooth movement
            curr_x = prev_x + (screen_x - prev_x) / smoothening
            curr_y = prev_y + (screen_y - prev_y) / smoothening

            # Move cursor (only index finger up)
            if fingers == [0, 1, 0, 0, 0]:
                pyautogui.moveTo(curr_x, curr_y)

            prev_x, prev_y = curr_x, curr_y

            # Click (pinch)
            thumb = landmarks[4]
            index = landmarks[8]

            distance = tracker.find_distance(thumb, index)

            if distance < 30:
                current_time = time.time()

                if current_time - last_click_time > 0.7:
                    pyautogui.click()
                    last_click_time = current_time

        cv2.imshow("Air OS", frame)

        if cv2.waitKey(1) == 27:
            break

        # Reduce CPU load
        time.sleep(0.01)

    except Exception as e:
        print("Error:", e)
        continue

cap.release()
cv2.destroyAllWindows()