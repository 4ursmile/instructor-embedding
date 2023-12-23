TASK_LIST_CLASSIFICATION = [
    "AmazonCounterfactualClassification",
    "AmazonPolarityClassification",
    "AmazonReviewsClassification",
    "Banking77Classification",
    "EmotionClassification",
    "ImdbClassification",
    "MassiveIntentClassification",
    "MassiveScenarioClassification",
    "MTOPDomainClassification",
    "MTOPIntentClassification",
    "ToxicConversationsClassification",
    "TweetSentimentExtractionClassification",
]

TASK_LIST_CLUSTERING = [
    "ArxivClusteringP2P",
    "ArxivClusteringS2S",
    "BiorxivClusteringP2P",
    "BiorxivClusteringS2S",
    "MedrxivClusteringP2P",
    "MedrxivClusteringS2S",
    "RedditClustering",
    "RedditClusteringP2P",
    "StackExchangeClustering",
    "StackExchangeClusteringP2P",
    "TwentyNewsgroupsClustering",
]

TASK_LIST_PAIR_CLASSIFICATION = [
    "SprintDuplicateQuestions",
    "TwitterSemEval2015",
    "TwitterURLCorpus",
]

TASK_LIST_RERANKING = [
    "AskUbuntuDupQuestions",
    "MindSmallReranking",
    "SciDocsRR",
    "StackOverflowDupQuestions",
]

TASK_LIST_RETRIEVAL = [
    "ArguAna",
    "ClimateFEVER",
    "CQADupstackAndroidRetrieval",
    "CQADupstackEnglishRetrieval",
    "CQADupstackGamingRetrieval",
    "CQADupstackGisRetrieval",
    "CQADupstackMathematicaRetrieval",
    "CQADupstackPhysicsRetrieval",
    "CQADupstackProgrammersRetrieval",
    "CQADupstackStatsRetrieval",
    "CQADupstackTexRetrieval",
    "CQADupstackUnixRetrieval",
    "CQADupstackWebmastersRetrieval",
    "CQADupstackWordpressRetrieval",
    "DBPedia",
    "FEVER",
    "FiQA2018",
    "HotpotQA",
    "MSMARCO",
    "NFCorpus",
    "NQ",
    "QuoraRetrieval",
    "SCIDOCS",
    "SciFact",
    "Touche2020",
    "TRECCOVID",
]

TASK_LIST_STS = [
    "BIOSSES",
    "SICK-R",
    "STS12",
    "STS13",
    "STS14",
    "STS15",
    "STS16",
    "STS17",
    "STS22",
    "STSBenchmark",
    "SummEval",
]
choice_list = ['classification', 'clustering', 'pair_classification', 'reranking', 'retrieval', 'sts']
mteb_task_list = [TASK_LIST_CLASSIFICATION, TASK_LIST_CLUSTERING, TASK_LIST_PAIR_CLASSIFICATION, TASK_LIST_RERANKING, TASK_LIST_RETRIEVAL, TASK_LIST_STS]
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('--model', default='large', type=str)
parser.add_argument('--task', default='all', choices=['all', 'classification', 'clustering', 'pair_classification', 'reranking', 'retrieval', 'sts'], type=str)
mteb_task_dic = {choice_list[i]: mteb_task_list[i] for i in range(len(choice_list))}
if __name__ == '__main__':
    args = parser.parse_args()
    model = args.model
    if model not in ['base', 'large', 'xl']:
        raise ValueError(f'Invalid model: {model}. model must be one of [base, large, xl]')
    if args.task == 'all':
        for tasks in mteb_task_list:
            for task in tasks:
                os.system(f'./eval.sh {model} {task}')
                print('\n')
    else:
        if args.task not in choice_list:
            raise ValueError(f'Invalid task: {args.task}. task must be one of [classification, clustering, pair_classification, reranking, retrieval, sts]')
        for task in mteb_task_dic[args.task]:
            os.system(f'./eval.sh {model} {task}')
            print('\n')