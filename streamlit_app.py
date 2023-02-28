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
