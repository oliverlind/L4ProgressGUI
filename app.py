import streamlit as st
from PIL import Image

import layout_tools
import plots
import diary

def main_ui():
    """
    Main streamlit UI
    :return:
    """

    # Page config
    st.set_page_config(
        page_title="Oliver Lind ",
        page_icon="chart_with_upwards_trend",
        layout="wide",
        initial_sidebar_state="auto"
    )

    # Title and introduction
    st.title('Oliver Lind Level 4 Project')

    with st.sidebar:
        st.header('1D Arrays Rydberg Atom Arrays')
        st.image('Diagrams/Atom Chain Set Up with Lasers.png')
        option = st.selectbox('Select Option', ['Intro', 'Diary', 'Code', 'Reports', 'Presentations'], )

    if option == 'Intro':
        st.subheader('Introduction')
        st.write("Hi there!")
        st.write(
            "Welcome to my webpage dedicated to my project on Rydberg atom array quantum simulators.")

        st.write("Feel free to explore different aspects of my project using the sidebar. I will update "
                 "these sections as I progress and reflect on different aspects of the project.")

        st.write("Much of the work done in the first term in outline in the group teams chat 'QSIM'. In term two, "
                 "as Tom (other project student) and I's projects diverge, I will add to this webpage with reflections "
                 "on the project and future plans")

        st.write("If you encounter any issues with the webpage or have suggestions on how to improve the organization "
                 "and presentation of my work, please don't hesitate to reach out to me via email at "
                 "oliver.l.lind@durham.ac.uk.")

        st.write("The code for the project can be accessed through my GitHub via the link: "
                 "https://github.com/oliverlind/RydbergQubit.")

    if option == 'Code':
        st.divider()
        st.subheader("Code set up")
        st.write('Structure of the python code is as follows')

        layout_tools.centre_image('Diagrams/Code_set_up.png')

        st.write("The code for the project can be accessed through my GitHub via the link: "
                 "https://github.com/oliverlind/RydbergQubit.")

        # st.write(" The code for 1D atom arrays as follows:")
        #
        # st.write(f"The 'RydbergHamiltonian1D' class computes the 2^n dimensional Hamiltonian matrix "
        #          f"for the following Hamiltonian:")
        #
        # #st.latex("H = -Σ_i \Delta_i|r_i⟩⟨r_i| + Σ_i,j J_ij * |r_i⟩⟨r_j|")
        #
        # st.write("The 'AdiabaticEvolution' class is responsible for evolving the Hamiltonian. This is done via "
        #          "Trotterization for a selected time interval 'dt' of a desired time.")
        #
        # st.write("The Hamiltonian can be evolved under different detuning schedules. So far, the two options are:")
        #
        # st.write("• Linear Detuning: Pick a start and a stop detuning value and evolve through these values in 't/dt' "
        #          "integer steps.")
        #
        # st.write("• Zero Detuning: Hamiltonian is evolved with zero detuning.")

    if option == 'Diary':
        st.divider()
        st.subheader('Project Diary')
        weeks_list = ['Week 1-8', 'Week 9', 'Week 10', 'Week 11', 'Week 12', 'Week 13',
                      'Week 14-15', 'Week 16', 'Week 17', 'Week 18', 'Week 19']
        week = st.selectbox('Select Week', reversed(weeks_list), key='Weeks')

        diary.diary(week)

    if option == 'Reports':
        st.subheader('Reports')

        with open('Reports and presentations/Oliver Lind L4 Report.pdf', "rb") as pdf_file:
            PDFbyte = pdf_file.read()

        container = st.container(border=True)

        container.write('**Final Report**')
        container.download_button(label="OL Final Report",
                                  data=PDFbyte,
                                  file_name='Oliver Lind L4 Report.pdf',
                                  mime='application/octet-stream')

        with open('Reports and presentations/L4_Formative_Progress_Report two col.pdf', "rb") as pdf_file:
            PDFbyte = pdf_file.read()

        container = st.container(border=True)

        container.write('**Interim Report**')
        container.download_button(label="OL Interim Report",
                                  data=PDFbyte,
                                  file_name='OL Interim Report.pdf',
                                  mime='application/octet-stream')

    if option == 'Presentations':
        st.subheader('Presentations')

        with open('Reports and presentations/L4 Presentation.pdf', "rb") as pdf_file:
            PDFbyte = pdf_file.read()

        container = st.container(border=True)

        container.write('**L4 seminar presentation**')
        container.download_button(label="L4 presentation",
                                  data=PDFbyte,
                                  file_name='L4 presentation OL.pdf',
                                  mime='application/octet-stream')

        with open('Diary/Strathclyde presentation Oliver.pdf', "rb") as pdf_file:
            PDFbyte = pdf_file.read()

        container = st.container(border=True)

        container.write('**Strathclyde presentation on recent local quench results**')
        container.download_button(label="Strathclyde presentation",
                                  data=PDFbyte,
                                  file_name='Strathclyde presentation OL.pdf',
                                  mime='application/octet-stream')








    # if option == 'Plots':
    #     types = st.selectbox('Select Type', ['Constant Zero Detunning', 'Two atom System', 'Quench'])
    #
    #     plots.plots(types)







if __name__ == "__main__":
    main_ui()
