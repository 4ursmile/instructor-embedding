billboard_task_list = ['mscoco', 'cnndm', 'mt']
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('--model', default='large', type=str)
if __name__=='__main__':
    args = parser.parse_args()
    model = args.model
    if model not in ['base', 'large', 'xl']:
        raise ValueError(f'Invalid model: {model}. model must be one of [base, large, xl]')
    for task in billboard_task_list:
        os.system(f'./eval_billboard.sh {model} {task}')
        print('\n')