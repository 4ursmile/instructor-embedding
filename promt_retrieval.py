promt_retrieval_task_list = ['rte','sst5','mrpc','dbpedia_14','hellaswag']
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('--model', default='large', type=str)
if __name__=='__main__':
    args = parser.parse_args()
    model = args.model
    if model not in ['base', 'large', 'xl']:
        raise ValueError(f'Invalid model: {model}. model must be one of [base, large, xl]')
    for task in promt_retrieval_task_list:
        os.system(f'./eval_promt_retrieval.sh {model} {task}')
        print('\n')