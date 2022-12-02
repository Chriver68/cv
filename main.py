import requests
import streamlit as st
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="CV van CV", page_icon=":thumb:", layout="wide")

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")


# ---- HEADER SECTION ----
with st.container():
    column_1, column_2, column_3= st.columns(3)
    with column_2:
        st.title("CHRISTIAAN VERDOOLD")

    with column_1:
        st.subheader("CONTACT:")
        st.write(":email: Neem contact op via het contactformulier onderaan de pagina.")

    with column_3:
        st.subheader("Functioneel beheerder/Procesverbeteraar")


# ---- WHAT I DO ----
with st.container():
    st.write("---")
    column_1, column_2, column_3 = st.columns(3)
    with column_1:
        st.subheader("Diploma's/Certificaten")
        st.write(
            """
            - Certificate of Lean Competency (LCS Level 1c Green Belt)
            - Integrated Service Management (ISM)
            - Functional Service Management (FSM)
            - Prince 2 Foundation
            - Tmap Next
            - BiSL Foundation
            - Nieuw in SQL en PL/SQL versie 10G
            - Oracle 91: SQL for End Users
            - Assurantie B
            - MBA (Moderne Bedrijfsadministratie)
            """
        )
        st.write("##")
        st.write("##")
        st.subheader("Hobbies:")
        st.write(
            """
            - Python programmeren
            - Fitness
            - Motorrijden
            - Hardlopen
            - Gezellig eten en drinken
            """
        )

    with column_2:
        st.header("Wie ben ik?")
        st.write("##")
        st.write(
            """
                Een ruim ervaren Functioneel Applicatiebeheerder die op een makkelijke manier 
                communiceert. 
                
                Flexibel, klant- en servicegericht, ondernemend, 
                initiatiefrijk en daadkrachtig. 
                
                Oplossingsgericht, durf kritisch te zijn en wil 
                producten opleveren die de gebruiker verder helpt bij hun werkzaamheden. 
                
                Ik heb een positieve en gedreven manier van werken en communiceren, zoek altijd 
                naar verbeteringen, 
                zowel in de aanwezige processen als in mijn eigen werk, heb 
                ruime ervaring met het schakelen tussen diverse teams en beschik over een gezonde 
                dosis verantwoordelijkheidsgevoel.
                
                De laatste tijd gaat mijn aandacht steeds meer uit 
                naar het verbeteren van met name het incidenten- en wijzigingsproces. 
                Mijn voorkeur gaat dan ook uit naar een functie waarin ik mij hierop kan richten.
                
                De volgende certificeringen heb ik in mijn bezit: BiSL Foundation, Prince2 Foundation, 
                Integrated- en Functional Service Management, Certificate of Lean Competency en 
                TMap Next. 
            """
        )

    with column_3:
        st.header("Wat verwacht ik van mijn nieuwe baan/werkgever?")
        st.write(
            """
                - 36 uur per week werken verdeeld over 4 dagen
                - Salaris rond 4.218,00/2.856 (BRUTO/NETTO) met 8% vakantiegeld
                - reistijd max. 30/45 minuten enkele reis vanaf Schoonhoven
                - mogelijkheid tot thuiswerken
                - geen storingsdienst van toepassing 
                - goede opleidingsmogelijkheden voor bijv. vakgerelateerde HBO-opleiding
                - bedrijfsprocessen zijn op orde 
                - gezonde dynamiek binnen de organisatie te hebben (niet autoritair)
                - goede samenwerking 
                - gezellige werksfeer

            """
        )

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Neem contact op indien u geinteresseerd bent naar mijn volledige CV.")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/CHR.VERDOOLD@GMAIL.COM" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Uw naam" required>
        <input type="text" name="bedrijfsnaam" placeholder="Bedrijfsnaam" required>
        <input type="email" name="email" placeholder="Uw email adres" required>
        <textarea name="message" placeholder="Plaats uw bericht hier" required></textarea>
        <button type="submit">Verzend</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()