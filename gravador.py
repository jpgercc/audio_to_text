import whisper
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wavfile
import keyboard
import os

def record_audio(samplerate=16000, filename="audio.wav"):
    audio_buffer = []

    def callback(indata, frames, time, status):
        """
        Callback é usado pela lib sounddevice para capturar áudio do microfone.
        `indata` contém os dados de áudio capturados.
        `frames` é o número de quadros capturados.
        `time` é o tempo de captura.
        `status` contém informações sobre erros ou avisos.
        """
        if status:
            print(status)
        audio_buffer.append(indata.copy())

    print("Pressione 'Enter' para COMEÇAR a gravar.")
    keyboard.wait('enter')

    print("\nGRAVANDO... Pressione 'Enter' para parar.")
    with sd.InputStream(samplerate=samplerate, channels=1, dtype='int16', callback=callback):
        keyboard.wait('enter')

    print("Gravação PARADA. Processando...")
    recorded_audio = np.concatenate(audio_buffer, axis=0)
    wavfile.write(filename, samplerate, recorded_audio)
    print(f"Arquivo '{filename}' salvo.")
    return filename

def transcribe_audio(audio_path, model_name="base", language="pt"):
    """
    Lista de modelos disponíveis em: https://huggingface.co/openai/whisper-base
    Lista de idiomas suportados: pt, en, es, fr, de, it, nl, ru, zh, ja, ko, etc.
    """
    print(f"Carregando modelo Whisper ({model_name})...")
    model = whisper.load_model(model_name)

    print("Transcrevendo áudio...")
    result = model.transcribe(audio_path, language=language)

    print("\n--- Transcrição ---")
    print(result["text"])
    print("-------------------")
    return result["text"]

def main():
    audio_file = "microfone_audio.wav"
    
    # Grava o áudio
    recorded_file = record_audio(filename=audio_file)
    
    # Transcreve o áudio
    transcribed_text = transcribe_audio(recorded_file)
    
    # Opcional: Remover o arquivo de áudio
    # os.remove(recorded_file)
    # print(f"Arquivo '{recorded_file}' removido.")

if __name__ == "__main__":
    main()