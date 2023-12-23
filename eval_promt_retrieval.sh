#!/bin/sh
cd evaluation/prompt_retrieval
python main.py --model_name "../../gpt-j-6b" --embedding_model "hkunlp/instructor-$1" --task $2 --model_cache_dir cache --output_dir outputs --add_prompt
cd ../..