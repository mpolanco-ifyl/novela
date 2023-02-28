import streamlit as st
import openai
import random

# Pide la clave de API de OpenAI al usuario
openai.api_key = st.text_input("Introduce tu clave de API de OpenAI:")

# Lista de autores españoles
autores_espanoles = ["Javier Marías", "Carlos Ruiz Zafón", "Arturo Pérez-Reverte", "Almudena Grandes", "Juan José Millás", "María Dueñas", "Javier Cercas", "Rosa Montero", "Eduardo Mendoza", "Luis Landero"]

# Se define la función para generar el cuento
def generar_cuento(trama, autor, incluir_dialogos):
    # Se establecen los parámetros para la generación del texto
    prompt = (f"Escribe un cuento que comience con la siguiente trama: {trama}\n\n"
              f"Imita el estilo de escritura de {autor}.")

    # Si el usuario ha indicado que quiere incluir diálogos, se agrega esta frase a la prompt
    if incluir_dialogos:
        prompt += "\n\nAsegúrate de incluir algunos diálogos en la historia."

    temperatura = random.uniform(0.7, 1.2)  # Ajuste de temperatura
    max_tokens = 4096  # Ajuste de max_tokens

    # Se genera el texto con el modelo GPT-3 de OpenAI
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=max_tokens,
        n=1,
        temperature=temperatura
    )

    # Se devuelve el texto generado
    return completions.choices[0].text

# Se define la app de Streamlit
def main():
    # Título de la app
    st.title("Generador de cuentos con OpenAI")

    # Descripción de la app
    st.write("Esta aplicación genera un cuento a partir de una trama dada, imitando el estilo de escritura de un autor español seleccionado por el usuario.")

    # Input de la trama
    trama = st.text_input("Introduce la trama del cuento:")

    # Input del autor
    autor = st.selectbox("Selecciona el autor a imitar:", autores_espanoles)

    # Input para incluir diálogos
    incluir_dialogos = st.radio("¿Quieres incluir diálogos en la historia?", options=["Sí", "No"])

    # Se genera el cuento
    if st.button("Generar cuento"):
        cuento = generar_cuento(trama, autor, incluir_dialogos == "Sí")
        st.write("Aquí está tu cuento:")
        st.write(cuento)

# Se ejecuta la app
if __name__ == "__main__":
    main()
