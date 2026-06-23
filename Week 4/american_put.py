import math
import numpy as np

def crr_put_price(S0, K, T, r, sigma, steps, american=True):
    """
    Prices European and American puts using a Cox-Ross-Rubinstein tree.
    Returns:
        If american=True: (price, boundary_list)
        If american=False: price
    """
    if S0 <= 0 or K <= 0:
        raise ValueError("S0 and K must be strictly positive.")
    if T <= 0:
        return max(K - S0, 0.0), [] if american else max(K - S0, 0.0)
    if sigma <= 0:
        raise ValueError("Volatility must be strictly positive.")
    if int(steps) != steps or steps < 1:
        raise ValueError("Steps must be a positive integer.")

    steps = int(steps)
    dt = T / steps
    u = math.exp(sigma * math.sqrt(dt))
    d = 1.0 / u
    growth = math.exp(r * dt)
    p = (growth - d) / (u - d)
    disc = math.exp(-r * dt)

    if not (0.0 < p < 1.0):
        raise ValueError("No-arbitrage condition violated. Increase steps.")

    j = np.arange(steps + 1)
    stock = S0 * (u ** j) * (d ** (steps - j))
    value = np.maximum(K - stock, 0.0)
    
    boundary = []

    for i in range(steps - 1, -1, -1):
        continuation = disc * (p * value[1:i + 2] + (1.0 - p) * value[0:i + 1])
        
        if american:
            j = np.arange(i + 1)
            stock = S0 * (u ** j) * (d ** (i - j))
            exercise = np.maximum(K - stock, 0.0)
            
            exercise_now = exercise > (continuation + 1e-10)
            if np.any(exercise_now):
                highest_exercise_stock = float(np.max(stock[exercise_now]))
                boundary.append((i * dt, highest_exercise_stock))
                
            value = np.maximum(continuation, exercise)
        else:
            value = continuation

    if american:
        boundary.reverse()
        return float(value[0]), boundary
    else:
        return float(value[0])
