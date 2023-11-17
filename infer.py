import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.generation.utils import GenerationConfig


def predict_batch_test():
    model_path = 'mydir/Baichuan-13B-Chat'
    tokenizer = AutoTokenizer.from_pretrained(model_path, use_fast=False, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(model_path, device_map="auto", torch_dtype=torch.float16, trust_remote_code=True)
    model.generation_config = GenerationConfig.from_pretrained(model_path)
    messages_batch = []
    messages1 = [{"role": "user", "content": "世界上第二高的山峰是哪座"}]
    messages2 = [{"role": "user", "content": "中国的首都在哪"}]
    messages_batch.append(messages1)
    messages_batch.append(messages2)
    response = model.chat_batch(tokenizer, messages_batch)
    print(response)



if __name__ == '__main__':
    # CUDA_VISIBLE_DEVICES=0 python infer.py
    predict_batch_test()
