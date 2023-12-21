cd evaluation/MTEB
pip install mteb
pip install mteb[beir]
echo "Successfully installed MTEB"
cd ../..
cd evaluation/text_evaluation
mkdir cache
echo "Successfully created cache folder"
cd ../..
cd evaluation/prompt_retrieval
mkdir outputs
mkdir cache
echo "Successfully created outputs and cache folder"
cd ../..
chmod 777 eval_promt_retrieval.sh
chmod 777 eval_billboard.sh
chmod 777 eval.sh
echo "Successfully Set up the evaluation folder"