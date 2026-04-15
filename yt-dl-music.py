
#importar librerias
import argparse 
import yt_dlp

#generador de variables y argumentos dentro del codigo
parser = argparse.ArgumentParser(description="Descargador de audio para YouTube")

parser.add_argument("-u", "--url", required=True, help="URL del video de youtube que quieres pasar a audio")
parser.add_argument("-f", "--format", default="mp3", help="Formato de salida (flac, m4a, wav, aac, opus, mp3)")
parser.add_argument("-n", "--name", default="audio", help="Nombre del archivo (No poner extencion en el nombre)")

args = parser.parse_args()


#variables
url = args.url
formato = args.format
name = args.name


#barra de progreso
def progreso(d):
    if d['status'] == 'downloading':
        porcentaje = d.get('_percent_str', '').strip()
        velocidad = d.get('_speed_str', '').strip()
        eta = d.get('_eta_str', '').strip()

        print(f"\rDescargando {porcentaje} | Velocidad {velocidad} | ETA {eta}", end="")
    
    if d['status'] == 'finished':
        print("\n✔ Descarga terminada")


#opciones de descarga de musica
opciones = {
    'format': 'bestaudio[ext=m4a]/bestaudio/best',
    'quiet': True,
    'no_warnings': True,
    'noplaylist': True,
    'outtmpl': f'{name}.%(ext)s',
    'progress_hooks': [progreso],

    # 🔥 CLAVE PARA 403
    'extractor_args': {
        'youtube': {
            'player_client': ['android']
        }
    },

    # 🔥 HEADERS tipo navegador
    'http_headers': {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/122 Safari/537.36',
        'Referer': 'https://www.youtube.com/'
    },

    # estabilidad
    'retries': 20,
    'fragment_retries': 20,
    'concurrent_fragment_downloads': 1,

    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': formato,
        'preferredquality': '0',
    }],
}


#extra el audio del video 
with yt_dlp.YoutubeDL(opciones) as ydl:
    ydl.download([url])
