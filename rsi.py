import pandas as pd

def calculate_rsi(data, period=14):
    """
    Calculate the Relative Strength Index (RSI) for a given data series.

    Args:
        data (list or pd.Series): List of closing prices or a Pandas Series.
        period (int): Number of periods to consider for RSI calculation. Default is 14.

    Returns:
        pd.Series: RSI values for each corresponding data point.
    """
    # Calculate price changes
    delta = data.diff()

    # Get positive and negative price changes
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    # Calculate average gain and average loss over the specified period
    avg_gain = gain.rolling(window=period).mean()
    avg_loss = loss.rolling(window=period).mean()

    # Calculate relative strength (RS)
    rs = avg_gain / avg_loss

    # Calculate RSI using the RS
    rsi = 100 - (100 / (1 + rs))

    return rsi

# Example usage:
# Assuming you have a pandas DataFrame with a 'Close' column containing the closing prices
# and you want to calculate the RSI for that column.

# Load data from a CSV file
df = pd.read_csv('your_data.csv')

# Calculate RSI for the 'Close' column
rsi_values = calculate_rsi(df['Close'])

# Print the RSI values
print(rsi_values)
