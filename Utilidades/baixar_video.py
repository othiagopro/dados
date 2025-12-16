import yt_dlp
import os

def baixar_alta_resolucao(url):
    # Verifica se o ffmpeg.exe está na mesma pasta do script
    if os.path.isfile('ffmpeg.exe'):
        print("✅ FFmpeg encontrado! Baixando em ALTA QUALIDADE...")
        ffmpeg_local = './ffmpeg.exe'
    else:
        print("⚠️ FFmpeg não encontrado na pasta do script.")
        print("Tentando baixar usando o FFmpeg do sistema (se houver)...")
        ffmpeg_local = None # Tenta usar o do sistema

    ydl_opts = {
        'format': 'bestvideo+bestaudio/best', # Alta resolução
        'merge_output_format': 'mp4',
        'outtmpl': '%(title)s.%(ext)s',
        'ffmpeg_location': ffmpeg_local, # Usa o arquivo local se existir
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("\n✅ Sucesso! Vídeo baixado em alta resolução.")
    except Exception as e:
        print("\n❌ Erro crítico.")
        print(f"Detalhe: {e}")
        if "ffmpeg" in str(e).lower():
            print("\nSOLUÇÃO: Baixe o ffmpeg.exe e coloque NESTA PASTA: " + os.getcwd())

if __name__ == "__main__":
    url = input("URL: ")
    baixar_alta_resolucao(url)