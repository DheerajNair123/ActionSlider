import cv2
import mediapipe as mp
import pyautogui
import time


mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

cap = cv2.VideoCapture(0)

# Cooldown ke liye
last_action_time = 0
cooldown = 1.0  ##bahot fast ho rha tha isilye cooldown rakha hai

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("Ignoring empty frame.")
        continue

    # Flip the frame for a selfie view(apna right computer ka tight hone ke liye)
    frame = cv2.flip(frame, 1)

    # Convert the frame to RGB(for mediapipee)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame for hand landmarks
    results = hands.process(rgb_frame)

    # Get the current time[bhai just for reference le rahe hai]
    current_time = time.time()

    #logic apply krdiya
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                frame, hand_landmarks, mp_hands.HAND_CONNECTIONS
            )

            # coordinates of the wrist [0 matlab starting]] and index fingertip (8)
            wrist = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST]
            index_fingertip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]

            # Calculate horizontal movement
            if current_time - last_action_time > cooldown:
                if index_fingertip.x < wrist.x - 0.1:
                    pyautogui.press("left")  # functionalities check
                    cv2.putText(frame, "Previous Slide", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
                    last_action_time = current_time  # Update last action time
                elif index_fingertip.x > wrist.x + 0.1:
                    pyautogui.press("right")  # functionalities check(next slide)
                    cv2.putText(frame, "Next Slide", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
                    last_action_time = current_time  # Update last action time

    # Display the frame
    cv2.imshow('Gesture Recognition', frame)

    # q dabaya toh bhi exit hoga
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
