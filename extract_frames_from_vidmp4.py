"""
Script to extract frames from all videos in a directory
Author: Maxime
Date: 2023-10-10

Description:
This script extracts frames from all videos in a specified directory at regular intervals and saves them to separate output directories.
"""

# Standard modules
import os

# Third-party modules
import cv2

# Constants
INPUT_VIDEO_DIR = 'vid'  # Directory containing input videos
OUTPUT_BASE_DIR = 'extracted_frames'  # Base directory for output frames
FRAME_INTERVAL = 30  # Interval between extracted frames
SUPPORTED_VIDEO_FORMATS = ('.mp4', '.avi', '.mov', '.mkv')  # Supported video formats


def create_output_dir(output_dir):
    """
    Creates the output directory if it doesn't exist.

    Args:
        output_dir (str): Path to the output directory.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Output directory created: {output_dir}")


def extract_frames(video_path, output_dir, frame_interval):
    """
    Extracts frames from a video and saves them to a directory.

    Args:
        video_path (str): Path to the video.
        output_dir (str): Output directory for frames.
        frame_interval (int): Interval between extracted frames.
    """
    # Create the output directory
    create_output_dir(output_dir)

    # Load the video
    cap = cv2.VideoCapture(video_path)

    # Check if the video was opened successfully
    if not cap.isOpened():
        print(f"Error: Unable to open video {video_path}.")
        return

    frame_count = 0
    saved_frame_count = 0

    while True:
        # Read the next frame
        ret, frame = cap.read()

        if not ret:
            break  # End of video

        frame_count += 1

        # Save every n-th frame
        if frame_count % frame_interval == 0:
            frame_filename = os.path.join(output_dir, f"frame_{saved_frame_count + 1}.jpg")
            cv2.imwrite(frame_filename, frame)
            saved_frame_count += 1
            print(f"Frame {saved_frame_count} saved: {frame_filename}")

    # Release the video capture object
    cap.release()
    print(f"Extraction complete. {saved_frame_count} frames saved in {output_dir}.")


def process_all_videos(input_dir, output_base_dir, frame_interval):
    """
    Processes all videos in the input directory and extracts frames.

    Args:
        input_dir (str): Directory containing input videos.
        output_base_dir (str): Base directory for output frames.
        frame_interval (int): Interval between extracted frames.
    """
    # Create the base output directory if it doesn't exist
    create_output_dir(output_base_dir)

    # Iterate through all files in the input directory
    for filename in os.listdir(input_dir):
        # Check if the file is a supported video format
        if filename.lower().endswith(SUPPORTED_VIDEO_FORMATS):
            video_path = os.path.join(input_dir, filename)
            video_name = os.path.splitext(filename)[0]  # Get video name without extension
            output_dir = os.path.join(output_base_dir, video_name)  # Create a subdirectory for this video

            print(f"Processing video: {filename}")
            extract_frames(video_path, output_dir, frame_interval)
        else:
            print(f"Skipping unsupported file: {filename}")


def main():
    """
    Main function of the script.
    """
    process_all_videos(INPUT_VIDEO_DIR, OUTPUT_BASE_DIR, FRAME_INTERVAL)


if __name__ == "__main__":
    main()