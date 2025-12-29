import typer
from ml_baseline.sample_data import make_sample_feature_table
from pathlib import Path
app = typer.Typer()


@app.command()
def make_sample_data(
    output_dir: Path = typer.Option( None, "--output-dir", "-o", help="Output directory"),
    n_users: int = typer.Option( 50, "--n-users", help="Number of users"),
    seed: int = typer.Option(0, "--seed", help="Random seed"), ):
    """
    Generate sample feature data.
    """
    path = make_sample_feature_table(
        root=output_dir,
        n_users=n_users,
        seed=seed,
    )
    typer.echo(f"Sample data written to: {path}")# print the path
@app.command()
def help():
    """Generate sample data for the project."""
    print(" Success! Sample data generated (Simulated).")

@app.command()
def hello():
    print(f"hello, this is command you can use\nhelp\nmake_sample_data")

if __name__ == "__main__":
    app()

