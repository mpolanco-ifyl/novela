import streamlit as st
import openai
import re

# Pide la clave de API de OpenAI al usuario
openai.api_key = st.text_input("Introduce tu clave de API de OpenAI:")

# Lista de autores españoles
autores_espanoles = ["Miguel de Cervantes", "Lope de Vega", "Federico García Lorca", "Gabriel García Márquez", "Jorge Luis Borges", "Isabel Allende", "Mario Vargas Llosa", "Octavio Paz", "Pablo Neruda", "Gustavo Adolfo Bécquer", "Juan Ramón Jiménez", "Antonio Machado", "Rosalía de Castro", "José Martí", "Rubén Darío", "Leopoldo Alas Clarín", "Emilia Pardo Bazán", "Ramón del Valle-Inclán", "Benito Pérez Galdós", "Fernán Caballero"]

# Se define la función para generar el cuento
def generar_cuento(trama, autor):
    # Se establecen los parámetros para la generación del texto
    prompt = (f"Escribe un cuento que comience con la siguiente trama: {trama}\n\n"
              f"Imita el estilo de escritura de {autor}.")
    temperatura = random.uniform(0.5, 1.2)
    max_tokens = 3024

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

    # Se genera el cuento
    if st.button("Generar cuento"):
        cuento = generar_cuento(trama, autor)
        st.write("Aquí está tu cuento:")
        st.write(cuento)

# Se ejecuta la app
if __name__ == "__main__":
    main() 
