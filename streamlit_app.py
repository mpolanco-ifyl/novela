import streamlit as st
import openai
import re

# Pide la clave de API de OpenAI al usuario
openai.api_key = st.text_input("Introduce tu clave de API de OpenAI:")

# Función para contar palabras
def count_words(text):
    words = re.findall(r'\w+', text)
    return len(words)

# Función principal de la aplicación
def main():
    st.title("Generador de escena de novela en español")

    # Preguntamos al usuario la consulta inicial
    st.write("Bienvenido al generador de escena de novela en español. ¿Qué tipo de escena te gustaría crear?")

    # Pedimos una sinopsis de la escena
    scene_synopsis = st.text_area("Escribe una breve sinopsis de la escena que quieres crear:")

    # Preguntamos por los personajes, si es necesario
    has_characters = st.radio("¿La escena incluye personajes?", ["Sí", "No"])
    if has_characters == "Sí":
        character_count = st.number_input("¿Cuántos personajes hay en la escena?", min_value=1, max_value=10, step=1)

        # Preguntamos por los nombres, roles y personalidades de cada personaje
        character_names = []
        character_roles = []
        character_personalities = []
        for i in range(character_count):
            name = st.text_input(f"Nombre del personaje #{i+1}", key=f"name_{i}")
            role = st.text_input(f"Papel del personaje #{i+1}", key=f"role_{i}")
            personality = st.text_area(f"Personalidad de {name}:", key=f"personality_{i}")
            character_names.append(name)
            character_roles.append(role)
            character_personalities.append(personality)

        # Preguntamos si hay diálogos en la escena
        has_dialogue = st.radio("¿La escena incluye diálogo?", ["Sí", "No"])

        # Preguntamos si se desea imitar un estilo o autor específico
        has_style = st.radio("¿Te gustaría imitar un estilo o autor específico?", ["Sí", "No"])
        if has_style == "Sí":
            style = st.text_input("¿Qué estilo o autor te gustaría imitar?")

        # Generamos la escena con GPT-3
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Genera una escena de novela que {scene_synopsis}.",
            max_tokens=3024,
            n=1,
            stop=None,
            temperature=0.7,
        )

        # Mostramos el resultado al usuario
        st.write(response.choices[0].text)

    # Mostramos el botón de reiniciar para que el usuario pueda volver a empezar
    if st.button("Reiniciar"):
        st.experimental_rerun()

if __name__ == "__main__":
    main()
