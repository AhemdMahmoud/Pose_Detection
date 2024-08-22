# Pose Detection with OpenCV and MediaPipe

This project implements real-time pose detection using a webcam feed, leveraging OpenCV for video capture and MediaPipe for pose estimation.

## Features

- Real-time pose detection from webcam feed
- Visualization of pose landmarks on the video stream
- Automatic screenshot capture at specified intervals

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7 or higher
- OpenCV (`cv2`)
- MediaPipe
- Webcam or video input device

## Installation

1. Clone this repository:
   ```
   https://github.com/AhemdMahmoud/Pose_Detection.git
   cd pose-detection-project
   ```

2. Install the required packages:
   ```
   pip install opencv-python mediapipe
   ```

## Usage

Run the script using Python:

```
python pose_detection.py
```

- The program will access your webcam and display the video feed with pose landmarks overlaid.
- Screenshots will be automatically saved in the `images` folder at 5-second intervals.
- Press 'q' to quit the application.

## Configuration

You can modify the following parameters in the `PoseDetector` class:

- `screenshot_interval`: Change the interval (in seconds) between automatic screenshots.
- `screenshot_dir`: Modify the directory where screenshots are saved.

## Troubleshooting

If you encounter issues:

1. Ensure your webcam is properly connected and accessible.
2. Check that you have the necessary permissions to write to the `images` directory.
3. Verify that all required libraries are correctly installed.

## Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.

## License

This project is open source and available under the [MIT License](LICENSE).

## Contact

If you have any questions or feedback, please open an issue in the GitHub repository.
