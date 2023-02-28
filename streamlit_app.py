import streamlit as st
import openai
import re

# Pide la clave de API de OpenAI al usuario
openai.api_key = st.text_input("Introduce tu clave de API de OpenAI:")

# Función para contar palabras
def count_words(text):
    words = re.findall(r'\w+', text)
    return len(words)

# Función para duplicar la longitud de un párrafo
def double_length(text):
    return text + text

# Función principal de la aplicación
def main():
    st.title("Generador de contenido en español")

    # Establecemos los valores de longitud de palabras para cada tipo de contenido
    word_counts = {
        "blog": 1000,
        "libro electrónico": 3000,
        "relato corto": 10000,
        "libro infantil": 40000,
        "novela romántica": 40000
    }

    # Preguntamos al usuario la consulta inicial
    st.write("Bienvenido al generador de contenido en español. ¿Qué tipo de contenido puedo escribir para ti hoy?")

    # Opciones de tipo de contenido
    content_type = st.selectbox("Selecciona el tipo de contenido", ["blog", "libro electrónico", "relato corto", "libro infantil", "novela romántica"])

    # Pedimos palabras clave y temas adicionales
    keywords = st.text_input("Escribe algunas palabras clave o temas que te gustaría incluir en el contenido")

    # Preguntamos por la longitud prevista del contenido
    word_count = word_counts[content_type]
    st.write(f"La longitud prevista del contenido es de {word_count} palabras.")

    # Preguntamos por la sensación general y el tono del contenido
    mood = st.text_input("¿Cuál es la sensación general que te gustaría transmitir en el contenido? (por ejemplo: misterioso, divertido, emocionante)")
    tone = st.text_input("¿Cuál es el tono que te gustaría utilizar en el contenido? (por ejemplo: formal, informal, neutro)")

    # Preguntamos por los personajes, si es necesario
    has_characters = st.radio("¿El contenido incluye personajes?", ["Sí", "No"])
    if has_characters == "Sí":
        character_count = st.number_input("¿Cuántos personajes hay en el contenido?", min_value=1, max_value=10, step=1)

        # Preguntamos por los nombres y roles de cada personaje
        character_names = []
        character_roles = []
        for i in range(character_count):
            name = st.text_input(f"Nombre del personaje #{i+1}")
            role = st.text_input(f"Papel del personaje #{i+1}")
            character_names.append(name)
            character_roles.append(role)

        # Describimos la personalidad de cada personaje
        for i in range(character_count):
            st.write(f"Personalidad de {character_names[i]}: ")
            personality = st.text_area(f"Describe la personalidad de {character_names[i]} en pocas palabras.")
    
           # Pedimos al usuario que escriba la consulta para generar el contenido
        st.write("Escribe a continuación tu consulta para generar el contenido:")

        if st.button("Generar contenido"):
            prompt = f"Su tarea consiste en actuar como escritor y autor profesional y redactar diversas formas de contenido. Todos los resultados deben estar en español. "

            # Añadimos la consulta del usuario al prompt
            query = st.text_area("Escribe tu consulta aquí:")
            prompt += query

            # Añadimos la información adicional al prompt
            prompt += f"Para el tipo de contenido '{content_type}', escribirás sobre '{keywords}' en un estilo {mood} y {tone}. "

            # Añadimos información sobre los personajes, si es necesario
            if has_characters == "Sí":
                prompt += "Los personajes en esta historia son: "
                for i in range(character_count):
                    prompt += f"{character_names[i]}, que es {character_roles[i]}. "
                    prompt += f"{character_names[i]} es {personality}. "

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
                response.choices[0].text += " "
                response.choices[0].text += response.choices[0].text
                words = count_words(response.choices[0].text)
            st.write(response.choices[0].text)

            # Pedimos al usuario que apruebe el contenido antes de duplicar su longitud
            if st.button("Duplicar longitud"):
                response.choices[0].text = double_length(response.choices[0].text)
                st.write(response.choices[0].text)

    # Mostramos el botón de reiniciar para que el usuario pueda volver a empezar
    if st.button("Reiniciar"):
        st.experimental_rerun()

if __name__ == "__main__":
    main()
