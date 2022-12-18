import os
import subprocess
import threading
import warnings
warnings.filterwarnings("ignore")

def process_video(input_dir, output_dir, file_name , splitval = "5"):
    """
    Processes a video file by splitting it into segments, extracting frames and audio from each segment, and saving the
    results in the output directory.

    Parameters:
        input_dir (str): The directory containing the input video file.
        output_dir (str): The directory where the processed data will be saved.
        file_name (str): The name of the input video file.
        splitval (str): The time in seconds to split the video file
    """
    # Create a new directory with the file name in the output directory
    destination_folder = file_name.split(".")[0]
    new_dir = os.path.join(output_dir, destination_folder)
    os.makedirs(new_dir)

    # Create subdirectories for split video, frames, and audio
    splitvideosrc = os.path.join(new_dir, "splitvideo")
    os.makedirs(splitvideosrc)
    splitframessrc = os.path.join(new_dir, "splitframes")
    os.makedirs(splitframessrc)
    splitaudiosrc = os.path.join(new_dir, "splitaudio")
    os.makedirs(splitaudiosrc)

    # Set the input and output file paths
    video_input_file = os.path.join(input_dir, file_name)
    video_output_template = os.path.join(splitvideosrc, "clip" + "_%03d.mp4")
    

    # Split the video into 5 second segments
    subprocess.run(["ffmpeg", "-i", video_input_file, "-vcodec", "copy", "-acodec", "copy", "-vsync", "0", "-async", "1", "-segment_time", splitval, "-reset_timestamps", "1", "-f", "segment", video_output_template])

    # Get the list of split video files
    splitvideolist = os.listdir(splitvideosrc)

    def extract_frames(input_file, output_template):
        """
        Extracts frames from a video file and saves them to the specified output template.

        Parameters:
            input_file (str): The path to the input video file.
            output_template (str): The template for the output frame filenames. The template should contain a format
                string (e.g. "%03d") that will be replaced with the frame number.
        """
        subprocess.run(["ffmpeg", "-i", input_file, "-vf", "fps=1", output_template])

    def extract_audio(input_file, output_file):
        """
        Extracts the audio from a video file and saves it to the specified output file.

        Parameters:
            input_file (str): The path to the input video file.
            output_file (str): The path to the output audio file.
        """
        #save the file as wav file
        subprocess.run(["ffmpeg", "-i", input_file, "-vn", "-acodec", "pcm_s16le", "-ar", "44100", "-ac", "2", output_file])
        # subprocess.run(["ffmpeg", "-i", input_file, "-vn", "-acodec", "libmp3lame", output_file])

    # Extract frames and audio from each split video in parallel
    threads = []
    for i in splitvideolist:
        # Create a new subdirectory for each split video
        clipdir = os.path.join(splitframessrc, i.split(".")[0])
        os.makedirs(clipdir)

        # Get the input file path
        inputfile = os.path.join(splitvideosrc, i)
        frame_output_template = os.path.join(clipdir, "frame" + "_%03d.jpg")

        # Extract frames in a new thread
        thread = threading.Thread(target=extract_frames, args=(inputfile, frame_output_template))
        thread.start()
        threads.append(thread)

        # Extract audio in a new thread
        outputfile = os.path.join(splitaudiosrc, i.split(".")[0] + ".wav")
        thread = threading.Thread(target=extract_audio, args=(inputfile, outputfile))
        thread.start()
        threads.append(thread)