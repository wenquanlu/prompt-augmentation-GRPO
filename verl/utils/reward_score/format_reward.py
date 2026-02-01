import re

def abel_format_reward(completion):
    return 1.0

def simplerl_format_reward(completion):
    return 1.0

def qwen_math_format_reward(completion):
    return 1.0


def open_r1_format_reward(completion):
    """Reward function that checks if the reasoning process is enclosed within <think> and </think> tags, while the final answer is enclosed within <answer> and </answer> tags."""
    count = 0.0
    if completion.count("<think>\n") == 1:
        count += 0.25
    if completion.count("\n</think>\n") == 1:
        count += 0.25
    if completion.count("\n<answer>\n") == 1:
        count += 0.25
    if completion.count("\n</answer>") == 1:
        count += 0.25
    return count

def open_r1_teacher_format_reward(completion):
    count = 0.0
    if completion.count("\n</think>\n") == 1:
        count += 1/3
    if completion.count("\n<answer>\n") == 1:
        count += 1/3
    if completion.count("\n</answer>") == 1:
        count += 1/3
    return count

def deepseek_r1_format_reward(completion):
    count = 0.0
    if completion.count("<think>") == 1:
        count += 0.25
    if completion.count("</think>") == 1:
        count += 0.25
    if completion.count("<answer>") == 1:
        count += 0.25
    if completion.count("</answer>") == 1:
        count += 0.25
    return count

def deepseek_r1_teacher_format_reward(completion):
    count = 0.0
    if completion.count("</think>") == 1:
        count += 1/3
    if completion.count("<answer>") == 1:
        count += 1/3
    if completion.count("</answer>") == 1:
        count += 1/3
    return count

def open_r1_format_reward_old(completion):
    """Reward function that checks if the reasoning process is enclosed within <think> and </think> tags, while the final answer is enclosed within <answer> and </answer> tags."""
    pattern = r"^<think>\n.*?\n</think>\n<answer>\n.*?\n</answer>$"
    matches = re.match(pattern, completion, re.DOTALL | re.MULTILINE) 
    return 1.0 if matches else 0.0


def deepseek_r1_format_reward_old(completion):
    pattern = r"^<think>.*?</think> <answer>.*?</answer>$"
    matches = re.match(pattern, completion, re.DOTALL | re.MULTILINE) 
    return 1.0 if matches else 0.0


def formal_format_reward(completion):
    return 1.0

def lm_eval_prompt1_format_reward(completion):
    return 1.0 if completion.count("The final answer is:") == 1 else 0.0

def lm_eval_prompt2_format_reward(completion):
    if completion.count("## Step 1:") != 1:
        return 0.0
    if completion.count("## Step 2:") != 1:
        return 0.0
    if completion.count("The final answer is:") != 1:
        return 0.0
    return 1.0

def lm_eval_prompt4_format_reward(completion):
    return 1.0 if completion.count("The final answer is:") == 1 else 0.0

def lm_eval_prompt8_format_reward(completion):
    return 1.0

def reflective_prompt_format_reward(completion):
    count = 0.0
    if completion.count("<solution>\n") == 1:
        count += 0.25
    if completion.count("\n</solution>\n") == 1:
        count += 0.25
    if completion.count("\n<check>\nLet's verify step by step") == 1:
        count += 0.25
    if completion.count("\n</check>") == 1:
        count += 0.25
    return count

def reflective_prompt_teacher_format_reward(completion):
    count = 0.0
    if completion.count("\n</solution>\n") == 1:
        count += 1/3
    if completion.count("\n<check>\nLet's verify step by step") == 1:
        count += 1/3
    if completion.count("\n</check>") == 1:
        count += 1/3
    return count


FORMAT_REWARDS = {
    "abel": abel_format_reward,
    "simplerl": simplerl_format_reward,
    "qwen-math": qwen_math_format_reward,
    "open-r1": open_r1_format_reward,
    "open-r1-teacher": open_r1_teacher_format_reward,
    "deepseek-r1": deepseek_r1_format_reward,
    "deepseek-r1-teacher": deepseek_r1_teacher_format_reward,
    "formal": formal_format_reward,
    "lm_eval_prompt1": lm_eval_prompt1_format_reward,
    "lm_eval_prompt4": lm_eval_prompt4_format_reward,
    "lm_eval_prompt8": lm_eval_prompt8_format_reward,
    "reflective_prompt": reflective_prompt_format_reward,
    "reflective_prompt-teacher": reflective_prompt_teacher_format_reward
}

def get_format_reward(format_name, completion):
    if format_name not in FORMAT_REWARDS:
        raise ValueError(f"Unknown format reward: {format_name}")
    return FORMAT_REWARDS[format_name](completion)
