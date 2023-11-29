import streamlit as st
import layout_tools

# Week 8

def diary(week):

    if week == 'Week 8':

        st.write('Alongside investigating further, the dynamics of the local quench, this week I had a look at some '
                 'applications of single addressing lasers on our atoms. One notable application I came across was '
                 'the generation of GHZ states on even number Rydberg atom chains. This was outlined in the following '
                 'paper: https://arxiv.org/abs/1905.05721.')

        st.write('The state we are after is the GHZ state which takes on different forms. In this case the state the '
                 'paper was referring to is:')

        st.latex(r'''
        ∣GHZ_\text{ N}⟩ = \frac{1}{\sqrt{2}}  (∣0101...⟩ \ + ∣1010...⟩)''')


        st.write('The paper reached this target state by perform a linear detuning sweep on an even number of neutral '
                 'Rb atoms at a distance such that nearest neighbour blockade took effect. This put the system into a '
                 'superposition of alternate Z2 crystals states alongside some ‘edge states’ with Rydberg excitations '
                 'on the end atoms.')

        st.write('In order to attain the GHZ state we would like to have the system in solely a superposition of the '
                 'alternating Z2 even states. To do this the paper single addresses atoms such that the two Z2 states '
                 'become the most energetically favourable. This is done by shining a less detuned leaser on the edge '
                 'atoms such that two edge Rydberg excitations is most energetically costly. As the process is down '
                 "adiabatically, the system stays in it's ground state which after the single adressing is the desired "
                 'GHZ state')

        st.write('Following the process outlined by the paper, I decided to try generating these states for a 4 and 6 '
                 'atom system. I did this by sweeping the edge atoms to lower detuning values then the rest as '
                 'outlined by the figures below.')

        layout_tools.centre_image('Plots/4 Atom System/GHZ State Preperation/4_D=130,180_state_fidelities.png')

        layout_tools.centre_image('Plots/4 Atom System/GHZ State Preperation/4_D=130,180_GHZ_fidelity.png')

        layout_tools.centre_image('Plots/6 Atom System/GHZ State preperation/6_D=130,180_GHZ_fidelity.png')

        st.write('The result we get is the generation of the of the GHZ state to 96% fidelity in the 4-atom case and '
                 '90% in the 6-atom case.  As expected, the fidelity of the GHZ decreases with an increase in the '
                 'number of atoms as new ‘edge states’ with third site excitations start to creep in. To address '
                 'this, we can as before single address these third sites with less detuned lasers to keep the two Z2 '
                 'states most energetically favourable.')