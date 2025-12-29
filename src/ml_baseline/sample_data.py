import numpy as np
import pandas as pd
from pathlib import Path

def make_sample_feature_table(*, root: Path | None = None, n_users: int = 50, seed: int = 0) -> Path:
    """Write a small, deterministic feature table for local demos."""
   
    output_dir = Path(root) if root is not None else Path.cwd() # the path of output_dir is enterd by user or it is the current dir
    output_dir.mkdir(parents=True, exist_ok=True) # create the dir if it does not exist
    #parents=True: create parent directories if they do not exist
    #exist_ok=True: do not raise an error if the directory already exists
    output_path = output_dir / "sample_features.csv"

    rng = np.random.default_rng(seed) # create a random number generator with the given seed for reproducibility
    user_id = [f"u{i:03d}" for i in range(1, n_users + 1)] 
    country = rng.choice(["SA","AE","QA"], size=n_users, replace=True)
    n_orders = rng.integers(1, 10, size=n_users)
    avg_amount = rng.normal(loc=10, scale=3, size=n_users).clip(min=1)
    total_amount = n_orders * avg_amount

    # simple binary target (demo only)
    is_high_value = (total_amount >= 80).astype(int)

    df = pd.DataFrame({
        "user_id": user_id,
        "country": country,
        "n_orders": n_orders,
        "avg_amount": avg_amount.round(2),
        "total_amount": total_amount.round(2), 
        "is_high_value": is_high_value    
    })
    
    df.to_csv(output_path, index=False)
    return output_path

# ext= best_effort_ext()
# out_path

# df = make_sample_feature_table()
# print(df.head())
