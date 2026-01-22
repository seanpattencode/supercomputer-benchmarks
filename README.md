# Supercomputer Benchmarks

Run 1990s supercomputer workloads on modern devices.

## Usage

```bash
# Quick benchmark (~2 seconds)
python3 benchmark.py

# Full benchmark (~3-5 minutes)
python3 benchmark_full.py
```

## Workloads

| Workload | 1990s Use Case |
|----------|----------------|
| Lorenz Attractor | Weather prediction, chaos theory |
| Matrix Multiply | LINPACK benchmark (THE supercomputer metric) |
| Heat Diffusion | CFD, aircraft design, reactor cooling |
| N-Body Molecular | Drug discovery, protein folding |
| Crypto Search | Code breaking, security research |

## Comparison

| System | Year | GFLOPS | Cost |
|--------|------|--------|------|
| Cray Y-MP | 1988 | 2.6 | $20M |
| Cray C90 | 1991 | 16 | $30M |
| CM-5 | 1991 | 32 | $5M |
| Raspberry Pi 4 | 2019 | ~3 | $55 |
| Budget Tablet | 2025 | ~3 | $111 |

A $111 tablet matches a 1988 Cray that cost $20 million.

## Requirements

- Python 3
- NumPy (optional, but recommended)

```bash
pip install numpy
```
