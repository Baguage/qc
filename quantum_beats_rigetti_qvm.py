import math
import numpy as np

from pyquil.quil import Program
from pyquil.gates import Z, X, H, CNOT, PHASE
from pyquil.api import QVMConnection
from math import pi


def create_singlet_state():
    """ Returns quantum program that constructs a Singlet state of two spins """

    p = Program()

    # Start by constructing a Triplet state of two spins (Bell state)
    # 10|> + 01|>
    # https://en.wikipedia.org/wiki/Triplet_state
    #
    p.inst(X(0))
    p.inst(H(1))
    p.inst(CNOT(1, 0))

    # Convert to Singlet
    # 01|> - 10|>
    # https://en.wikipedia.org/wiki/Singlet_state
    #
    p.inst(Z(1))

    return p


def add_switch_to_singlet_triplet_basis_gate_to_program(program):
    """ Adds SWITCH_TO_SINGLET_TRIPLET_BASIS gate to a quantum program"""

    # The "SWITCH_TO_SINGLET_TRIPLET_BASIS" gate
    # will represent the system in singlet/triplet basis
    # 11|> will mean Singlet state, and 00|> will mean Triplet state
    my_array = np.array([
        [0, 1 / math.sqrt(2), 1 / math.sqrt(2), 0],
        [1, 0, 0, 0],
        [0, 0, 0, 1],
        [0, 1 / math.sqrt(2), -1 / math.sqrt(2), 0],
    ])
    program.defgate("SWITCH_TO_SINGLET_TRIPLET_BASIS", my_array)


def main():
    qvm = QVMConnection()

    # Rotation
    for angle in [0, pi/4, pi/2, 3*pi/4, pi]:
        p = create_singlet_state()
        add_switch_to_singlet_triplet_basis_gate_to_program(p)

        # Rotate phase to specified angle. In a real system, both spins/qubits are rotating,
        # But the difference between angles is all that matters
        p.inst(PHASE(angle, 0))
        # Using custom gate defined in add_switch_to_singlet_triplet_basis_gate_to_program function
        p.inst(("SWITCH_TO_SINGLET_TRIPLET_BASIS", 0, 1))
        # p.inst(PHASE(pi/4, 1))
        wavefunction = qvm.wavefunction(p)
        probs = wavefunction.get_outcome_probs()

        print("Rotation angle: %s", angle/pi*180)
        print("Probabilities ('11' - Singlet, '00' - Triplet): %s" % probs)


if __name__ == '__main__':
    main()
