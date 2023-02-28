import streamlit as st
import openai
import re
import os

# Inicializa el modelo GPT-3
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Función para contar palabras
def count_words(text):
    words = re.findall(r'\w+', text)
    return len(words)

# Función principal de la aplicación
def main():
    st.title("Generador de cuentos")

    # Preguntamos al usuario por la sinopsis de la escena
    prompt = st.text_area("Introduce la sinopsis del cuento que quieres generar:")

    # Preguntamos por los personajes y su personalidad
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

    # Preguntamos por el género o temática del cuento
    genre = st.selectbox("Selecciona el género o temática del cuento", ["Fantasía", "Ciencia ficción", "Romance", "Terror", "Misterio"])
    
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


    # Convertimos la escena en un cuento y mostramos el resultado
story_prompt = f"{response.choices[0].text}\n\nUna vez que {character_names[0]} {character_roles[0]}, {character_names[1]} {character_roles[1]}. "
story_prompt += f"El cuento es de {genre.lower()}."
story_response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=story_prompt,
    max_tokens=1600,
    n=1,
    stop=None,
    temperature=0.7,
)

    # Mostramos el resultado final al usuario
    words = count_words(story_response.choices[0].text)
    st.write(f"Tu historia tiene {words} palabras:")
    st.write(story_response.choices[0].text)

if __name__ == "__main__":
    main()
