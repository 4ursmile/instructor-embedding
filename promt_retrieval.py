promt_retrieval_task_list = ['rte','sst5','mrpc','dbpedia_14','hellaswag']
model = 'large'
import os
for task in promt_retrieval_task_list:
    os.system(f'./eval_promt_retrieval.sh {model} {task}')
    print('\n')