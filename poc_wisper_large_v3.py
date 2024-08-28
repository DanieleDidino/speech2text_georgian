import datetime
from transformers import pipeline
from transformers.pipelines.audio_utils import ffmpeg_read


MODEL_NAME = "openai/whisper-large-v3"
DEVICE = "cpu"

PATHS_AUDIO_FILE = "files_poc/path_audio_files.txt"


def get_file_paths() -> list[str]:
    with open(PATHS_AUDIO_FILE, "r") as text_file:
        lines = text_file.readlines()
    path_audio_files = []
    for line in lines:
        path_audio_files.append("files_poc/audio/" + line.strip())
    return path_audio_files


def define_pipeline(MODEL_NAME:str, device:str = "cpu") -> pipeline:

    pipe = pipeline(
        task="automatic-speech-recognition",
        model=MODEL_NAME,
        device=device,
    )
    return pipe


if __name__ == "__main__":
    
    # Load file
    paths_audio_file = get_file_paths()

    # Define pipeline
    pipe = define_pipeline(MODEL_NAME, DEVICE)

    # transcribe speech-to-text
    transcriptions = pipe(
        inputs = paths_audio_file,
        batch_size=1, # DEPENDS ON THE MEMORY AVAILABLE
        generate_kwargs={
            "language": "georgian"
        }
    )

    now = datetime.datetime.now()
    timestamp = now.strftime("%Y%m%d_%H%M%S")
    filename = f"files_poc/transcript_{timestamp}.txt"

    with open(filename, "w") as text_file:
        for transcription in transcriptions:
            text_file.write(transcription["text"])
            text_file.write("\n")
