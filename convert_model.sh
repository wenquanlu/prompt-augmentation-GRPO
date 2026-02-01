#!/bin/bash

#SBATCH -n 1
#SBATCH -c 16
#SBATCH --gres=gpu:1
#SBATCH --nodes=1
#SBATCH -t 48:00:00
#SBATCH -p YOUR_PARTITION
#SBATCH --output=./slurm/%x-%j.out
#SBATCH --error=./slurm/%x-%j.err

source ~/anaconda3/etc/profile.d/conda.sh
conda activate verl2

BASE_DIR="checkpoints/verl_dapo_math_lvl3to5/qwen_math_1.5b_mix"
for step in $(seq 20 20 3960); do
    echo "===== Processing global_step_${step} ====="

    ACTOR_DIR="${BASE_DIR}/global_step_${step}/actor"
    TARGET_DIR="${ACTOR_DIR}/weight"

    if [ -d "${TARGET_DIR}" ]; then
        echo "Skipping global_step_${step}: weight directory already exists"
        continue
    fi
    
    # create target dir if not exists
    mkdir -p "${TARGET_DIR}"

    # merge FSDP shards
    python -m verl.model_merger merge \
        --backend fsdp \
        --local_dir "${ACTOR_DIR}" \
        --target_dir "${TARGET_DIR}"

done