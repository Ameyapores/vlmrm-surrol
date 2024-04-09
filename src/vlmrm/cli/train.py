import typer

from vlmrm.trainer.train import train

def main():
    config = "/home/pores/Projects/vlmrm_surrol/config.yaml"  # Replace with the actual path to your config.yaml file
    train(config)

if __name__ == "__main__":
    typer.run(main)

# if __name__ == "__main__":
#     typer.run(train)
