#!/bin/sh
cd evaluation/text_evaluation
python main.py --cache cache --model_name "hkunlp/instructor-$1" --task $2 
cd ../..