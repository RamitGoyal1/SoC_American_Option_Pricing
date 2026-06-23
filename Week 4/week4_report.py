import numpy as np
import matplotlib.pyplot as plt
from american_put import crr_put_price

S0, K, T, r, sigma = 100.0, 100.0, 1.0, 0.05, 0.25

print("==================================================")
print("WEEK 4 BASELINE PRICER REPORT EXECUTIONS")
print("==================================================")

euro_price = crr_put_price(S0, K, T, r, sigma, steps=500, american=False)
amer_price, boundary = crr_put_price(S0, K, T, r, sigma, steps=500, american=True)
premium = amer_price - euro_price

print(f"European Put Price (500 steps) : {euro_price:.4f}")
print(f"American Put Price (500 steps) : {amer_price:.4f}")
print(f"Early-Exercise Premium        : {premium:.4f}\n")

print("Step Count Convergence Table:")
print("-" * 45)
print("Steps | European Price | American Price | Premium")
print("-" * 45)
for n in [25, 50, 100, 200, 500, 1000]:
    e_p = crr_put_price(S0, K, T, r, sigma, steps=n, american=False)
    a_p, _ = crr_put_price(S0, K, T, r, sigma, steps=n, american=True)
    print(f"{n:5d} | {e_p:.4f}       | {a_p:.4f}       | {(a_p - e_p):.4f}")
print("-" * 45 + "\n")

print("Generating 3D Price Surface chart...")
spots = np.linspace(60, 140, 40)
maturities = np.linspace(0.05, 2.0, 30)
S_mesh, T_mesh = np.meshgrid(spots, maturities)
prices = np.zeros(S_mesh.shape)

for i, t_val in enumerate(maturities):
    for j, s_val in enumerate(spots):
        prices[i, j] = crr_put_price(s_val, K, t_val, r, sigma, steps=100, american=True)[0]

fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot(111, projection="3d")
surf = ax.plot_surface(S_mesh, T_mesh, prices, cmap="viridis", edgecolor='none')
ax.set_xlabel("Spot Price (S)")
ax.set_ylabel("Maturity (T)")
ax.set_zlabel("American Put Price")
ax.set_title("American Put Option Price Surface")
plt.tight_layout()
plt.savefig("figures/price_surface.png")
plt.close()

print("Generating 2D Early Exercise Boundary line chart...")
times = [t for t, _ in boundary]
spots_boundary = [s for _, s in boundary]

plt.figure(figsize=(7, 4))
plt.plot(times, spots_boundary, color="crimson", linewidth=2.0, label="Boundary S*(t)")
plt.axhline(K, color="black", linestyle="--", alpha=0.5, label="Strike K")
plt.xlabel("Time to Maturity (t in Years)")
plt.ylabel("Highest Exercise Stock Price")
plt.title("American Put Option Early Exercise Boundary")
plt.legend()
plt.grid(True, linestyle=":", alpha=0.6)
plt.tight_layout()
plt.savefig("figures/exercise_boundary.png")
plt.close()

print("All report tasks executed. Visual charts saved.")
