import os
import whisper

# Paths
audio_folder = "downloads"          # Folder containing the mp3 files
transcribed_folder = "transcribed"  # Folder to save the SRT files

# Function to transcribe audio and save as SRT
def transcribe_audio_to_srt(audio_file, model, output_folder, language="ar"):
    if not os.path.isfile(audio_file):
        print(f"Audio file not found: {audio_file}")
        return

    print(f"Transcribing file: {audio_file} with language set to Arabic")
    # Load the Whisper model
    whisper_model = whisper.load_model(model)
    result = whisper_model.transcribe(audio_file, language=language, verbose=False)

    # Create SRT content
    srt_content = ""
    for i, segment in enumerate(result['segments']):
        start = segment['start']
        end = segment['end']
        text = segment['text'].strip()

        # Format timestamps for SRT
        start_time = f"{int(start // 3600):02}:{int((start % 3600) // 60):02}:{int(start % 60):02},{int((start % 1) * 1000):03}"
        end_time = f"{int(end // 3600):02}:{int((end % 3600) // 60):02}:{int(end % 60):02},{int((end % 1) * 1000):03}"

        srt_content += f"{i + 1}\n{start_time} --> {end_time}\n{text}\n\n"

    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Save SRT file
    audio_filename = os.path.basename(audio_file)
    srt_filename = os.path.splitext(audio_filename)[0] + ".srt"
    srt_path = os.path.join(output_folder, srt_filename)

    with open(srt_path, "w", encoding="utf-8") as f:
        f.write(srt_content)
    print(f"SRT file saved: {srt_path}")

# Transcribe all mp3 files in the folder
def transcribe_all_files_in_folder(folder, output_folder, model="medium", language="ar"):
    if not os.path.exists(folder):
        print(f"Folder not found: {folder}")
        return

    # Get all mp3 files in the folder
    audio_files = [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith(".mp3")]

    if not audio_files:
        print(f"No MP3 files found in folder: {folder}")
        return

    for audio_file in audio_files:
        try:
            transcribe_audio_to_srt(audio_file, model, output_folder, language=language)
        except Exception as e:
            print(f"Error processing {audio_file}: {e}")

# Run the transcription
if __name__ == "__main__":
    # Set the Whisper model to 'medium'
    whisper_model = "medium"

    # Transcribe all mp3 files in the downloads folder with Arabic language
    transcribe_all_files_in_folder(audio_folder, transcribed_folder, model=whisper_model, language="ar")
