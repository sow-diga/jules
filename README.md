# MP3 to SRT Transcription Tool
This script transcribes MP3 audio files to SRT (SubRip Text) subtitle files using OpenAI's Whisper model. It processes all MP3 files in a specified input folder and saves the corresponding SRT files to an output folder.

## Features
* Transcribes MP3 audio to SRT subtitles.
* Uses OpenAI's Whisper model for transcription.
* Processes all MP3 files in a specified input folder.
* Saves SRT files to a specified output folder.
* Creates output folder if it doesn't exist.

## Requirements
* Python 3.7+
* OpenAI Whisper library
* `ffmpeg` installed and in PATH

## Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/mp3-to-srt-transcription.git
   cd mp3-to-srt-transcription
   ```
2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Install ffmpeg:**
   Follow the instructions for your operating system to install `ffmpeg`. Make sure it's added to your system's PATH.
   * **Ubuntu/Debian:** `sudo apt update && sudo apt install ffmpeg`
   * **macOS (using Homebrew):** `brew install ffmpeg`
   * **Windows:** Download from [ffmpeg.org](https://ffmpeg.org/download.html) and add the `bin` directory to your PATH.

## Configuration
The script `mp3tosrt.py` is configured primarily through command-line arguments. These arguments allow you to specify input and output folders, the Whisper model to use, and the language for transcription. The available arguments are detailed in the "Usage" section below.

If no arguments are provided, the script will use the following default values:
*   **Input Folder:** `downloads` (The script will look for MP3 files in a folder named "downloads" in the same directory as the script)
*   **Output Folder:** `transcribed` (SRT files will be saved in a folder named "transcribed" in the same directory as the script)
*   **Whisper Model:** `medium`
*   **Language:** `ar` (Arabic)

You can override these defaults by providing the respective command-line arguments as shown in the "Usage" section.

## Usage
Run the script from the command line.

To run with default settings (input: `downloads`, output: `transcribed`, model: `medium`, language: `ar`):
```bash
python mp3tosrt.py
```

To specify custom settings, use the arguments below.

**Arguments:**
* `--input_folder`: (Optional) Path to the folder containing MP3 files. Defaults to `downloads` in the script's directory.
* `--output_folder`: (Optional) Path to the folder where SRT files will be saved. Defaults to `transcribed` in the script's directory.
* `--model`: (Optional) Whisper model to use (e.g., `tiny`, `base`, `small`, `medium`, `large`). Defaults to `medium`.
* `--language`: (Optional) Language code for transcription (e.g., `en`, `es`, `fr`). Defaults to `ar` (Arabic).

**Example of overriding defaults:**
The following command transcribes English audio from `./samples/mp3` to SRT files in `./samples/srt`, using the `small` model:
```bash
python mp3tosrt.py --input_folder ./samples/mp3 --output_folder ./samples/srt --model small --language en
```

## Script Details (`mp3tosrt.py`)
The Python script `mp3tosrt.py` performs the following actions:
1. **Parses Command-Line Arguments:**
   - `input_folder`: Specifies the directory containing the MP3 files to be transcribed. (Defaults to `downloads` if not provided).
   - `output_folder`: Specifies the directory where the generated SRT files will be saved. (Defaults to `transcribed` if not provided).
   - `model`: (Optional) Specifies the Whisper model size (default: `medium`).
   - `language`: (Optional) Specifies the language of the audio (default: `ar` - Arabic).
2. **Loads Whisper Model:** Initializes the specified Whisper model.
3. **Processes MP3 Files:**
   - Iterates through each file in the `input_folder`.
   - Checks if the file is an MP3 file (ends with `.mp3`).
   - If it is, it proceeds to transcribe the audio.
4. **Transcribes Audio:**
   - Uses the loaded Whisper model to transcribe the audio from the MP3 file.
   - The `model.transcribe()` method returns a dictionary containing the transcription text and segments.
5. **Formats Transcription to SRT:**
   - Iterates through the segments obtained from the transcription.
   - For each segment, it extracts the start time, end time, and text.
   - Formats this information into the standard SRT format:
     ```
     Segment Index
     HH:MM:SS,mmm --> HH:MM:SS,mmm
     Segment Text
     ```
   - The timestamps are converted to the `HH:MM:SS,mmm` format.
6. **Saves SRT File:**
   - Constructs the output SRT filename based on the input MP3 filename (e.g., `audio.mp3` -> `audio.srt`).
   - Creates the `output_folder` if it does not already exist.
   - Writes the formatted SRT content to the corresponding file in the `output_folder`.
   - Prints a confirmation message indicating the successful creation of the SRT file.
7. **Handles Errors:**
   - Includes basic error handling for file operations and transcription processes (though more robust error handling could be added).

## Contributing
Contributions are welcome! If you have suggestions for improvements or find any issues, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
