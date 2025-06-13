import streamlit as st
from fpdf import FPDF

st.title("Encuesta sobre el uso de ChatGPT en Educación")

st.write("Por favor, responde a cada afirmación seleccionando tu nivel de acuerdo:")

# Lista de preguntas
questions = [
    "ChatGPT facilita la creación de actividades educativas innovadoras.",
    "ChatGPT mejora la eficiencia en la planeación de clases.",
    "ChatGPT es una herramienta útil para generar ideas educativas basadas en problemas reales.",
    "ChatGPT contribuye a diversificar las estrategias de enseñanza utilizadas en clase.",
    "ChatGPT contribuye a personalizar el aprendizaje según las necesidades de los estudiantes.",
    "ChatGPT fomenta el desarrollo del pensamiento crítico en los estudiantes.",
    "ChatGPT promueve la autonomía en el aprendizaje de los estudiantes.",
    "ChatGPT mejora la comprensión de los conceptos en estudiantes con dificultades de aprendizaje.",
    "ChatGPT estimula la curiosidad y la creatividad en los estudiantes.",
    "Considero que ChatGPT tiene un impacto positivo en la enseñanza y el aprendizaje.",
    "Los beneficios de usar ChatGPT superan sus limitaciones en el contexto educativo.",
    "ChatGPT me motiva a explorar nuevas formas de enseñar y aprender.",
    "Recomendaría el uso de ChatGPT a otros docentes para mejorar los escenarios educativos.",
]

# Opciones
options = [
    "Totalmente de acuerdo",
    "De acuerdo",
    "Ni de acuerdo ni en desacuerdo",
    "En desacuerdo",
    "Totalmente en desacuerdo",
]

# Respuestas almacenadas
responses = {}

for i, q in enumerate(questions):
    responses[q] = st.radio(f"{i+1}. {q}", options, key=i)

# Botón para generar PDF
if st.button("Generar PDF con respuestas"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Resultados de la Encuesta sobre ChatGPT", ln=1, align="C")

    for i, (question, answer) in enumerate(responses.items(), 1):
        pdf.multi_cell(0, 10, txt=f"{i}. {question}\nRespuesta: {answer}", align="L")
        pdf.ln()

    pdf_output = "respuestas_encuesta_chatgpt.pdf"
    pdf.output(pdf_output)

    with open(pdf_output, "rb") as f:
        st.download_button(
            label="Descargar PDF",
            data=f,
            file_name=pdf_output,
            mime="application/pdf"
        )
