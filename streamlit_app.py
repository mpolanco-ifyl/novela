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
    st.title("Generador de escenas de novela")

    # Pedimos los detalles de la escena al usuario
    st.write("Bienvenido al generador de escenas de novela.")
    scene_synopsis = st.text_area("Escribe una breve sinopsis de la escena que quieres generar:")

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
            personality = st.text_area(f"Personalidad de {name}")
            character_names.append(name)
            character_roles.append(role)
            character_personalities.append(personality)

    # Preguntamos por el estilo o autor que se desea imitar
    style = st.text_input("¿Qué estilo o autor te gustaría imitar en esta escena?")

    # Preguntamos si la escena incluye diálogos
    has_dialogue = st.radio("¿La escena incluye diálogos?", ["Sí", "No"])

    # Generamos la escena con GPT-3
    if st.button("Generar escena"):
        prompt = f"Genera una escena de novela. {scene_synopsis} "
        if has_characters == "Sí":
            prompt += "Los personajes en esta escena son: "
            for i in range(character_count):
                prompt += f"{character_names[i]}, que es {character_roles[i]}. "
                prompt += f"{character_names[i]} es {character_personalities[i]}. "
        prompt += f"Imita el estilo de {style}. La escena{' incluye' if has_dialogue == 'Sí' else ' no incluye'} diálogos. "

        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.7,
        )

        st.write(response.choices[0].text)

if __name__ == "__main__":
    main()
