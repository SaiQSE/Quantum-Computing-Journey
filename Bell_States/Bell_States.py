from qiskit import QuantumCircuit,transpile
from qiskit_aer import AerSimulator
def run_circuit(circuit):
    Simulator=AerSimulator()
    compiled_circuit=transpile(circuit,Simulator)
    Job=Simulator.run(compiled_circuit,shots=1000)
    results=Job.result()
    counts=results.get_counts()
    print("\n",counts)

def phi_plus():
    bell=QuantumCircuit(2,2)
    bell.h(0)
    bell.cx(0,1)
    bell.measure([0,1],[0,1])
    print("phi plus outcomes:")
    run_circuit(bell)
    print("\n","Circuit diagram")
    print(bell.draw("text"))

def phi_minus():
    bell=QuantumCircuit(2,2)
    bell.h(0)
    bell.cx(0,1)
    bell.z(0)
    bell.measure([0,1],[0,1])
    print("phi minus outcomes:")
    run_circuit(bell)
    print("\n","Circuit diagram")
    print(bell.draw("text"))

def psi_plus():
    bell=QuantumCircuit(2,2)
    bell.h(0)
    bell.x(1)
    bell.cx(0,1)
    bell.measure([0,1],[0,1])
    print("psi plus outcomes:")
    run_circuit(bell)
    print("\n","Circuit diagram")
    print(bell.draw("text"))

def psi_minus():
    bell=QuantumCircuit(2,2)
    bell.h(0)
    bell.x(1)
    bell.cx(0,1)
    bell.z(0)
    bell.measure([0,1],[0,1])
    print("psi minus outcomes:")
    run_circuit(bell)
    print("\n","Circuit diagram")
    print(bell.draw("text"))  

phi_plus()
phi_minus()
psi_plus()
psi_minus()      
