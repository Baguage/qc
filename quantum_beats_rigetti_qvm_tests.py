import unittest
from .quantum_beats_rigetti_qvm import create_singlet_state
from pyquil.api import QVMConnection


class CoreFunctionsTest(unittest.TestCase):
    """ REQUIRES CONNECTION TO RIGETTI FOREST QVM """

    def test_create_singlet_state(self):
        p = create_singlet_state()
        qvm = QVMConnection()
        wavefunction = qvm.wavefunction(p)
        # Make sure the wave function is what we expect
        # 1/sqrt(2) * (01|> - 10|>)
        self.assertEqual(wavefunction.amplitudes[0], 0)
        self.assertAlmostEqual(wavefunction.amplitudes[1], 0.7071067811865475+0j)
        self.assertAlmostEqual(wavefunction.amplitudes[2], -0.7071067811865475+0j)
        self.assertEqual(wavefunction.amplitudes[3], 0)


if __name__ == '__main__':
    unittest.main()
