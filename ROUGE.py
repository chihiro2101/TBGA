import os
from rouge import FilesRouge
from rouge import Rouge
import nltk
from shutil import copyfile
import statistics as sta



def main():
    hyp = 'hyp'
    raw_ref = 'sum'    
    FJoin = os.path.join
    files_hyp = [FJoin(hyp, f) for f in os.listdir(hyp)]
    files_raw_ref = [FJoin(raw_ref, f) for f in os.listdir(raw_ref)]
    
    f_hyp = []
    f_raw_ref = []
    for file in files_hyp:
        f = open(file)
        f_hyp.append(f.read())
        f.close()
    for file in files_raw_ref:
        f = open(file)
        f_raw_ref.append(f.read())
        f.close()
        
    # import pdb
    # pdb.set_trace()
    rouge_1_tmp = []
    rouge_2_tmp = []
    rouge_L_tmp = []
    number = 1
    for hyp, ref in zip(f_hyp, f_raw_ref):
        rouge = Rouge()
        scores = rouge.get_scores(hyp, ref, avg=True)
        rouge_1 = scores["rouge-1"]["f"]
        rouge_2 = scores["rouge-2"]["f"]
        rouge_L = scores["rouge-l"]["f"]
        rouge_1_tmp.append(rouge_1)
        rouge_2_tmp.append(rouge_2)
        rouge_L_tmp.append(rouge_L)
        # import pdb; pdb.set_trace()
        # print(number)
        # print(scores)
        # number +=1
    rouge_1_avg = sta.mean(rouge_1_tmp)
    rouge_2_avg = sta.mean(rouge_2_tmp)
    rouge_L_avg = sta.mean(rouge_L_tmp)
    print('Rouge-1')
    print(rouge_1_avg)
    print('Rouge-2')
    print(rouge_2_avg)
    print('Rouge-L')
    print(rouge_L_avg)


if __name__ == "__main__":
    main()

