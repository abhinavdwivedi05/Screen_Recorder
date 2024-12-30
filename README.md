
# Screen Recording Script

This Python script allows you to record your screen for a user-defined duration and save the video with a custom name in the same directory where the script is located. It uses **OpenCV** and **PyAutoGUI** to capture the screen and create a video file.

## Requirements

- Python 3.x
- Libraries:
  - `opencv-python`
  - `pyautogui`
  - `numpy`
  - `pywin32`

You can install the required libraries using `pip`:

```bash
pip install opencv-python pyautogui numpy pywin32
```

## Usage

1. Clone or download this repository.
2. Navigate to the folder where the script is located.
3. Run the script:

```bash
python screen_recorder.py
```

4. When prompted:
   - Enter the name for the video file (e.g., `recording.mp4`).
   - Enter the duration (in seconds) for the screen recording.

The video will be saved in the same directory as the script with the name you provided.

## Features

- Customizable video name.
- User-defined recording duration.
- Saves video in the current directory.
- Uses XVID codec for video encoding.

## Example

```bash
Enter the name for the video: my_recording.mp4
Enter The duration for screen recording in seconds: 10
****Recording Started****
---Video has been stored in same directory as the code---
```

## License

This project is open-source and available under the [MIT License](LICENSE).
