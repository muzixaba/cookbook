import click
from prompt_toolkit import prompt

@click.command()
@click.option('--count', default=1,
            help="Number of greetings")
@click.option('--name', 
            help='The person to greet')
def hello(count, name):
    """Says hello to 'name', 'count' times"""
    for i in range(count):
        click.echo(f"Hello {name}")

if __name__ == "__main__":
    hello()