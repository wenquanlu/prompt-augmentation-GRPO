
templates_teacher_forcing = {
    "abel": """
{{- '<|im_start|>system\nPlease reason step by step, and put your final answer within \\\\boxed{}.<|im_end|>\n' }}
{%- for message in messages %}
    {%- if (message.role == "user") %}
        {{- '<|im_start|>' + message.role + '\n' + message.content + '<|im_end|>' + '\n' }}
    {%- endif %}
{%- endfor %}
{%- if add_generation_prompt %}
    {{- '<|im_start|>assistant\n' + "Let's think step by step.\n" }}
{%- endif %}
""",
    "simplerl": """
{{- '<|im_start|>system\nYou are a helpful assistant.<|im_end|>\n' }}
{%- for message in messages %}
    {%- if (message.role == "user") %}
        {{- '<|im_start|>' + message.role + '\n' + message.content + '\n' + 'Please reason step by step, and put your final answer within \\\\boxed{}.' + '<|im_end|>' + '\n' }}
    {%- endif %}
{%- endfor %}
{%- if add_generation_prompt %}
    {{- '<|im_start|>assistant\n' }}
{%- endif %}
""",
    "qwen-math": """
{{- '<|im_start|>system\nPlease reason step by step, and put your final answer within \\\\boxed{}.<|im_end|>\n' }}
{%- for message in messages %}
    {%- if (message.role == "user") %}
        {{- '<|im_start|>' + message.role + '\n' + message.content + '<|im_end|>' + '\n' }}
    {%- endif %}
{%- endfor %}
{%- if add_generation_prompt %}
    {{- '<|im_start|>assistant\n' }}
{%- endif %}
""",
    "open-r1": """
{{- '<|im_start|>system\nYou are a helpful AI Assistant that provides well-reasoned and detailed responses. You first think about the reasoning process as an internal monologue and then provide the user with the answer. Respond in the following format: <think>\n...\n</think>\n<answer>\n...\n</answer>\nInside the <answer>...</answer> block, the final answer must be enclosed in \\\\boxed{}.<|im_end|>\n' }}
{%- for message in messages %}
    {%- if (message.role == "user") %}
        {{- '<|im_start|>' + message.role + '\n' + message.content + '<|im_end|>' + '\n' }}
    {%- endif %}
{%- endfor %}
{%- if add_generation_prompt %}
    {{- '<|im_start|>assistant\n' }}
{%- endif %}
""",
    "open-r1-teacher": """
{{- '<|im_start|>system\nYou are a helpful AI Assistant that provides well-reasoned and detailed responses. You first think about the reasoning process as an internal monologue and then provide the user with the answer. Respond in the following format: <think>\n...\n</think>\n<answer>\n...\n</answer>\nInside the <answer>...</answer> block, the final answer must be enclosed in \\\\boxed{}.<|im_end|>\n' }}
{%- for message in messages %}
    {%- if (message.role == "user") %}
        {{- '<|im_start|>' + message.role + '\n' + message.content + '<|im_end|>' + '\n' }}
    {%- endif %}
{%- endfor %}
{%- if add_generation_prompt %}
    {{- '<|im_start|>assistant\n<think>\n' }}
{%- endif %}
""",
    "deepseek-r1": """
{{- '<|im_start|>system\nA conversation between User and Assistant. The User asks a question, and the Assistant solves it. The Assistant first thinks about the reasoning process in the mind and then provides the User with the answer. The reasoning process is enclosed within <think> </think> and answer is enclosed within <answer> </answer> tags, respectively, i.e., <think> reasoning process here </think> <answer> answer here </answer>. Inside the <answer>...</answer> block, the final answer must be enclosed in \\\\boxed{}.<|im_end|>\n' }}
{%- for message in messages %}
    {%- if (message.role == "user") %}
        {{- '<|im_start|>' + message.role + '\n' + message.content + '<|im_end|>' + '\n' }}
    {%- endif %}
{%- endfor %}
{%- if add_generation_prompt %}
    {{- '<|im_start|>assistant\n' }}
{%- endif %}
""",
    "deepseek-r1-teacher": """
{{- '<|im_start|>system\nA conversation between User and Assistant. The User asks a question, and the Assistant solves it. The Assistant first thinks about the reasoning process in the mind and then provides the User with the answer. The reasoning process is enclosed within <think> </think> and answer is enclosed within <answer> </answer> tags, respectively, i.e., <think> reasoning process here </think> <answer> answer here </answer>. Inside the <answer>...</answer> block, the final answer must be enclosed in \\\\boxed{}.<|im_end|>\n' }}
{%- for message in messages %}
    {%- if (message.role == "user") %}
        {{- '<|im_start|>' + message.role + '\n' + message.content + '<|im_end|>' + '\n' }}
    {%- endif %}
{%- endfor %}
{%- if add_generation_prompt %}
    {{- '<|im_start|>assistant\n<think>' }}
{%- endif %}
""",
    "formal": """
{{- '<|im_start|>system\nYou are an intelligent assistant who helps with user questions. Provide a rigorous, step-by-step derivation of the solution. The final answer must be clearly indicated within \\\\boxed{}.<|im_end|>\n' }}
{%- for message in messages %}
    {%- if (message.role == "user") %}
        {{- '<|im_start|>' + message.role + '\n' + message.content + '<|im_end|>' + '\n' }}
    {%- endif %}
{%- endfor %}
{%- if add_generation_prompt %}
    {{- '<|im_start|>assistant\n' }}
{%- endif %}    
""",
    "lm_eval_prompt1": """
{{- '<|im_start|>system\nSolve the following math challenge. Explain your approach step-by-step\nThe answer should end with: The final answer is: \\\\boxed{answer}\nwhere [answer] is just the final number or expression that solves the problem<|im_end|>\n' }}
{%- for message in messages %}
    {%- if (message.role == "user") %}
        {{- '<|im_start|>' + message.role + '\n' + message.content + '<|im_end|>' + '\n' }}
    {%- endif %}
{%- endfor %}
{%- if add_generation_prompt %}
    {{- "<|im_start|>assistant\nLet's think step by step" }}
{%- endif %}
""",
    "lm_eval_prompt2": """
{{- '<|im_start|>system\nYou should solve this math problem.\nFollow this structured format\n## Step 1: [Brief description]\n[Simple explanation and calculations]\n\n## Step 2: [Brief description]\n[Simple explanation and calculations]\n\nRepeat steps until your reach a solution<|im_end|>\n' }}
{%- for message in messages %}
    {%- if (message.role == "user") %}
        {{- '<|im_start|>' + message.role + '\n' + message.content + '\n' + 'End with:\nThe final answer is: \\\\boxed{answer}\nwhere [answer] is just the final number or expression that solves the problem.' + '<|im_end|>' + '\n' }}
    {%- endif %}
{%- endfor %}
{%- if add_generation_prompt %}
    {{- '<|im_start|>assistant\n' }}
{%- endif %}
""",
    "lm_eval_prompt2_teacher": """
{{- '<|im_start|>system\nYou should solve this math problem.\nFollow this structured format\n## Step 1: [Brief description]\n[Simple explanation and calculations]\n\n## Step 2: [Brief description]\n[Simple explanation and calculations]\n\nRepeat steps until your reach a solution<|im_end|>\n' }}
{%- for message in messages %}
    {%- if (message.role == "user") %}
        {{- '<|im_start|>' + message.role + '\n' + message.content + '\n' + 'End with:\nThe final answer is: \\\\boxed{answer}\nwhere [answer] is just the final number or expression that solves the problem.' + '<|im_end|>' + '\n' }}
    {%- endif %}
{%- endfor %}
{%- if add_generation_prompt %}
    {{- '<|im_start|>assistant\n## Step 1: ' }}
{%- endif %}
""",
    "lm_eval_prompt4": """
{{- '<|im_start|>system\nAnalyze and solve the math task.<|im_end|>\n' }}
{%- for message in messages %}
    {%- if (message.role == "user") %}
        {{- '<|im_start|>' + message.role + '\n' + message.content + '\n' + 'End the answer with:\nThe final answer is: \\\\boxed{answer} where [answer] is just the final number or expression that solves the problem.' + '<|im_end|>' + '\n' }}
    {%- endif %}
{%- endfor %}
{%- if add_generation_prompt %}
    {{- '<|im_start|>assistant\n' }}
{%- endif %}
""",
    "lm_eval_prompt8": """
{{- '<|im_start|>system\nSolve the following math problem\nShow each step of your solution\nPut the final answer within \\\\boxed{}<|im_end|>\n' }}
{%- for message in messages %}
    {%- if (message.role == "user") %}
        {{- '<|im_start|>' + message.role + '\n' + message.content + '<|im_end|>' + '\n' }}
    {%- endif %}
{%- endfor %}
{%- if add_generation_prompt %}
    {{- "<|im_start|>assistant\nLet's think step by step" }}
{%- endif %}
""",
    "react": """
{{- '<|im_start|>system\nYou are a helpful AI Assistant that solves math problems. You must solve the problem using the following iterative Thought-Action-Observation format.\nThought: reason about what mathematical step to take next\nAction: perform the actual mathematical computation\nObservation: analyze the result of the computation\nRepeat until you reach a solution. Put your final answer within \\\\boxed{}.<|im_end|>\n' }}
{%- for message in messages %}
    {%- if (message.role == "user") %}
        {{- '<|im_start|>' + message.role + '\n' + message.content + '<|im_end|>' + '\n' }}
    {%- endif %}
{%- endfor %}
{%- if add_generation_prompt %}
    {{- '<|im_start|>assistant\n' }}
{%- endif %}
""",
    "react_teacher": """
{{- '<|im_start|>system\nYou are a helpful AI Assistant that solves math problems. You must solve the problem using the following iterative Thought-Action-Observation format.\nThought: reason about what mathematical step to take next\nAction: perform the actual mathematical computation\nObservation: analyze the result of the computation\nRepeat until you reach a solution. Put your final answer within \\\\boxed{}.<|im_end|>\n' }}
{%- for message in messages %}
    {%- if (message.role == "user") %}
        {{- '<|im_start|>' + message.role + '\n' + message.content + '<|im_end|>' + '\n' }}
    {%- endif %}
{%- endfor %}
{%- if add_generation_prompt %}
    {{- '<|im_start|>assistant\nThought: ' }}
{%- endif %}
"""
}


