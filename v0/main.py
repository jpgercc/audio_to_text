import whisper

model = whisper.load_model("base")
result = model.transcribe("audio.mp3", language="pt") # ou audio.mp4
print(result["text"])

# pip install whisper
# you need to install ffmpeg for this to work and make sure it's in your PATH
"""
O Whisper usa PyTorch por baixo. A maneira mais fácil de instalar é com pip, mas o ideal é seguir as instruções do site do PyTorch para a sua configuração (se tiver placa de vídeo NVIDIA, use a versão com CUDA). Ex: pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118 (se for CUDA 11.8).
"""