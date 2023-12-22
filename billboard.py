billboard_task_list = ['mscoco', 'cnndm', 'mt']
model = 'large'
import os
for task in billboard_task_list:
    os.system(f'./eval_billboard.sh {model} {task}')
    print('\n')