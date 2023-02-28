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
    st.title("Generador de escenas de novela en español")

    # Preguntamos al usuario por la sinopsis de la escena
    st.write("Escribe una sinopsis de la escena que te gustaría generar:")
    prompt = st.text_area("Sinopsis:")

    # Preguntamos por los personajes
    character_count = st.number_input("¿Cuántos personajes hay en la escena?", min_value=1, max_value=10, step=1)
    character_names = []
    character_roles = []
    character_personalities = []
    for i in range(character_count):
        name = st.text_input(f"Nombre del personaje #{i+1}")
        role = st.text_input(f"Papel del personaje #{i+1}")
        personality = st.text_area(f"Personalidad de {name}:")
        character_names.append(name)
        character_roles.append(role)
        character_personalities.append(personality)

    # Preguntamos por el estilo o autor que se desea imitar
    author_style = st.text_input("¿Qué estilo o autor te gustaría imitar? (opcional)")

    # Preguntamos si hay diálogos
    has_dialogue = st.radio("¿Incluye diálogos la escena?", ["Sí", "No"])

    # Generamos la escena al presionar el botón
    if st.button("Generar escena"):
        prompt += f"\n\nPersonajes: {', '.join(character_names)}"
        for i in range(character_count):
            prompt += f"\n\n{character_names[i]} es {character_roles[i]} y tiene una personalidad {character_personalities[i]}."
        if has_dialogue == "Sí":
            prompt += "\n\nDiálogo: [Inserta aquí el diálogo de la escena]"
        if author_style:
            prompt += f"\n\nEstilo o autor a imitar: {author_style}"

        # Generamos la escena con GPT-3
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=3048,
            n=1,
            stop=None,
            temperature=0.7,
        )

        # Contamos las palabras en la respuesta y la mostramos al usuario
        words = count_words(response.choices[0].text)
        st.write(response.choices[0].text)

    # Mostramos el botón de reiniciar para que el usuario pueda volver a empezar
    if st.button("Reiniciar"):
        st.experimental_rerun()

if __name__ == "__main__":
    main()
