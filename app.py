import streamlit as st
from PIL import Image

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
        option = st.selectbox('Select Option', ['Intro', 'Diary', 'Code', 'Papers', 'Interim Report', 'Presentation', 'Final Report'], )

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
        st.subheader("Code set up")

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
        week = st.selectbox('Select Week', ['Week 1-7', 'Week 8', 'Week 9', 'Week 10', 'Week 11', 'Week 12', 'Week 13'], key='Weeks')

        diary.diary(week)



    # if option == 'Plots':
    #     types = st.selectbox('Select Type', ['Constant Zero Detunning', 'Two atom System', 'Quench'])
    #
    #     plots.plots(types)







if __name__ == "__main__":
    main_ui()
