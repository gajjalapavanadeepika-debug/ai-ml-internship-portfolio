import cv2
import mediapipe as mp
import pyautogui

# Disable PyAutoGUI fail-safe to prevent accidental interruptions
pyautogui.FAILSAFE = False

# Initialize MediaPipe Hands and OpenCV Video Capture
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

# Get screen width and height for coordinate mapping
screen_width, screen_height = pyautogui.size()

while cap.isOpened():
    success, image = cap.read()
    if not success:
        print("Ignoring empty camera frame.")
        continue

    # Flip the image horizontally for a selfie-view display and convert BGR to RGB
    image = cv2.flip(image, 1)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Process the image and find hands
    results = hands.process(image_rgb)
    
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            h, w, c = image.shape
            index_finger = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            thumb_finger = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            middle_finger = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
            
            x_index, y_index = int(index_finger.x * w), int(index_finger.y * h)
            x_thumb, y_thumb = int(thumb_finger.x * w), int(thumb_finger.y * h)
            x_middle, y_middle = int(middle_finger.x * w), int(middle_finger.y * h)
            
            # 1. Cursor Movement (Index Finger)
            screen_x = int(index_finger.x * screen_width)
            screen_y = int(index_finger.y * screen_height)
            pyautogui.moveTo(screen_x, screen_y)
            
            # 2. Click Trigger (Thumb & Index distance)
            click_distance = ((x_thumb - x_index)**2 + (y_thumb - y_index)**2) ** 0.5
            if click_distance < 35:
                pyautogui.click()
                pyautogui.sleep(0.2)
                
            # 3. Scrolling Action (Thumb & Middle finger distance)
            scroll_distance = ((x_thumb - x_middle)**2 + (y_thumb - y_middle)**2) ** 0.5
            if scroll_distance < 30:
                pyautogui.scroll(-40)  # Scroll down
                pyautogui.sleep(0.1)
            elif scroll_distance > 100:
                pyautogui.scroll(40)   # Scroll up
                pyautogui.sleep(0.1)

    # Display the webcam window
    cv2.imshow('AI Hand Gesture Computer Control', image)
    
    if cv2.waitKey(5) & 0xFF == 27:  # Press 'Esc' to exit
        break

cap.release()
cv2.destroyAllWindows()
