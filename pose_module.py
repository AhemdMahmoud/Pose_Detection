import cv2
import mediapipe as mp
import time
import os

class PoseDetector:
    def __init__(self):
        # Initialize MediaPipe Pose.
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose()
        # Initialize MediaPipe drawing utilities.
        self.mp_drawing = mp.solutions.drawing_utils
        # Time tracking for screenshots.
        self.last_screenshot_time = time.time()
        self.screenshot_interval = 5  # Interval in seconds
        
        # Use a relative path for the screenshot directory
        self.screenshot_dir = os.path.join(os.path.dirname(__file__), 'images')
        os.makedirs(self.screenshot_dir, exist_ok=True)  # Create directory if it does not exist
        print(f"Screenshot directory: {self.screenshot_dir}")  # Debug print
        
        self.screenshot_count = 0

    def process_frame(self, frame):
        # Convert the BGR image to RGB.
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Process the frame and detect poses.
        results = self.pose.process(rgb_frame)
        return results

    def draw_landmarks(self, frame, results):
        # Draw pose landmarks on the frame.
        if results.pose_landmarks:
            self.mp_drawing.draw_landmarks(
                frame, 
                results.pose_landmarks, 
                self.mp_pose.POSE_CONNECTIONS,
                self.mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=4),
                self.mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2)
            )

    def save_screenshot(self, frame):
        current_time = time.time()
        if current_time - self.last_screenshot_time >= self.screenshot_interval:
            screenshot_filename = os.path.join(self.screenshot_dir, f"screenshot_{self.screenshot_count}.png")
            try:
                cv2.imwrite(screenshot_filename, frame)
                print(f"Screenshot saved as {screenshot_filename}")
                self.last_screenshot_time = current_time
                self.screenshot_count += 1
            except Exception as e:
                print(f"Error saving screenshot: {e}")

def main():
    # Capture video from webcam (or replace with video file path).
    cap = cv2.VideoCapture(0)
    detector = PoseDetector()

    if not cap.isOpened():
        print("Error: Could not open video capture")
        return

    while True:
        ret, frame = cap.read()
    
        if not ret:
            print("Error: Could not read frame")
            break

        result = detector.process_frame(frame)
        detector.draw_landmarks(frame, result)
        
        # Save screenshot if interval has passed
        detector.save_screenshot(frame)
        
        # Display the frame.
        cv2.imshow('Pose Detection', frame)

        # Break loop on 'q' key press.
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources.
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()