#!/usr/bin/env python3
"""1990s Supercomputer Workload Simulations - run on a tablet!"""

import time
import sys

def check_numpy():
    try:
        import numpy as np
        return True
    except ImportError:
        return False

HAS_NUMPY = check_numpy()

if HAS_NUMPY:
    import numpy as np

def header(title):
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}")

# ============================================================
# 1. WEATHER SIMULATION (Lorenz Attractor - Chaos Theory)
#    Used for: Understanding atmospheric unpredictability
#    1990s use: Early weather models, "butterfly effect"
# ============================================================
def weather_lorenz(steps=100000):
    """Lorenz attractor - foundation of chaos theory in weather."""
    header("WEATHER: Lorenz Attractor (Chaos Theory)")
    print("This model showed why weather is hard to predict long-term")
    print(f"Simulating {steps:,} timesteps...")

    # Lorenz parameters
    sigma, rho, beta = 10.0, 28.0, 8.0/3.0
    dt = 0.01
    x, y, z = 1.0, 1.0, 1.0

    start = time.time()
    for _ in range(steps):
        dx = sigma * (y - x)
        dy = x * (rho - z) - y
        dz = x * y - beta * z
        x += dx * dt
        y += dy * dt
        z += dz * dt
    elapsed = time.time() - start

    print(f"Final state: x={x:.4f}, y={y:.4f}, z={z:.4f}")
    print(f"Time: {elapsed:.3f}s | {steps/elapsed:,.0f} steps/sec")
    return elapsed

# ============================================================
# 2. MOLECULAR DYNAMICS (N-body simulation)
#    Used for: Drug discovery, protein folding
#    1990s use: Early HIV research, material science
# ============================================================
def molecular_dynamics(n_atoms=200, steps=500):
    """Simple N-body molecular dynamics."""
    header("MOLECULAR DYNAMICS: N-Body Simulation")
    print(f"Simulating {n_atoms} atoms for {steps} steps...")
    print("1990s: Used for drug discovery, protein research")

    if not HAS_NUMPY:
        print("(Requires numpy - skipping)")
        return 0

    # Initialize random positions and velocities
    np.random.seed(42)
    pos = np.random.randn(n_atoms, 3) * 10
    vel = np.random.randn(n_atoms, 3) * 0.1
    mass = np.ones(n_atoms)
    dt = 0.01

    start = time.time()
    for step in range(steps):
        # Compute pairwise forces (O(n²) - classic approach)
        forces = np.zeros_like(pos)
        for i in range(n_atoms):
            for j in range(i+1, n_atoms):
                r = pos[j] - pos[i]
                dist = np.sqrt(np.sum(r**2)) + 0.1  # softening
                f = r / (dist**3)  # simplified gravity-like
                forces[i] += f
                forces[j] -= f

        # Update velocities and positions
        vel += forces * dt / mass[:, np.newaxis]
        pos += vel * dt

    elapsed = time.time() - start
    interactions = n_atoms * (n_atoms-1) // 2 * steps
    print(f"Interactions computed: {interactions:,}")
    print(f"Time: {elapsed:.3f}s | {interactions/elapsed:,.0f} interactions/sec")
    return elapsed

# ============================================================
# 3. CFD - HEAT DIFFUSION (2D Laplace equation)
#    Used for: Aerodynamics, engine design, weather
#    1990s use: Aircraft design, nuclear reactor cooling
# ============================================================
def heat_diffusion(grid_size=100, iterations=1000):
    """2D heat diffusion using finite differences."""
    header("CFD: 2D Heat Diffusion")
    print(f"Grid: {grid_size}x{grid_size} | Iterations: {iterations}")
    print("1990s: Aircraft design, reactor cooling simulation")

    if not HAS_NUMPY:
        print("(Requires numpy - skipping)")
        return 0

    # Initialize grid with boundary conditions
    grid = np.zeros((grid_size, grid_size))
    grid[0, :] = 100    # Top hot
    grid[-1, :] = 0     # Bottom cold
    grid[:, 0] = 50     # Left warm
    grid[:, -1] = 50    # Right warm

    start = time.time()
    for _ in range(iterations):
        # Jacobi iteration (classic method)
        grid[1:-1, 1:-1] = 0.25 * (
            grid[:-2, 1:-1] + grid[2:, 1:-1] +
            grid[1:-1, :-2] + grid[1:-1, 2:]
        )

    elapsed = time.time() - start
    cells = (grid_size-2)**2 * iterations
    print(f"Cell updates: {cells:,}")
    print(f"Time: {elapsed:.3f}s | {cells/elapsed:,.0f} cells/sec")
    print(f"Center temp: {grid[grid_size//2, grid_size//2]:.2f}°")
    return elapsed

# ============================================================
# 4. MATRIX OPERATIONS (LINPACK-style)
#    Used for: Basically everything - the benchmark
#    1990s use: THE measure of supercomputer performance
# ============================================================
def matrix_benchmark(size=500):
    """Matrix multiplication - core supercomputer benchmark."""
    header("LINPACK-STYLE: Matrix Multiplication")
    print(f"Matrix size: {size}x{size}")
    print("1990s: THE supercomputer benchmark (still used today)")

    if not HAS_NUMPY:
        print("(Requires numpy - skipping)")
        return 0

    A = np.random.rand(size, size)
    B = np.random.rand(size, size)

    start = time.time()
    C = np.dot(A, B)
    elapsed = time.time() - start

    # 2*n³ FLOPs for matrix multiply
    flops = 2 * size**3
    gflops = flops / elapsed / 1e9

    print(f"Operations: {flops:,} FLOPs")
    print(f"Time: {elapsed:.3f}s")
    print(f"Performance: {gflops:.2f} GFLOPS")
    print(f"\n>>> This would rank as a TOP SUPERCOMPUTER in early 1990s!")
    return elapsed

# ============================================================
# 5. CRYPTANALYSIS (Brute force search)
#    Used for: Code breaking, security
#    1990s use: NSA, intelligence agencies
# ============================================================
def crypto_search(keyspace=5000000):
    """Brute force key search simulation."""
    header("CRYPTANALYSIS: Brute Force Search")
    print(f"Searching {keyspace:,} keys...")
    print("1990s: Code breaking, DES cracking attempts")

    target = hash("SECRET_KEY_12345") % keyspace

    start = time.time()
    found = None
    for key in range(keyspace):
        if hash(f"KEY_{key}") % keyspace == target:
            found = key
            # Keep searching to measure full speed
    elapsed = time.time() - start

    print(f"Keys tested: {keyspace:,}")
    print(f"Time: {elapsed:.3f}s | {keyspace/elapsed:,.0f} keys/sec")
    return elapsed

# ============================================================
# MAIN
# ============================================================
if __name__ == "__main__":
    print("="*60)
    print("  1990s SUPERCOMPUTER WORKLOADS ON YOUR TABLET")
    print("  Comparing to Cray C90 (~16 GFLOPS, $30 million)")
    print("="*60)

    total_start = time.time()

    weather_lorenz(100000)
    molecular_dynamics(150, 300)
    heat_diffusion(100, 1000)
    matrix_benchmark(400)
    crypto_search(3000000)

    total = time.time() - total_start

    print("\n" + "="*60)
    print("  SUMMARY")
    print("="*60)
    print(f"Total time: {total:.1f}s")
    print(f"""
In the 1990s, these workloads required:
  - Cray C90: $30,000,000 + building + cooling + staff
  - Your tablet: $111 + pocket

Your tablet can simulate:
  ✓ Weather chaos (Lorenz attractor)
  ✓ Molecular interactions (drug research scale)
  ✓ Heat/fluid flow (2D CFD)
  ✓ Matrix math at ~1-5 GFLOPS (early 90s Cray level)
  ✓ Cryptographic key search

Not bad for something that also plays YouTube.
""")
