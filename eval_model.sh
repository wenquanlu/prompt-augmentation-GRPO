#!/bin/bash

#SBATCH -n 1
#SBATCH -c 16
#SBATCH --gres=gpu:nvidia_l40s:1
#SBATCH --nodes=1
#SBATCH -t 48:00:00
#SBATCH -p YOUR_PARTITION
#SBATCH --output=./slurm/%x-%j.out
#SBATCH --error=./slurm/%x-%j.err

source ~/anaconda3/etc/profile.d/conda.sh
conda activate verl2

python evaluate_model.py --model_name checkpoints/verl_dapo_math_lvl3to5/qwen_math_1.5b_mix/global_step_2820/actor/weight