import numpy as np

def gentrification_score_from_crime(df):
    # Use the most recent acceleration as the score (negative acceleration = improving)
    if 'acceleration' not in df.columns or df.empty:
        return 0.0
    recent_accel = df['acceleration'].iloc[-1]
    # Invert so that negative acceleration (declining crime) is positive for gentrification
    score = -recent_accel if not np.isnan(recent_accel) else 0.0
    return float(score) 