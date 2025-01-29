# Black-Scholes Option Pricing Model


import math
from scipy.stats import norm

# Input parameters
S = 43  # Underlying Price
K = 39  # Strike Price
T = 3   # Time to Expiration (in years)
r = 0.1 # Risk-Free Rate (annualized)
vol = 0.1 # Volatility (σ, annualized)

# Calculate d1 and d2
def calculate_d1(S, K, T, r, vol):
    """
    Calculate d1 for the Black-Scholes formula.
    """
    return (math.log(S / K) + (r + 0.5 * vol**2) * T) / (vol * math.sqrt(T))

def calculate_d2(d1, vol, T):
    """
    Calculate d2 for the Black-Scholes formula.
    """
    return d1 - (vol * math.sqrt(T))

# Calculate call and put option prices
def calculate_call_price(S, K, T, r, d1, d2):
    """
    Calculate the theoretical price of a European call option.
    """
    return S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)

def calculate_put_price(S, K, T, r, d1, d2):
    """
    Calculate the theoretical price of a European put option.
    """
    return K * math.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)

# Main function to run the Black-Scholes calculations
def black_scholes(S, K, T, r, vol):
    """
    Main function to calculate and display the results of the Black-Scholes model.
    """
    # Calculate d1 and d2
    d1 = calculate_d1(S, K, T, r, vol)
    d2 = calculate_d2(d1, vol, T)

    # Calculate call and put option prices
    call_price = calculate_call_price(S, K, T, r, d1, d2)
    put_price = calculate_put_price(S, K, T, r, d1, d2)

    # Display results
    print('The value of d1 is: ', round(d1, 4))
    print('The value of d2 is: ', round(d2, 4))
    print('The price of the call option is: $', round(call_price, 2))
    print('The price of the put option is: $', round(put_price, 2))

# Run the Black-Scholes model with the given parameters
if __name__ == "__main__":
    black_scholes(S, K, T, r, vol)