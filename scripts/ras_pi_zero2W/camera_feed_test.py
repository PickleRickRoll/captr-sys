import cv2  # Import the OpenCV library for video and image processing
from datetime import datetime  # Import the datetime module to handle date and time

def main():
    """
    CHANGE YOUR DIMENSIONS HERE ACCORDING TO YOUR CAMERA PROPERTIES FOR TESTING
    """
    # Initialize the camera (0 is the default camera)
    cap = cv2.VideoCapture(0)  # Open a connection to the camera
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800)  # Set the frame width to 800 pixels
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 448)  # Set the frame height to 448 pixels

    # Set the frame rate
    # cap.set(cv2.CAP_PROP_FPS, 24)  # Optionally set the frames per second to 24

    if not cap.isOpened():  # Check if the camera opened successfully
        print("Error: Could not open video capture.")  # Print an error message if the camera did not open
        return  # Exit the function

    w = cap.get(3)  # Get the frame width
    h = cap.get(4)  # Get the frame height
    print('width=', w)  # Print the frame width
    print('height=', h)  # Print the frame height
    print('capturing fps = ', cap.get(5))  # Print the frames per second

    while True:  # Start an infinite loop to continuously capture frames
        # Capture frame-by-frame
        ret, frame = cap.read()  # Read a frame from the camera
        cv2.putText(frame, datetime.now().strftime("%Y-%m-%d %H-%M-%S"), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 1, cv2.LINE_AA)
        # Overlay the current date and time on the frame

        if not ret:  # Check if the frame was captured successfully
            print("Error: Failed to capture frame.")  # Print an error message if the frame was not captured
            break  # Exit the loop

        # Display the resulting frame. Uncommenting the next line will display the frame in a window, but it may cause lag.
        # cv2.imshow('Camera Feed', frame)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):  # Wait for 1 millisecond for a key press and check if it is 'q'
            break  # Exit the loop if 'q' is pressed

    # When everything is done, release the capture and close windows
    cap.release()  # Release the camera resource
    cv2.destroyAllWindows()  # Close all OpenCV windows

if __name__ == "__main__":
    main()  # Call the main function if this script is executed directly

