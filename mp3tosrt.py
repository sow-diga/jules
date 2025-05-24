import os
import whisper
import argparse

# Function to transcribe audio and save as SRT
def transcribe_audio_to_srt(audio_file_path, model_name, output_srt_path, language): # language default removed
    if not os.path.isfile(audio_file_path):
        print(f"Audio file not found: {audio_file_path}")
        return

    print(f"Transcribing file: {audio_file_path} with language set to {language}")
    # Load the Whisper model
    whisper_model = whisper.load_model(model_name)
    result = whisper_model.transcribe(audio_file_path, language=language, verbose=False) # language passed

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

    # Ensure the output folder (part of output_srt_path) exists
    output_folder_for_srt = os.path.dirname(output_srt_path)
    if not os.path.exists(output_folder_for_srt):
        os.makedirs(output_folder_for_srt)

    # Save SRT file
    # audio_filename = os.path.basename(audio_file_path) # Not needed, srt_path is now full path
    # srt_filename = os.path.splitext(audio_filename)[0] + ".srt" # Not needed
    # srt_path = os.path.join(output_folder, srt_filename) # output_srt_path is now the full path

    with open(output_srt_path, "w", encoding="utf-8") as f:
        f.write(srt_content)
    print(f"SRT file saved: {output_srt_path}")

# Transcribe all mp3 files in the folder
def transcribe_all_files_in_folder(input_audio_folder, output_srt_folder, model_name, language): # defaults removed
    if not os.path.exists(input_audio_folder):
        print(f"Folder not found: {input_audio_folder}")
        return

    # Get all mp3 files in the folder
    audio_files = [os.path.join(input_audio_folder, f) for f in os.listdir(input_audio_folder) if f.endswith(".mp3")]

    if not audio_files:
        print(f"No MP3 files found in folder: {input_audio_folder}")
        return

    # Ensure the output folder exists
    if not os.path.exists(output_srt_folder):
        os.makedirs(output_srt_folder)

    for audio_file_path in audio_files:
        try:
            base_filename = os.path.basename(audio_file_path)
            srt_filename = os.path.splitext(base_filename)[0] + ".srt"
            full_output_srt_path = os.path.join(output_srt_folder, srt_filename)
            transcribe_audio_to_srt(audio_file_path, model_name, full_output_srt_path, language=language)
        except Exception as e:
            print(f"Error processing {audio_file_path}: {e}")

# Run the transcription
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Transcribe MP3 audio files to SRT subtitles using OpenAI Whisper.")
    parser.add_argument(
        "--input_folder",
        type=str,
        default="downloads",
        help="Folder containing the MP3 files. Default is 'downloads'."
    )
    parser.add_argument(
        "--output_folder",
        type=str,
        default="transcribed",
        help="Folder to save the SRT files. Default is 'transcribed'."
    )
    parser.add_argument(
        "--model",
        type=str,
        default="medium",
        help="Whisper model to use (e.g., tiny, base, small, medium, large). Default is 'medium'."
    )
    parser.add_argument(
        "--language",
        type=str,
        default="ar",
        help="Language code for transcription (e.g., en, es, fr). Default is 'ar' (Arabic)."
    )

    args = parser.parse_args()

    # Transcribe all mp3 files using the provided or default arguments
    transcribe_all_files_in_folder(args.input_folder, args.output_folder, args.model, args.language)
