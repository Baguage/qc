# Simulating chemical systems on a quantum computer

This is a repository for code to simulate Quantum beats (Dynamic singlet–triplet transitions) in spin-correlated radical pairs
on a quantum computer. We are going to use Riggeti Forest and IBM Q as our platforms.
Modeling quantum beats might be one of the applications where quantum supremacy can be demonstrated.

This effect was discovered in 1976 by J. Klein and R. Voltz and B. Brocklehurst and developed into a spectroscopic tecnique by professor Yu N Molin's group in Russia.
Please refer to the 2007 review by V A Bagryansky, V I Borovkov and Yu N Molin http://iopscience.iop.org/article/10.1070/RC2007v076n06ABEH003715/pdf for additional information.

# Usage - Rigetti code

Follow instructions on http://pyquil.readthedocs.io/en/latest/start.html page. I personally prefer creating a separate virtual environment for every project, but it is a matter of taste. 

You will need to request a Forest API key. I got mine in a minute after request. 

Run the program:
```
python quantum_beats_rigetti_qvm.py
```

# Usage - IBM Q code

TBD
