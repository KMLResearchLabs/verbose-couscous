import pandas as pd


def export_to_csv(leads: list, filename: str = "leads.csv"):
    df = pd.DataFrame(leads)
    df.to_csv(filename, index=False)