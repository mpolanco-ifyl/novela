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

    # Establecemos los valores de longitud de palabras para la escena de novela
    word_count = 1600

    # Preguntamos al usuario por una sinopsis de la escena
    st.write("Bienvenido al generador de escena de novela en español. Por favor, proporciona una breve sinopsis de la escena que te gustaría generar:")
    prompt = st.text_area("Escribe la sinopsis aquí:")

    # Preguntamos por los personajes, si es necesario
    has_characters = st.radio("¿La escena incluye personajes?", ["Sí", "No"])
    if has_characters == "Sí":
        character_count = st.number_input("¿Cuántos personajes hay en la escena?", min_value=1, max_value=10, step=1)

        # Preguntamos por los nombres, roles y personalidades de cada personaje
        character_names = []
        character_roles = []
        character_personalities = []
        for i in range(character_count):
            name = st.text_input(f"Nombre del personaje #{i+1}")
            role = st.text_input(f"Papel del personaje #{i+1}")
            personality = st.text_area(f"Personalidad del personaje #{i+1}")
            character_names.append(name)
            character_roles.append(role)
            character_personalities.append(personality)

    # Preguntamos por el estilo o autor que se desea imitar
    style = st.text_input("¿Qué estilo o autor te gustaría imitar en la escena?")

    # Preguntamos si la escena tiene diálogos
    has_dialogue = st.radio("¿La escena tiene diálogos?", ["Sí", "No"])

    # Generamos el contenido con GPT-3
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=word_count,
        n=1,
        stop=None,
        temperature=0.7,
    )

    # Contamos las palabras en la respuesta y la mostramos al usuario
    words = count_words(response.choices[0].text)
    if words < word_count:
        response.choices[0].text += " " * (word_count - words)
    st.write(response.choices[0].text)

    # Mostramos el botón de reiniciar para que el usuario pueda volver a empezar
    if st.button("Reiniciar"):
        st.experimental_rerun()

if __name__ == "__main__":
    main()
