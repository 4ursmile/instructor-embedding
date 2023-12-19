#!/bin/sh
cd evaluation/MTEB
python examples/evaluate_model.py --model_name "hkunlp/instructor-$1" --output_dir outputs --task_name $2 --result_file results
cd ../..