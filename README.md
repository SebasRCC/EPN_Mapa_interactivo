# 🤖🗺️ Campus Bot EPN - Mapa Interactivo

Bienvenido al proyecto **Campus Bot EPN**: un asistente inteligente que te ayuda a **encontrar facultades, departamentos y lugares clave** dentro del campus de la **Escuela Politécnica Nacional** 🇪🇨, todo con una sola pregunta.

---

## 🌟 ¿Qué hace este proyecto?

Campus Bot EPN:

🗣️ Permite que los usuarios hagan preguntas como:  
> _"¿Dónde está la facultad de sistemas?"_  
> _"¿Dónde queda el gimnasio?"_

🧠 Reconoce automáticamente alias comunes o coloquiales para cada lugar (como "sistemas", "dee", "bombonera").

📍 Muestra la ubicación exacta en un **mapa interactivo** usando Leaflet.

📌 Si el usuario permite su ubicación, ¡Campus Bot traza la ruta desde donde estás hasta el lugar que buscas!

🖼️ Incluye una interfaz gráfica atractiva con banners institucionales.

---

## 🚀 ¿Cómo ejecutar el proyecto?

Sigue estos pasos para correr el bot en tu computador:

1. ✅ Asegúrate de tener **Python 3.7+** instalado.
    - Puedes verificarlo con:  
      ```bash
      python --version
      ```

2. 📦 Instala Flask (y cualquier otro paquete necesario):
    - Si tienes un archivo `requirements.txt`, ejecuta:
      ```bash
      pip install -r requirements.txt
      ```
    - O manualmente:
      ```bash
      pip install flask
      ```

3. 📁 Asegúrate de tener estos archivos en el proyecto:
    - `app.py` (el servidor Flask)
    - `lugares_epn.json` (base de datos de lugares y alias)
    - `templates/index.html` (interfaz web)
    - Carpeta `static/` con imágenes y banners

4. ▶️ Ejecuta el servidor con:
    ```bash
    python app.py
    ```

5. 🌐 Abre tu navegador en:  
    [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🧠 ¿Cómo funciona la lógica del bot?

- El bot **normaliza** las preguntas eliminando tildes, mayúsculas, etc.
- Luego busca coincidencias con los **alias de cada lugar** en la base de datos `lugares_epn.json`.
- Si encuentra una coincidencia, devuelve la **ubicación geográfica** y la despliega en el mapa.
- Si el navegador lo permite, obtiene tu ubicación actual y traza la **ruta** hacia el destino.

---

## 🧩 Tecnologías usadas

- ⚙️ **Python 3** y **Flask** – Backend ligero
- 📍 **Leaflet.js** – Mapa interactivo
- 📡 **Geolocalización del navegador**
- 🗂️ **JSON** – Base de datos de lugares
- 🎨 HTML + CSS – Interfaz responsiva

---




## 📬 Contribuciones

¡Tus aportes son bienvenidos! Puedes:
- Añadir más lugares o alias al `lugares_epn.json`
- Mejorar el diseño visual de la interfaz
- Expandir funcionalidades del bot (por ejemplo, horario de oficinas, eventos, etc.)

---

## 🏫 Hecho para la Escuela Politécnica Nacional

> Proyecto académico para la materia de Inteligencia Ariticial

---

## 🧑‍💻 Autores

Sebas Ramos – [GitHub](https://github.com/tu-usuario)
Juan Mateo Quisilema - [GitHub](https://github.com/JuanMateoQ)
Jhair Zambrano - [GitHub](https://github.com/Jhairzp27)

---

## ⚠️ Licencia

Este proyecto está bajo la licencia MIT.  
Puedes usarlo, modificarlo y distribuirlo libremente con atribución.

