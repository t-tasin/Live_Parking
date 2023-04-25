Live Parking Documentation

Project Name: Live Parking

1. Overview

Live Parking is a Python-based application that uses computer vision to monitor the availability of parking spaces in real-time. The application processes a bird's eye view video feed of a parking lot, detects occupied and unoccupied spaces, and displays the parking status on the screen. The application is useful for parking lot management and can help users identify available parking spaces quickly.

2. Modules and Dependencies

Live Parking relies on the following modules and libraries:

- OpenCV (cv2): For video processing, image manipulation, and rendering.
- Pickle: For storing and retrieving parking space coordinates.
- cvzone: For displaying text on the images.
- NumPy (np): For numerical operations.

3. Files and Functions

The project is divided into two files:

- Parking_Available.py: The main file that processes the video input and displays parking availability.
- TrackParkingSpace.py: A utility file to define parking space locations in the input image.

4. Parking_Available.py

The Parking_Available.py file processes video input from a bird's eye view of a parking lot and checks the availability of parking spaces.

Key features:
- Reads video input from a file ("Park_BirdEye.mp4").
- Processes each frame to detect occupied and unoccupied parking spaces.
- Highlights the parking spaces with different colors based on their availability.
- Displays the number of available parking spaces on the screen.

5. TrackParkingSpace.py

The TrackParkingSpace.py file is a utility script used to define the coordinates of parking spaces in the input image. The user can interactively mark parking spaces by clicking on the image.

Key features:
- Reads an input image of the parking lot ("ParkingLot_BirdEye.png").
- Allows the user to add parking space locations by left-clicking on the image.
- Allows the user to remove parking space locations by right-clicking on the image.
- Stores the parking space locations in a file ('CarParkPosition_v2') for later use.

6. Usage

To define parking space locations, execute the TrackParkingSpace.py file:

```
python TrackParkingSpace.py
```

Left-click on the image to add parking space locations, and right-click to remove them. Once the parking spaces are defined, close the window.

To run the Live Parking application, execute the Parking_Available.py file:

```
python Parking_Available.py
```

The application will process the video input and display the parking availability on the screen.

7. Customization

To use the Live Parking application with a different video or image source, replace the file names in Parking_Available.py and TrackParkingSpace.py with the desired file paths. Ensure that the new files have a similar bird's eye view perspective and adjust the parking space dimensions (width and height) accordingly.

8. License

Live Parking is an open-source project. Feel free to use, modify, and distribute the code as needed, following the terms and conditions of the license.
