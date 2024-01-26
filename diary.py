import streamlit as st
import layout_tools

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

    if week == 'Week 10':

        st.write('After last week’s results, I am finding that the interesting thing about this system is how '
                 'entanglement and correlations propagate through the system after a quench. This lead me to a few '
                 'papers looking at quasiparticle like propagation in Isling chains and the Lieb-Robinson bound.')

        st.write('The Lieb Roboinson Bound is a theoretical limit to how fast infomation can travel in a non '
                 'relatavisic quantum system. I believe this in a very interesting are to look at in to context of '
                 'inhomogenous quenchs')

        st.write('To begin investigating entanglement propagation after a local quench I made a colormap plot of each '
                 'of the individual atoms von Nuemenn Entropies. For a seven-atom system it is clear that there is '
                 'some sort of entanglement propagating through the system.')

        layout_tools.centre_image('Plots/7 Atom System/Quench 1st Atom/Entanglement Entropys/7_D=200_entanglement_entropy.png')

        st.write('The papers I have found interesting are...')

    if week == 'Week 11':

        st.write('This week has been mainly dedicated to preparing the presentation of the interim report. However, I will summarise some potential interesting avenues to look at as the project develops.')

        st.write('Many-body quantum mechanics is naturally hard to study due the large number of possible states we have at our disposal. Out of equilibrium dynamics, complicates things further as we cease to be in a steady state. Finding ways to simplify the dynamics of these scenarios enables further study into phenomena such as thermalization, quantum transport and entanglement growth. ')

        st.write('A coherent description of multiple dynamics on 1D Rydberg atom array I believe will prove useful in studying many-body quantum phenomena. Our project should therefore be focused on providing a rigours description of this. Moreover, we can look to new ways of modelling entanglement propagation through the system (perhaps through a quasiparticle picture).')

        st.write('The physics underlying a 1D Rydberg atom array is very rich and opens up many avenues to understanding equilibrium and non-equilibrium quantum many body dynamics.')

        st.write('<span style="color:red">***EDIT Week 12***</span>', unsafe_allow_html=True)

        st.write('After doing the presentation and getting good feedback I have reflected on a few things. These things are:')

        st.write('- In the text above I use the word ‘rigours’ to describe the goal of describing the system. This is a huge overestimation. If this project has taught me anything is that quantum many-body systems are very complicated! Much more complicated than they seems at first. The richness and depth of the Schrodinger equation for even three interacting atoms is immense. This is precisely why we need quantum simulators and cannot do everything on a laptop!')

        st.write('- The aim of the project should therefore very much tailor to finding ways of describing ‘characteristics’ of the system. And evaluating how possible/useful these measurements are on reaching a consensus on large overarching aspects of the project (thermalisation, entanglement, information propagation...). By no means should the goal be a full ‘coherent’ description of the system. That would be mad!')

        st.write('- With this in mind, the next few weeks are going to be dedicated to evaluating how **effective** different measures are in describing the complex non equilibrium dynamics of our systems. We leave to pros to come up with a ‘quasiparticle’ picture to how entanglement spreads form the local quench – I will be waiting humbly.')

    if week == 'Week 12':

        st.write('This week I was looking at if the correlation function could provide some new insight into the '
                 'dynamics after a quench. This was inspired by the use of the correlation function to describe the '
                 'Quantum Kibble Zurek Mechanism (QKZM) as done in this paper from the Lukin group: '
                 'https://www.nature.com/articles/s41586-019-1070-1')

        st.write('The Quantum Kibble Zurek mechanism describes the formation of topological defects in an order '
                 'system when it is driven through a phase transition to quickly to be fully adiabatic. It an '
                 'important concept in quantum annealing where defects in the system are associate with errors. As a '
                 'result, finding optimal annealing regime such that defects are minimise is an active area of '
                 'research. ')

        st.write('Since Rydberg atom arrays have a lot of potential to act as the hardware for solving a lot of '
                 'annealing problems understanding how these defects arise and if/how they propagate is interesting '
                 'give the scope of our system.')

        st.write('The correlation function tells us conditional probabilities between atom states. For example is we '
                 'find atom 1 in the ground state how likely is atom 2 to be in the ground state?')

        st.write('The correlation function is defined')

        st.latex(r'G(i, j) = \langle n_{i}n_{j} \rangle  - \langle n_{i}n_{j} \rangle')

        st.write(r'We can also write the generalised correlation function for two sites separated by a distance r by '
                 'summing over all pairs separated by that distance ($N_{R})')

        st.latex(r'G(r) = \sum_{i}^{N-r} G(i, i+r) / N_{r}')

        st.write('The correlation is another tool which we can use to evaluate the vast parameter space of the '
                 'quench. Not only does it show that after a quench atoms become increasingly correlated but also '
                 'indicate how corelations are distributed amongst the atoms. In the plots below it is apparent that '
                 'larger quenches (quenches from higher detuning) result in stronger longer range corelations. In the '
                 'following week, I will have a look at ways to quantify this effect as well as better explaining '
                 'what the correlation function measures (starting from a two atom system.')

        st.subheader('Plots')

        layout_tools.centre_image('Plots/5 Atom System/Correlations/Correlation function/With atom 1/q1_D=10_g(1,i).png', title=r'$\Delta$ = 10 MHz / 2$\pi$')
        layout_tools.centre_image(
            'Plots/5 Atom System/Correlations/Correlation function/With atom 1/q1_D=20_g(1,i).png', title=r'$\Delta$ = 20 MHz / 2$\pi$')
        layout_tools.centre_image(
            'Plots/5 Atom System/Correlations/Correlation function/With atom 1/q1_D=25_g(1,i).png', title=r'$\Delta$ = 25 MHz / 2$\pi$')
        layout_tools.centre_image(
            'Plots/5 Atom System/Correlations/Correlation function/With atom 1/q1_D=30_g(1,i).png', title=r'$\Delta$ = 30 MHz / 2$\pi$')
        layout_tools.centre_image(
            'Plots/5 Atom System/Correlations/Correlation function/With atom 1/q1_D=31.8_g(1,i).png', title=r'$\Delta$ = $V_{i,i+1}$ = 31.8 MHz / 2$\pi$')


