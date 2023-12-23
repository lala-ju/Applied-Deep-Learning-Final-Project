import argparse
import json
import jsonlines

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pred", type=str, required=True)
    parser.add_argument("--ans", type=str, required=True)
    return parser.parse_args()

def main():
    args = parse_args()
    # pred = json.load(open(args.pred))
    pred = []
    with open(args.pred) as f:
        for line in f:
            pred.append(json.loads(line))
    ans = json.load(open(args.ans))
    
    exact_match = 0
    total = 0
    # Positive: Grammatically correct
    # Negative: Grammatically incorrect
    true_positive = 0
    true_negative = 0
    total_positive = 0
    total_negative = 0
    false_positve = 0
    
    for p, a in zip(pred, ans):
        assert(p["id"] == a["id"])
        if a["instruction"] == a["output"][0] and len(a["output"]) == 1:
            total_positive += 1
            if p["output"] == a["output"][0]:
                true_positive += 1
                exact_match += 1
        else:
            if p["output"] == a["instruction"]:
                false_positve += 1
            for ans in a:
                if p["output"] == ans:
                    exact_match += 1
                    true_negative += 1
                    break
            total_negative += 1
        total += 1
        
    print(f"Exact Match = {exact_match} / {total} = {exact_match / total}")
    print(f"Grammatically correct = {true_positive} / {total_positive}")
    print(f"Grammatically incorrect = {true_negative} / {total_negative}")
    print(f"Uncorrected = {false_positve}")
    
if __name__ == "__main__":
    main()