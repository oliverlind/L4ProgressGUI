import streamlit as st

import layout_tools


def plots(types):
    if types == 'Constant Zero Detunning':
        st.write("Below you will find plots illustrating the behaviour of 1D atom arrays being driven by an "
                 "oscillatory field at the Rabi frequency Ω = 4 (2πxMHz).")

        st.subheader('3 Atom Chain')

        st.write("The initial case we explore is that of no Van Der Wals interaction between the atoms (V=0). As "
                 "expected, each individual atoms Rydberg Fidelity (probability of being in the Rydberg state) "
                 "oscillates at the rabi frequency Ω = 4 (MHz); time period T = 0.25 μs")

        layout_tools.centre_image('Plots/Rabi Oscillations/n=3/Rabi_Osc_No_Int.png')

        st.write("Next, we turn on the interaction such that the second atom lies within the Blockade radius of "
                 "the first and third atom. Note: ‘a’ here is the uniform separation of the atoms an ‘R_b’ is the "
                 "blockade radius.")

        layout_tools.centre_image('Plots/Rabi Oscillations/n=3/Rabi_Osc_NN.png')

        layout_tools.centre_image('Plots/Rabi Oscillations/n=3/Rabi_Osc_NN_line.png')

        st.write("Now if we increase the time we evolve the system to 12 μs we get interesting plot:")

        layout_tools.centre_image('Plots/Rabi Oscillations/n=3/Rabi_Osc_NN_line_t=12.png')

    if types == 'Linear Detuning Increase':
        linear_detunning_increase()


    if types == 'Z3 Configuration':
        layout_tools.centre_image('Plots/n=7.png')

    if types == 'Quenches':
        pass


def linear_detunning_increase():
    st.subheader('One Atom')

    st.subheader('Two Atoms')
    layout_tools.centre_image('Plots/Linear detunning increase/n=2/energy_eigenspectra.png')
    layout_tools.centre_image('Plots/Linear detunning increase/n=2/eigenstates_density_matrices.png')

    col1, col2 = st.columns([1,1])

    # with col1:
    #     st.image('Plots/Linear detunning increase/n=2/energy_eigenspectra.png')
    #
    # with col2:
    #     st.image('Plots/Linear detunning increase/n=2/eigenstates_density_matrices.png')