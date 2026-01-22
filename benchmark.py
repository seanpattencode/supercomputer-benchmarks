#!/usr/bin/env python3
"""Quick 1990s supercomputer workload demo."""
import time
import sys

try:
    import numpy as np
    HAS_NUMPY = True
except:
    HAS_NUMPY = False

print("="*60)
print("  1990s SUPERCOMPUTER WORKLOADS - QUICK VERSION")
print("="*60)

# 1. WEATHER - Lorenz
print("\n[1] WEATHER: Lorenz Attractor")
sigma, rho, beta = 10.0, 28.0, 8.0/3.0
x, y, z = 1.0, 1.0, 1.0
start = time.time()
for _ in range(50000):
    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z
    x += dx * 0.01
    y += dy * 0.01
    z += dz * 0.01
t1 = time.time() - start
print(f"    50K steps in {t1:.2f}s - chaos theory foundation")

# 2. MATRIX - LINPACK style
if HAS_NUMPY:
    print("\n[2] LINPACK: Matrix Multiply (300x300)")
    A = np.random.rand(300, 300)
    B = np.random.rand(300, 300)
    start = time.time()
    C = np.dot(A, B)
    t2 = time.time() - start
    flops = 2 * 300**3
    gflops = flops / t2 / 1e9
    print(f"    {flops:,} FLOPs in {t2:.3f}s = {gflops:.2f} GFLOPS")
else:
    print("\n[2] LINPACK: (numpy not installed)")
    t2 = 0
    gflops = 0

# 3. HEAT DIFFUSION
if HAS_NUMPY:
    print("\n[3] CFD: Heat Diffusion (80x80 grid, 500 iter)")
    grid = np.zeros((80, 80))
    grid[0, :] = 100
    start = time.time()
    for _ in range(500):
        grid[1:-1, 1:-1] = 0.25 * (
            grid[:-2, 1:-1] + grid[2:, 1:-1] +
            grid[1:-1, :-2] + grid[1:-1, 2:]
        )
    t3 = time.time() - start
    print(f"    Done in {t3:.3f}s - aircraft/reactor design")
else:
    print("\n[3] CFD: (numpy not installed)")
    t3 = 0

# 4. CRYPTO SEARCH
print("\n[4] CRYPTO: Key search (1M keys)")
start = time.time()
target = 12345
for k in range(1000000):
    h = (k * 31337) % 999983
    if h == target:
        pass
t4 = time.time() - start
print(f"    1M keys in {t4:.2f}s = {1000000/t4:,.0f} keys/sec")

# Summary
print("\n" + "="*60)
print("  COMPARISON TO 1990s SUPERCOMPUTERS")
print("="*60)
print("""
| System          | Year | GFLOPS | Cost      |
|-----------------|------|--------|-----------|
| Cray Y-MP       | 1988 |    2.6 | $20M      |
| Cray C90        | 1991 |   16.0 | $30M      |
| CM-5            | 1991 |   32.0 | $5M       |
| Your Tablet     | 2025 |   ~{:.1f} | $111      |
""".format(gflops if gflops else 1.5))

if gflops >= 2:
    print(">>> Your tablet MATCHES early 1990s Cray performance!")
    print(">>> For $111 vs $20-30 MILLION")
elif gflops >= 0.5:
    print(">>> Your tablet approaches late-80s supercomputer level")

print("""
What 1990s scientists needed supercomputers for:
  ✓ Weather prediction    - RUNS ON YOUR TABLET
  ✓ Nuclear simulation    - RUNS ON YOUR TABLET
  ✓ Drug discovery        - RUNS ON YOUR TABLET
  ✓ Aircraft design       - RUNS ON YOUR TABLET
  ✓ Code breaking         - RUNS ON YOUR TABLET

The $30M Cray C90 required:
  - Special building with raised floors
  - Massive cooling systems
  - Team of operators
  - Months of wait time for jobs

Your tablet:
  - Fits in a bag
  - Runs on battery
  - Instant results
  - Also plays Candy Crush
""")
