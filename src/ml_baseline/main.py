import typer
from ml_baseline.sample_data import make_sample_feature_table
app = typer.Typer()

@app.command()
def make_sample_data():
    """Generate sample data for the project."""
    make_sample_feature_table()
    print(" Success! Sample data generated (Simulated).")

@app.command()
def help():
    """Generate sample data for the project."""
    print(" Success! Sample data generated (Simulated).")

if __name__ == "__main__":
    app()

