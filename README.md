# Scripts de Gravação e Transcrição de Áudio

Este repositório contém dois scripts Python para gravação de áudio e transcrição automática utilizando o modelo Whisper da OpenAI.

## Scripts

### 1. `gravador.py`
- **O que faz:**
  - Permite gravar áudio do microfone pressionando a tecla Enter para iniciar e parar a gravação.
  - Salva o áudio em um arquivo WAV.
  - Transcreve automaticamente o áudio gravado usando o modelo Whisper.
  - Exibe a transcrição no terminal.

- **Como instalar as dependências:**
  ```powershell
  pip install openai-whisper sounddevice numpy scipy keyboard
  # O Whisper instala o PyTorch automaticamente, mas para melhor desempenho (ex: GPU), siga as instruções em https://pytorch.org/get-started/locally/
  ```

- **Como rodar:**
  ```powershell
  python gravador.py
  ```

### 2. `main.py`
- **O que faz:**
  - Transcreve um arquivo de áudio existente (ex: `audio.mp3` ou `audio.mp4`) usando o modelo Whisper.
  - Exibe a transcrição no terminal.

- **Como instalar as dependências:**
  ```powershell
  pip install openai-whisper
  # O Whisper instala o PyTorch automaticamente, mas para melhor desempenho (ex: GPU), siga as instruções em https://pytorch.org/get-started/locally/
  # É necessário ter o ffmpeg instalado e disponível no PATH do sistema.
  ```

- **Como rodar:**
  ```powershell
  python main.py
  ```
  - Certifique-se de que o arquivo de áudio (`audio.mp3` ou `audio.mp4`) está na mesma pasta do script ou ajuste o caminho no código.

## Observações
- O Whisper suporta diversos idiomas. Para alterar o idioma da transcrição, modifique o parâmetro `language` nos scripts.
- Para melhor desempenho, utilize uma GPU compatível e instale o PyTorch com suporte CUDA.
- Consulte a documentação oficial do Whisper: https://github.com/openai/whisper
