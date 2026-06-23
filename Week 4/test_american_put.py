import pytest
from american_put import crr_put_price

def test_american_vs_european():
    args = dict(S0=100, K=100, T=1.0, r=0.05, sigma=0.25, steps=200)
    amer_price, _ = crr_put_price(**args, american=True)
    euro_price = crr_put_price(**args, american=False)
    assert amer_price >= euro_price

def test_put_monotonicity_in_spot():
    low_spot, _ = crr_put_price(S0=80, K=100, T=1.0, r=0.05, sigma=0.25, steps=200, american=True)
    high_spot, _ = crr_put_price(S0=120, K=100, T=1.0, r=0.05, sigma=0.25, steps=200, american=True)
    assert low_spot > high_spot

def test_put_monotonicity_in_volatility():
    low_vol, _ = crr_put_price(S0=100, K=100, T=1.0, r=0.05, sigma=0.15, steps=200, american=True)
    high_vol, _ = crr_put_price(S0=100, K=100, T=1.0, r=0.05, sigma=0.35, steps=200, american=True)
    assert high_vol >= low_vol

if __name__ == "__main__":
    test_american_vs_european()
    test_put_monotonicity_in_spot()
    test_put_monotonicity_in_volatility()
    print("All tests passed!")
