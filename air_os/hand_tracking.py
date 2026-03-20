import cv2
import mediapipe as mp
import math


class HandTracker:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7
        )
        self.mp_draw = mp.solutions.drawing_utils

    def find_hands(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                self.mp_draw.draw_landmarks(
                    frame,
                    hand_landmarks,
                    self.mp_hands.HAND_CONNECTIONS
                )

        return frame, results

    def get_landmarks(self, frame, results):
        h, w, _ = frame.shape
        landmarks = []

        if results.multi_hand_landmarks:
            hand = results.multi_hand_landmarks[0]

            for id, lm in enumerate(hand.landmark):
                cx, cy = int(lm.x * w), int(lm.y * h)
                landmarks.append((id, cx, cy))

        return landmarks

    def fingers_up(self, landmarks):
        fingers = []

        if not landmarks:
            return []

        # Thumb
        if landmarks[4][1] > landmarks[3][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        # Other fingers
        tip_ids = [8, 12, 16, 20]

        for tip in tip_ids:
            if landmarks[tip][2] < landmarks[tip - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        return fingers

    def find_distance(self, p1, p2):
        x1, y1 = p1[1], p1[2]
        x2, y2 = p2[1], p2[2]

        return math.hypot(x2 - x1, y2 - y1)