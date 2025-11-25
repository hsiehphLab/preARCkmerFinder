#!/usr/bin/bash -l


#SBATCH --time=24:00:00
#SBATCH --mem=30g
#SBATCH --cpus-per-task=1

source /projects/standard/hsiehph/shared/bin/initialize_conda.sh
conda activate snakemake


snakemake -s make_meryl_database_and_remove_error_kmers.snake --jobname "{rulename}.{jobid}" --profile profile -w 60 --jobs 50 -p -k
