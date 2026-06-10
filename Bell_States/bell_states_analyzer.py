from qiskit import QuantumCircuit
from qiskit_ibm_runtime import QiskitRuntimeService
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager 
from qiskit_ibm_runtime import SamplerV2 as Sampler
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
from qiskit_ibm_runtime import EstimatorV2 as Estimator
from qiskit.quantum_info import SparsePauliOp

service=QiskitRuntimeService()
backend=service.least_busy(
    operational=True,
    simulator=False
)
print("Quantum Computer Name:", backend.name)
passmanager=generate_preset_pass_manager(
    target=backend.target,
    optimization_level=3
    )
J=1.0
hx=-0.5

def Hamiltonian_new(circuit):
    Hamiltonian=SparsePauliOp.from_list([("ZZ",J),("XI",hx),("IX",hx)])
    Hamiltonian_newlayout=Hamiltonian.apply_layout(
        layout=circuit.layout
    )
    return Hamiltonian_newlayout
   
def sampler_run(circuit):
    sampler=Sampler(mode=backend)
    return sampler.run([circuit],shots=1000)

def estimator_run(circuit,observable):
    estimator=Estimator(mode=backend)
    return estimator.run([(circuit,observable)])

def bell_state1():
    bell1 = QuantumCircuit(2)
    bell1.h(0)
    bell1.cx(0,1)
    compiled_estimator_circuit1 = passmanager.run(bell1)
    observable1 = Hamiltonian_new(compiled_estimator_circuit1)
    Job = estimator_run(compiled_estimator_circuit1,observable1 )
    estimator_results = Job.result()
    print("\nEnergy =", estimator_results[0].data.evs)
    bell1_sampler = bell1.copy()
    bell1_sampler.measure_all()
    compiled_sampler_circuit = passmanager.run(bell1_sampler)
    Job1 = sampler_run(compiled_sampler_circuit)
    sampler_results = Job1.result()
    counts = sampler_results[0].data.meas.get_counts()
    print(counts)
    plot_histogram(counts)
    plt.show()

def bell_state2():
    bell2=QuantumCircuit(2)
    bell2.h(0)
    bell2.cx(0,1)
    bell2.z(0)
    compiled_estimator_circuit2 = passmanager.run(bell2)
    observable2 = Hamiltonian_new(compiled_estimator_circuit2)
    Job = estimator_run(compiled_estimator_circuit2,observable2 )
    estimator_results = Job.result()
    print("\nEnergy =", estimator_results[0].data.evs)
    bell2_sampler = bell2.copy()
    bell2_sampler.measure_all()
    compiled_sampler_circuit = passmanager.run(bell2_sampler)
    Job1 = sampler_run(compiled_sampler_circuit)
    sampler_results = Job1.result()
    counts = sampler_results[0].data.meas.get_counts()
    print(counts)
    plot_histogram(counts)
    plt.show()

def bell_state3():
    bell3=QuantumCircuit(2)
    bell3.h(0)
    bell3.x(1)
    bell3.cx(0,1)
    compiled_estimator_circuit3 = passmanager.run(bell3)
    observable3 = Hamiltonian_new(compiled_estimator_circuit3)
    Job = estimator_run(compiled_estimator_circuit3,observable3 )
    estimator_results = Job.result()
    print("\nEnergy =", estimator_results[0].data.evs)
    bell3_sampler = bell3.copy()
    bell3_sampler.measure_all()
    compiled_sampler_circuit = passmanager.run(bell3_sampler)
    Job1 = sampler_run(compiled_sampler_circuit)
    sampler_results = Job1.result()
    counts = sampler_results[0].data.meas.get_counts()
    print(counts)
    plot_histogram(counts)
    plt.show()

def bell_state4():
    bell4=QuantumCircuit(2)
    bell4.h(0)
    bell4.x(1)
    bell4.cx(0,1)
    bell4.z(0)
    compiled_estimator_circuit4 = passmanager.run(bell4)
    observable4 = Hamiltonian_new(compiled_estimator_circuit4)
    Job = estimator_run(compiled_estimator_circuit4,observable4 )
    estimator_results = Job.result()
    print("\nEnergy =", estimator_results[0].data.evs)
    bell4_sampler = bell4.copy()
    bell4_sampler.measure_all()
    compiled_sampler_circuit = passmanager.run(bell4_sampler)
    Job1 = sampler_run(compiled_sampler_circuit)
    sampler_results = Job1.result()
    counts = sampler_results[0].data.meas.get_counts()
    print(counts)
    plot_histogram(counts)
    plt.show()

bell_state1()
bell_state2()
bell_state3()
bell_state4()
