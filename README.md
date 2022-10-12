# **Roko!**

## Acerca de **Roko!**

**Roko!** es un programa que te permite playlist y videos de **YouTube** de manera sencilla.

#### ¿Qué puedes hacer con **Roko!**? 🤯

1. Puedes descargar **videos**.
2. Puedes descargar solamente el **audio** de los videos.
3. Puedes descargar **playlist** completas.

#### ¿Cómo utilizar **Roko!**? 👀

- Primero debes insertar el enlace del video que quieras descargar.
- Después debes seleccionar la carpeta de salida.
- Antes de iniciar la descarga debes seleccionar si quieres descargar audio o video.
- Finalmente inicias la descarga.

![Main](/assets/RokoWindow.png)

### Métodos de instalación: 

#### Descarga **Roko!** 📦:
1. **En Windows** 💻:

    Haz click [aquí](https://github.com/MilfuegosxD/Roko-/releases/tag/v1.0.1) para descargar **Roko! v1.0.1** e instalar.🎵



#### Clona el repositorio 📚:
> Verifica de tener [Python](https://www.python.org/downloads/release/python-3107/) y [Git](https://git-scm.com/download) instalados en tu equipo 😁

1. Clona el repositorio 🧲:

       git clone https://github.com/MilfuegosxD/Roko-

2. Entra al repositorio 📁:

       cd Roko-

3. Crear un [entorno virtual](https://docs.python.org/es/3/glossary.html#term-virtual-environment) 💻:

       python -m venv .env

   > [¿Cómo crear un entorno virtual?](https://www.freecodecamp.org/espanol/news/entornos-virtuales-de-python-explicados-con-ejemplos/) 🤯

4. Activa el entorno virtual ✅:

    - **En Windows** 💻:
    
          .env/Scripts/activate
    
      > Asegúrate de [habilitar la ejecución de scripts.](https://es.stackoverflow.com/questions/321611/problema-con-scripts-en-visual-studio-code) 👀

    - **En Linux** 💻:
    
          source /.env/bin/activate

5. Instala las dependencias 📦:
    
   - Paquetes y modulos necesarios 📝: 

         pip install -r requirements.txt
      
   - Instalar ffmpeg 📦:
      
       - **En Windows** 💻:
        
         Haz click a la imagen para descargar 😎
         [!["Download](/assets/ffmpeg.png)](https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-full.7z)
        
         > Necesitas un programa que sea capaz de descomprimir archivos .7z si no lo tienes puedes descargar [7zip](https://www.7-zip.org/).

         Una vez hayas descomprimido el archivo debes mover los siguientes archivos al directorio **.env/Scripts**
         ![ffmpegfiles](/assets/ffmpegfiles.png)

       - **En Linux**

           Haz click [aquí](https://www.hostinger.es/tutoriales/instalar-ffmpeg-linux#:~:text=Para%20instalar%20FFmpeg%20en%20Debian,el%20repositorio%20oficial%20de%20Debian.) para obtener más información 😜


6. Ejecuta el programa 🎧:
      - **En Windows** 💻

             python src\Roko.py
      
      - **En linux** 💻 

             python3 src\Roko.py
#### Preguntas frecuentes:
- ¿Por qué mi video no ha sido descargado?

Lo más probable es que el video sea privado o que no esté disponible en el país.

- ¿Se le puede bajar la calidad al video o audio?

No, por el momento no hemos implementado esa opción.





Desarrollado por: [MilfuegosxD](https://github.com/MilfuegosxD)
