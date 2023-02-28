import openai
import streamlit as st

# Configura la clave de la API de GPT-3
openai.api_key = "TU_CLAVE_DE_API_DE_GPT-3"

# Crea la interfaz de usuario con Streamlit
st.title("Generador de cuentos con GPT-3")
st.write("Ingrese los detalles del cuento:")
trama = st.text_input("Trama:")
personajes = st.text_input("Personajes:")
rol_personajes = st.text_input("Rol de los personajes:")
personalidad_personajes = st.text_input("Personalidad de los personajes:")
dialogos = st.text_input("¿Hay diálogos?")
estilo_autor = st.text_input("¿Qué estilo de autor desea imitar?")
clave_api = st.text_input("Ingrese su clave de API de GPT-3:")

# Genera el texto del cuento utilizando la API de GPT-3
if st.button("Generar cuento"):
    with st.spinner("Generando cuento..."):
        response = openai.Completion.create(
            engine="davinci",
            prompt=trama + " " + personajes + " " + rol_personajes + " " + personalidad_personajes + " " + dialogos + " " + estilo_autor,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        cuento_generado = response.choices[0].text
    st.write("Cuento generado:")
    st.write(cuento_generado)
