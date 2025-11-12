import pandas as pd


def load_data(filepath: str="../data/communes-france-2025.csv.gz") -> pd.DataFrame:
    
    d = {
        "code_insee": ["str", "insee_code"],
        "nom_standard": ["string", "name"],
        "dep_code": ["string", "dep_code"],
        "dep_nom": ["string", "dep_name"],
        "superficie_km2": ["float32", "area_km2"],
        "altitude_moyenne": ["float32", "mean_altitude_m"],
    }

    df = pd.read_csv(
        filepath,
        compression="gzip",
        usecols=d.keys(),
        dtype={k: v[0] for k, v in d.items()}
    ).rename(columns={k: v[1] for k, v in d.items()})
    
    return df