import argparse
import os
import re
from collections import defaultdict
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument("--num", type=int, required=True)
parser.add_argument("--out", type=str, required=True)
parser.add_argument("--tsv", type=str, required=True)
parser.add_argument("--files", nargs="+", required=True)
args = parser.parse_args()

data = defaultdict(list)
for path in args.files:
    match = re.search(r"_k(\d+)_r\d+\.txt$", path)
    if not match:
        continue
    k = int(match.group(1))
    with open(path) as f:
        data[k].append(float(f.read().strip()))

os.makedirs(os.path.dirname(args.tsv), exist_ok=True)
with open(args.tsv, "w") as f:
    f.write("k\tmean\n")
    for k in sorted(data.keys()):
        for mean in data[k]:
            f.write(f"{k}\t{mean}\n")

ks = sorted(data.keys())
fig, ax = plt.subplots(figsize=(12, 5))
ax.boxplot([data[k] for k in ks], labels=[f"k={k}" for k in ks], widths=0.5)
ax.axhline((args.num + 1) / 2, color="gray", linestyle="--", linewidth=0.8)
ax.set_ylabel("Mean")
ax.set_title(f"Testing Draws for {args.num}")

os.makedirs(os.path.dirname(args.out), exist_ok=True)
plt.tight_layout()
plt.savefig(args.out)
plt.close()
