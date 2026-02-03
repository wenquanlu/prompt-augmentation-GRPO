#!/bin/bash
#SBATCH --ntasks-per-node=1
#SBATCH --gres=gpu:1
#SBATCH --partition=qed  # Adjust this for your cluster
#SBATCH --output=./slurm/%x-%j.out
#SBATCH --error=./slurm/%x-%j.err
#SBATCH --time=48:00:00
#SBATCH --nodes=1
#SBATCH --cpus-per-task=16

source ~/anaconda3/etc/profile.d/conda.sh
conda activate verl2



MODEL_NAME_OR_PATH="YOUR DOWNLOADED CHECKPOINT PATH"
N_REPEAT=5

for rep in $(seq 1 ${N_REPEAT}); do
    python evaluate_model.py --model_name ${MODEL_NAME_OR_PATH}
done

