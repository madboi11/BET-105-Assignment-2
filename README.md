# Law of Large Numbers – Snakemake Pipeline

This pipeline demonstrates the Law of Large Numbers graphically. Given a range **1 to n**, we repeatedly draw **k** values and compute their mean. As k increases, the sample mean converges to the true mean **(n + 1) / 2**. The experiment is repeated 10 times per k value and the distribution of means is shown as a boxplot.

## Example Output

<img width="1200" height="500" alt="lln_n1000" src="https://github.com/user-attachments/assets/120548a6-e6ea-4391-add8-cd931748ea0e" />


## Requirements

```
conda create -n snakemake -c conda-forge -c bioconda snakemake
conda activate snakemake
conda install matplotlib
```

## How to Run

```
snakemake --cores 4
```

To change parameters, edit `config.yaml` before running.

## Configuration

```yaml
num: 1000          # upper bound of the range [1, num]
repeats: 10        # number of repeated draws per k value
ks: [5, 10, 25, 50, 100, 200, 1000, 2000]   # draw sizes to test
```

## File Structure

```
.
├── Snakefile
├── config.yaml
├── README.md
├── scripts/
│   ├── sample.py       # draws k values from [1..num] and saves the mean
│   └── plot_lln.py     # aggregates all means into a TSV and generates the boxplot
└── results/
    ├── samples/        # one .txt file per (num, k, repeat) combination
    ├── nNUM_means.tsv  # aggregated results with columns: k, mean
    └── plots/
        └── lln_nNUM.png
```
