import cv2
from datetime import datetime

def main():
    # Initialize the camera (0 is the default camera)
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 448)

    # Set the frame rate
    cap.set(cv2.CAP_PROP_FPS, 24)
    
    if not cap.isOpened():
        print("Error: Could not open video capture.")
        return


    print(f"Frame dimensions: 640x480")

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        cv2.putText(frame, datetime.now().strftime("%Y-%m-%d %H-%M-%S") , (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 1, cv2.LINE_AA)

        if not ret:
            print("Error: Failed to capture frame.")
            break

        # Display the resulting frame
        #cv2.imshow('Camera Feed', frame)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture and close windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
