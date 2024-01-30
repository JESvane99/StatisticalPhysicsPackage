"""
All one could desire with partition functions
"""

import numpy as np

import itertools

import sympy as sp

from sympy import oo, Matrix

from IPython.display import display, Latex

from scipy.constants import physical_constants

h, f, beta, E0, E_s, k, T = sp.symbols("h f beta E0 E_s k T",
                                       real=True,
                                       positive=True)
n = sp.symbols("n", integer=True)
U = sp.symbols("U", positive=True)


def T_therm_equil_resevoir(Delta_Energy, total_num):
    """
    Calculation of Temperature when relative probability is given

    params:
    - Delta_energy: the energy difference between the two states
    which are involved
    - rel_prob: relative probability, $\frac{\rho(s_2)}{\rho(s_1)}$
    """

    k = np.array(
        [
            "Boltzmann constant in eV/K",
            "Boltzmann constant",
            "Boltzmann constant in Hz/K",
            "Boltzmann constant in inverse meters per kelvin",
        ]
    )

    for i in k:
        print("Use this if", i, "matches the units given:")
        bolt = physical_constants[i][0]
        print(Delta_Energy / (bolt * np.log(total_num)))


def Frac_partition_funcs(E_difference, T):
    """
    The fraction of higher energy state particles
    vs lower energy state particles

    params:
    - E_difference: energy difference between the two states.
    - T: temperature

    Returns:
    - Fraction of particles with higher energy.
    """
    Res_difference = np.exp(
        -E_difference / (physical_constants["Boltzmann constant"][0] * T)
    )

    print(
        f"for every 1 particle in the lowest state there is\n {Res_difference}"
        "particles in the higher energy state"
    )

    Res_frac_lowerstate = 1 / (1 + Res_difference)

    Res_frac_upperstate = 1 - Res_frac_lowerstate

    print(
        f"The percentage of lower state particles is {Res_frac_lowerstate}\n"
        f"The percentage of lower state particles is {Res_frac_upperstate}"
    )

    return Res_difference


def PF_average_energy(func, beta):
    """
    Calculating the average energy using the partition function

    Notes:
    - remember that beta is 1/(kT) and not (kT) such that
    the correct derevative is taken

    params:
    - func: the function written symbolically using sympy module
    - beta: should correspond to 1/(kT) in the function which is used

    returns:
    - Average energy for one particle
    """
    h, f, beta, E0, E_s, k, T = sp.symbols(
        "h f beta E0 E_s k T",
        real=True,
        positive=True
    )

    myfunc = func

    res = -1 / myfunc * myfunc.diff(beta)

    res = res.collect((beta, E0, beta * E0))

    display(Latex("The average energy is:"), res)

    N = sp.symbols("N")

    # E_tot = N * res

    # display(Latex("The total energy for N particles is:"), E_tot)

    res2 = sp.log(myfunc)

    res2 = -res2.diff(beta)

    compare = res.equals(res2)

    if not compare:
        raise "derivatives do not compare"


    try:
        T_toinf = sp.limit(res, beta, sp.oo)

        T_tonot = sp.limit(res, beta, 0)

        print("----------------------------------------------------------------")

        display(Latex("Evaluation of average energy at $beta \Rightarrow 0$"), T_tonot)

        print("----------------------------------------------------------------")

        display(Latex("Evaluation of average energy at $beta \Rightarrow \infin$"), T_toinf)

    except Exception:  # noqa: E722
        try:
            res = res.expand()

            T_toinf = res.limit(beta, sp.oo)

            display(
                Latex("Evaluation of average energy at $ beta \Rightarrow \infin$"), T_toinf
            )
            print("")
            print("Could not evaluate for beta->0\n" "use this to do it yourself:")

        except Exception:  # noqa: E722
            try:
                res = res.expand()

                T_tonot = res.limit(beta, 0)

                display(
                    Latex("Evaluation of average energy at $beta \Rightarrow 0$"), T_tonot
                )
                print("")
                print("Could not evaluate for beta->infinity\n" "use this expansion of the avereage energy to do it yourself:")

            except Exception:  # noqa: E722
                print("tried to evaluate at extreme temperatures......")
                print("Simultaniously froze and melted")
                print("only you can evaluate it now")

    display(res)

    return res


def PF_heat_capacity(partition_func, beta):
    """
    Calculating the total energy using the partition function

    Uses that to derive the heat capacity,
    and then evaluates at T->0 and T -> infinity

    Notes:
    - remember that beta is 1/(kT) and not (kT) such
    that the correct derevative is taken

    params:
    - func: the function written symbolically using sympy module
    - beta: should correspond to 1/(kT) in the function which is used

    returns:
    - heat capacity
    """
    h, f, beta, E0, E_s, k, T = sp.symbols(
        "h f beta E0 E_s k T",
        real=True,
        positive=True
    )
    try:
        k, T, N = sp.symbols("k T N", positive=True)

        myfunc = N * PF_average_energy(partition_func, beta)

        myfunc = myfunc.subs(beta, 1 / (k * T)).simplify()

        C_V = myfunc.diff(T)

        T_toinf = sp.limit(C_V, T, sp.oo)

        T_tonot = sp.limit(C_V, T, 0)

        display(Latex("The total Energy as a function of T:"), myfunc)

        print("----------------------------------------------------------------")

        display(Latex("Heat Capacity at constant volume:"), C_V)

        print("----------------------------------------------------------------")

        display(Latex("Evaluation of heat capacity at $T \Rightarrow 0$"), T_tonot)

        print("----------------------------------------------------------------")

        display(Latex("Evaluation of heat capacity at $T \Rightarrow \infin$"), T_toinf)

        return C_V
    except Exception:
        print("... Heat capacity failed Will return average energy pr particle...")
        print("but at least you got the average energy")

    finally:
        print("done")


def PF_prob_of_one_state(func, energy=h * f, single_state=False):
    """
    Probability of one state being the one state
    """

    if not single_state:
        boltfactor = sp.sum(sp.exp(-beta * energy), (n, 0, oo))

        boltfactor = 1

    else:
        boltfactor = sp.exp(-beta * energy)

    prob = 1 / func * boltfactor

    return prob


def partition_func_template(
    m=1, quant_single_state: list = [1], e_unit=None, e_input=None
):
    """
    Gives a partition function as an expanded sum.

    if e_input is not 'None' do not bother with other parameters

    Params:
    m: number of different energy states

    quant_single_state: quantity of a single state i.e. degeneracy

    e_input(array like): Use this param when different energies of all possible outcomes is sort array like.

    """
    Z = sp.symbols("Z", function=True)

    Z = 0

    if isinstance(e_unit, sp.Symbol):
        energy = sp.symbols(f"E:{m}")

        for i, j in zip(quant_single_state, range(m)):
            Z += sp.exp(-beta * energy[j]) * i

        display(Z)

    elif e_unit == "helmholts":
        m_ = m

        Z_ = sp.symbols(f"Z_{m_}")

        N = sp.symbols(f"N_{m_}")

        Z = 1 / sp.factorial(N) * Z_**N

    else:
        energy = e_input

        for i in energy:
            Z += sp.exp(-beta * i)

        display(Z)
    return Z


def symbolic_F_free_energy(num_particles=1, stirling_approx=True):
    """
    Function for writing up the free energy with or without the stirling approximation

    Uses the partition_func_template

    :param int num_particles: Number of different particles.
    Turns it into alphabetical i.e. 1=a 2=3 and so on.

    :param bool stirling_approx: decides wether or not the stirling approximation should be used.
    """
    alphabet_of_part = [chr(i + 97) for i in range(num_particles)]

    z_list = sp.symbols(f"Z_a:{chr(num_particles+96)}")

    F_tot = 0

    if stirling_approx is True:
        for i, j in zip(alphabet_of_part, z_list):
            j = partition_func_template(i, e_unit="helmholts")

            N_ = sp.var(f"N_{i}")
            Z_ = sp.var(f"Z_{i}")
            display(j)

            F_part = -k * T * sp.log(j)

            F_part = F_part.replace(sp.log(j), N_ * sp.log(Z_) - (N_ * sp.log(N_) + N_))
            F_tot += F_part

    else:
        for i, j in zip(alphabet_of_part, z_list):
            j = partition_func_template(i, e_unit="helmholts")

            display(j)

            F_part = -k * T * sp.log(j)
            F_tot += F_part

    # F_tot = F_tot.simplify()

    return F_tot


if __name__ == "__main__":
    HFE = symbolic_F_free_energy(3, stirling_approx=False)
    display(HFE)


def create_arrays(r, k):
    """
    Returns an array with following properties:

    - sum(row_i) = k
    - len(row_i) = r
    - shape = (i, r) = (rows,cols)
    - i = [0,1,...,r*k]
    - circulates through all possible compositions of arrays
            with possitive inputs that has a sum = k
    """

    # Initialize an empty list to store the arrays
    arrays = []

    # Generate all possible combinations of r elements from 0 to k with repetition
    combos = itertools.combinations_with_replacement(range(k + 1), r)

    # Iterate over the combinations and check if the sum of the elements is equal to k
    # sumcount = []

    # for rs in range(r):
    #     while sum(sumcount) < k :
    #         sumcount.append(1)

    #     sumcount.append(0)

    #     if len(sumcount) == r:
    #         break

    for c in combos:
        if sum(c) == k:
            # Convert the combination to a list and append it to the arrays list
            arrays.append(list(c))

    display(arrays)

    temp_array = np.array(arrays)
    useful, garb = np.array(arrays).shape
    while useful < r * k:
        temp_array = np.roll(temp_array, 1, axis=1).tolist()
        for x in temp_array:
            arrays.append(x)
        useful += len(temp_array)

    # Return the arrays list
    return np.array(arrays)


def energyMatrix(
    n: int = 1,
    m: int = 1,
    qntt_prtcls: int = 1,
    nrg_type=None,
    ret_all: bool = False
):
    """
    gives a matrix containing the different energies of a system

    params:
    n: number of different states i.e. if a system has two states with -e and one with e, then n=3

    m: is the quantity of energy which has negative prefix

    qntt_prtcls: quantity of particles i.e. how many particles in the system

    is_disting: Bool which tells the function if the particles
        are distinguishable or not. Defualt: True

    """
    psbl_systts = create_arrays(n, qntt_prtcls)

    nrgmtrx = []

    while len(nrgmtrx) < n:
        for item in range(m):
            nrgmtrx.append(-1)
        nrgmtrx.append(1)

    nrgvctr = np.array(nrgmtrx)
    FMatrix = np.dot(psbl_systts, nrgvctr)

    if nrg_type:
        FMatrix = nrg_type * FMatrix

    display(
        "This is from the function energyMatrix --------------------"
    )
    print("Possible outcomes of particle positions: \n")
    display(Matrix(psbl_systts))

    print("The energy vector: \n")
    display(Matrix(nrgvctr))

    print("The Energies for the different possible systems: \n")
    display(Matrix(FMatrix))

    display("\n -------------------------------------")

    if ret_all is True:
        return FMatrix, psbl_systts, nrgvctr
    return FMatrix


# eps = sp.symbols('epsilon', positive = True)

# nrgs = energyMatrix(3,2,2,nrg_type=eps)

# nrgs_b = np.add(nrgs,[U,0,U,0,U,0])

# F1a = partition_func_template(e_input=nrgs)

# F1b = partition_func_template(e_input=nrgs_b)
