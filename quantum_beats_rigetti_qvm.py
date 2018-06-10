import math
import numpy as np

from pyquil.quil import Program
from pyquil.gates import Z, X, H, CNOT, PHASE
from pyquil.api import QVMConnection
from math import pi


def create_singlet_state():
    """ Returns quantum program that constructs a Singlet state of two spins """

    # Start by constructing a Triplet state of two spins (Bell state)
    # 10|> + 01|>
    # https://en.wikipedia.org/wiki/Triplet_state
    #
    p = Program()
    p.inst(X(0))
    p.inst(H(1))
    p.inst(CNOT(1, 0))

    # Convert to Singlet
    # 01|> - 10|>
    # https://en.wikipedia.org/wiki/Singlet_state
    #
    p.inst(Z(1))

    return p


if __name__ == '__main__':
    p = create_singlet_state()
    # run the program on a QVM
    qvm = QVMConnection()
    result = qvm.wavefunction(p)
    print(result)

    # Rotation
    for angle in [0, pi/4, pi/2, 3*pi/4, pi]:
        p = create_singlet_state()

        # The "SWITCH_TO_SINGLET_TRIPLET_BASIS" gate
        # will represent entangled state of two spin in singlet/triplet basis
        # 11|> will mean Singlet state, and 00|> will mean Triplet state
        my_array = np.array([
            [0, 1 / math.sqrt(2), 1 / math.sqrt(2), 0],
            [1, 0, 0, 0],
            [0, 0, 0, 1],
            [0, 1 / math.sqrt(2), -1 / math.sqrt(2), 0],
        ])
        p.defgate("SWITCH_TO_SINGLET_TRIPLET_BASIS", my_array)

        # Rotate to specified angle
        p.inst(PHASE(angle, 0))
        p.inst(("SWITCH_TO_SINGLET_TRIPLET_BASIS", 0, 1))
        # p.inst(PHASE(pi/4, 1))
        result = qvm.wavefunction(p)
        probs = result.get_outcome_probs()

        print("Rotation angle: %s", angle/pi*180)
        print("Probabilities ('11' - Singlet, '00' - Triplet): %s" % probs)
