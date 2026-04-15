
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
    'format': 'bestaudio/best',
    'noplaylist': True,
    'extractaudio': True,
    'quiet': True,
    'no_warnings': True,
    'progress_hooks': [progreso],
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': formato,
        'preferredquality': '320'
    }],
    'outtmpl': f'{name}.%(ext)s'
}


#extra el audio del video 
with yt_dlp.YoutubeDL(opciones) as ydl:
    ydl.download([url])
