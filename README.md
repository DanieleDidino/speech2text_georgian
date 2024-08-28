<h1 align="center">Speech To Text - Georgian Language</h1>

This is a POC to transcribe Georgian audio files into text.

It uses the OpenAI model `whisper-large-v3`.

TO DO
1. Add **Attention Masking**
2. Test other models
3. Preprocess audio


## Installation

#### Python version: 3.10.12 

#### 1. Clone the repository

with HTTPS
```bash
git clone https://github.com/DanieleDidino/speech2text_georgian.git
```

with SSH
```bash
git clone git@github.com:DanieleDidino/speech2text_georgian.git
```

#### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

#### 3. Activate the virtual environment and install dependencies

```bash
source .venv/bin/activate
pip install -r requirements.txt
```

#### 4. Add the audio files

- Add the audio files in the folder `/files_poc/audio`.
- Add the names of the audio files in the txt file `files_poc/path_audio_files.txt`.

#### 5. Run the script to transcribe the audio

```bash
python3 poc_wisper_large_v3.py
```

The transcriptions are stored in the file in the folder `files_poc`.

The file name includes the date and the time.

Example of file name: `transcript_20240828_131440.txt`.

#### 6. Deactivate the virtual environment

After generating the synthetic data and the dynamic few-shot prompt, you can deactivate the virtual environment:

```bash
deactivate
```
