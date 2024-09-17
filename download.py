import yt_dlp
import os

# Cores ANSI para mensagens
VERDE = "\033[92m"
VERMELHO = "\033[91m"
RESET = "\033[0m"

def baixar_video(url, pasta_destino):
    try:
        # Cria a pasta de destino se não existir
        if not os.path.exists(pasta_destino):
            os.makedirs(pasta_destino)

        # Configura opções para baixar na melhor qualidade
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': os.path.join(pasta_destino, '%(title)s.%(ext)s'),
            'noplaylist': True,  # Evita baixar playlists inteiras
            'quiet': True,      # Suprime a saída padrão de yt-dlp
            'progress_hooks': [mostrar_progresso]
        }

        # Inicia o download
        print(f"{VERDE}DOWNLOAD INICIADO{RESET}")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            video_title = info.get('title', 'Desconhecido')
            print(f"{VERDE}VÍDEO: {video_title}{RESET}")
            ydl.download([url])
        print(f"{VERDE}DOWNLOAD CONCLUÍDO!{RESET}")

    except Exception as e:
        print(f"{VERMELHO}VÍDEO NÃO ENCONTRADO{RESET}")
        print(f"{VERMELHO}Erro: {e}{RESET}")

def mostrar_progresso(d):
    if d['status'] == 'downloading':
        percent_complete = d.get('downloaded_bytes', 0) / d.get('total_bytes', 1) * 100
        print(f"[download] {d['filename']} - {percent_complete:.2f}% completo")

if __name__ == "__main__":
    url_video = input(f"{VERDE}Digite a URL do vídeo do YouTube:{RESET} ")
    pasta_resultado = "results"
    baixar_video(url_video, pasta_resultado)
