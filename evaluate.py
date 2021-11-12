import json
import argparse

argument_parser = argparse.ArgumentParser(description="The evaluation script for the Emotional Mario Task at MediaEval 2021")

argument_parser.add_argument("-i", "--run-path", type=str, default=None)
argument_parser.add_argument("-t", "--truth-path", type=str, default=None)

def evaluate(run, truth):
    print(run)

if __name__ == '__main__':
    args = argument_parser.parse_args()

    run_path = args.run_path
    truth_path = args.truth_path

    # check if needed args are here:
    if run_path is None or truth_path is None:
        argument_parser.print_help()
        raise Exception("Please provide the paths to run and truth data.")

    f1 = open(run_path)
    run = json.load(f1)

    f2 = open(truth_path)
    truth = json.load(f2)

    evaluate(run, truth)