import streamlit as st
from PIL import Image

import plots

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
        option = st.selectbox('Select Option', ['Intro', 'Plots', 'Code', 'Papers'], )

    if option == 'Intro':
        st.subheader('Introduction')
        st.write("Hi there!")
        st.write(
            "Welcome to my webpage dedicated to my project on Rydberg atom array quantum computers and simulators.")

        st.write("Feel free to explore different aspects of my project using the sidebar. I will regularly update "
                 "these sections as I make progress, with further subsections for each aspect.")

        st.write("I'll also keep the Teams chat updated with relevant plots and results to complement the webpage "
                 "content.")

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

    if option == 'Plots':
        types = st.selectbox('Select Type', ['Constant Zero Detunning', 'Linear Detuning Increase', 'Z3 Configuration'])

        plots.plots(types)





if __name__ == "__main__":
    main_ui()
