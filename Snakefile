configfile: "config.yaml"

NUM = config["num"]
K = config["k"]
REPEATS = list(range(1, config["repeats"] + 1))

rule all:
    input:
        f"results/plots/lln_n{NUM}.png"

rule sample:
    output:
        "results/samples/n{num}_k{k}_r{repeat}.txt"
    shell:
        "python scripts/sample.py --num {wildcards.num} --k {wildcards.k} --repeat {wildcards.repeat} --out {output}"

rule plot:
    input:
        expand("results/samples/n{{num}}_k{k}_r{repeat}.txt", k=K, repeat=REPEATS)
    output:
        plot="results/plots/lln_n{num}.png",
        tsv="results/n{num}_means.tsv"
    shell:
        "python scripts/plot.py --num {wildcards.num} --out {output.plot} --tsv {output.tsv} --files {input}"
