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
    st.title("Generador de cuentos")

    # Preguntamos al usuario por la sinopsis del cuento
    prompt = st.text_area("Introduce la sinopsis del cuento que quieres generar:")

    # Preguntamos por detalles específicos sobre la trama y los personajes
    genre = st.text_input("¿Qué género o temática te gustaría que tuviera el cuento?")
    character_count = st.number_input("¿Cuántos personajes hay en el cuento?", min_value=1, max_value=10, step=1)
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

    # Preguntamos por el estilo o autor que se desea imitar y si hay diálogos
    style = st.text_input("¿Qué estilo o autor te gustaría imitar?")
    has_dialogue = st.radio("¿Incluye la escena algún diálogo?", ["Sí", "No"])

    # Generamos el cuento con GPT-3
    if st.button("Generar cuento"):
        prompt = f"{prompt}\n\nGénero: {genre}\n\nPersonajes:\n"
        for i in range(character_count):
            prompt += f"{character_names[i]} es un {character_roles[i]} con una personalidad {character_personalities[i]}.\n"
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=3600,
            n=1,
            stop=None,
            temperature=0.7,
        )

        # Convertimos la escena en un cuento y mostramos el resultado
if response.choices:
    story_prompt = f"{response.choices[0].text}\n\nUna vez que {character_names[0]} {character_roles[0]}, {character_names[1]} {character_roles[1]}. "
    if has_dialogue == "Sí":
        story_prompt += f"\"{st.text_input('Escribe una línea de diálogo:')}\" dijo {character_names[2]}."
    story_response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=story_prompt,
        max_tokens=1600,
        n=1,
        stop=None,
        temperature=0.7,
    )
    if story_response.choices:
        # Mostramos el resultado final al usuario
        words = count_words(story_response.choices[0].text)
        st.write(f"Tu historia tiene {words} palabras:")
        st.write(story_response.choices[0].text)
    else:
        st.write("Lo siento, no se pudo generar la historia. Por favor intenta con otra sinopsis o revisa la información que proporcionaste.")

 
if __name__ == "__main__":
    main()

