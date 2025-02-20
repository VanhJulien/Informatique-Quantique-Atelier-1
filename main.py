from qiskit_ibm_runtime import QiskitRuntimeService
from dotenv import load_dotenv
from qiskit import QuantumCircuit
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler
import os

load_dotenv()
 
QiskitRuntimeService.save_account(
  token=os.getenv("IBM_TOKEN"),
  channel="ibm_quantum" # `channel` distinguishes between different account types
)

 
# Create empty circuit
example_circuit = QuantumCircuit(2)
example_circuit.measure_all()
 
# You'll need to specify the credentials when initializing QiskitRuntimeService, if they were not previously saved.
service = QiskitRuntimeService()
backend = service.least_busy(operational=True, simulator=False)
 
sampler = Sampler(backend)
job = sampler.run([example_circuit])
print(f"job id: {job.job_id()}")
result = job.result()
print(result)