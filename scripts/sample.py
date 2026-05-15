import argparse
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("--num", type=int, required=True)
parser.add_argument("--k", type=int, required=True)
parser.add_argument("--repeat", type=int, required=True)
parser.add_argument("--out", type=str, required=True)
args = parser.parse_args()

rng = np.random.default_rng(seed=args.repeat)
mean = rng.integers(1, args.num + 1, size=args.k).mean()

with open(args.out, "w") as f:
    f.write(f"{mean}\n")
