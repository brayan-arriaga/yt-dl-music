# yt-dl-music

**yt-dl-music** es una herramienta CLI escrita en Python que permite **descargar el audio de videos de YouTube en la mejor calidad posible** y convertirlo a diferentes formatos desde la terminal.

Utiliza yt-dlp para descargar el audio y FFmpeg para convertirlo automáticamente al formato deseado.

---

# Características

* Descarga audio desde videos de YouTube
* Convierte automáticamente el audio al formato elegido
* Descarga el **mejor audio disponible**
* Funciona completamente desde la **terminal**
* Herramienta **ligera y simple**

---

# Requisitos

Antes de usar la herramienta necesitas instalar:

* Python 3
* yt-dlp
* FFmpeg

---

# Instalación

Clona el repositorio:

```bash
git clone https://github.com/brayan-arriaga/yt-dl-music
```

Entra al directorio del proyecto:

```bash
cd yt-dl-music
```

Instala las dependencias:

```bash
pip install yt-dlp
pip install ffmpeg
```

Da permisos de ejecución al script:

```bash
chmod +x yt-dl-music.py
```

---

# Uso

Ejecuta el programa con:

```bash
python3 yt-dl-music.py -u URL -n nombre -f formato
```

---

# Argumentos

| Argumento       | Descripción                  |
| --------------- | ---------------------------- |
| `-u` `--url`    | URL del video de YouTube     |
| `-n` `--name`   | Nombre del archivo de salida |
| `-f` `--format` | Formato del audio            |

---

# Formatos soportados

Los formatos disponibles son:

* mp3
* flac
* m4a
* aac
* opus
* wav

---

# Ejemplo

```bash
python3 yt-dl-music.py \
-u "https://www.youtube.com/watch?v=4gZdE5dimMg" \
-n "mi_cancion" \
-f mp3
```

Esto descargará el audio del video y lo guardará como:

```
mi_cancion.mp3
```

---

# Sistema operativo

Actualmente probado en:

* Linux



