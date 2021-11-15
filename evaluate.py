import json
import argparse
import pandas as pd
import numpy as np

argument_parser = argparse.ArgumentParser(
    description="The evaluation script for the Emotional Mario Task at MediaEval 2021")

argument_parser.add_argument("-i", "--run-path", type=str, default=None)
argument_parser.add_argument("-t", "--truth-path", type=str, default=None)

infiles_gse = """D:\\DataSets\\EmotionalMario21\\runs\\team_gse\\new0.5\\participant2_Method1.json    D:\\DataSets\\EmotionalMario21\\truth\\participant_2_events.json  05m1
D:\\DataSets\\EmotionalMario21\\runs\\team_gse\\new0.5\\participant2_Method2.json    D:\\DataSets\\EmotionalMario21\\truth\\participant_2_events.json  05m2
D:\\DataSets\\EmotionalMario21\\runs\\team_gse\\new0.5\\participant4_Method1.json    D:\\DataSets\\EmotionalMario21\\truth\\participant_4_events.json  05m1
D:\\DataSets\\EmotionalMario21\\runs\\team_gse\\new0.5\\participant4_Method2.json    D:\\DataSets\\EmotionalMario21\\truth\\participant_4_events.json  05m2
D:\\DataSets\\EmotionalMario21\\runs\\team_gse\\new0.5\\participant7_Method1.json    D:\\DataSets\\EmotionalMario21\\truth\\participant_7_events.json  05m1
D:\\DataSets\\EmotionalMario21\\runs\\team_gse\\new0.5\\participant7_Method2.json    D:\\DataSets\\EmotionalMario21\\truth\\participant_7_events.json  05m2
D:\\DataSets\\EmotionalMario21\\runs\\team_gse\\new0.7\\participant2_Method2.json    D:\\DataSets\\EmotionalMario21\\truth\\participant_2_events.json  07m2
D:\\DataSets\\EmotionalMario21\\runs\\team_gse\\new0.7\\participant4_Method2.json    D:\\DataSets\\EmotionalMario21\\truth\\participant_4_events.json  07m2
D:\\DataSets\\EmotionalMario21\\runs\\team_gse\\new0.7\\participant7_Method2.json    D:\\DataSets\\EmotionalMario21\\truth\\participant_7_events.json  07m2
D:\\DataSets\\EmotionalMario21\\runs\\team_gse\\new0.9\\participant2_Method2.json    D:\\DataSets\\EmotionalMario21\\truth\\participant_2_events.json  09m2
D:\\DataSets\\EmotionalMario21\\runs\\team_gse\\new0.9\\participant4_Method2.json    D:\\DataSets\\EmotionalMario21\\truth\\participant_4_events.json  09m2
D:\\DataSets\\EmotionalMario21\\runs\\team_gse\\new0.9\\participant7_Method2.json    D:\\DataSets\\EmotionalMario21\\truth\\participant_7_events.json  09m2"""

infiles_dcu = """D:\\DataSets\\EmotionalMario21\\runs\\team_dcu\\participant_2.json  D:\\DataSets\\EmotionalMario21\\truth\\participant_2_events.json    run1
D:\\DataSets\\EmotionalMario21\\runs\\team_dcu\\participant_4.json  D:\\DataSets\\EmotionalMario21\\truth\\participant_4_events.json    run1
D:\\DataSets\\EmotionalMario21\\runs\\team_dcu\\participant_7.json  D:\\DataSets\\EmotionalMario21\\truth\\participant_7_events.json    run1"""

def evaluate(run, truth, df, runid="undefined", filename="undefined", max_distance=25):
    # compare everyone with everything ...
    # print("run identifier, events in run, events in truth, avg. distance, precision, recall")
    # print("length run:", len(run), ", length truth: ", len(truth))
    # for all events in the run data:
    matches = []
    cumulative_distance = 0
    for truth_evt in truth:
        # find the closest event in the truth data:
        curr_dist = max_distance
        curr_run_evt = None
        for run_evt in run:
            distance = abs(truth_evt['frame_number'] - run_evt['frame_number'])
            if abs(truth_evt['frame_number'] - run_evt['frame_number']) < curr_dist:
            # if abs(truth_evt['frame_number'] - run_evt['frame_number']) < curr_dist and truth_evt['event'] == run_evt['event']:
                curr_run_evt = truth_evt
                curr_dist = distance
        if curr_run_evt is not None:  # add it to the list if it is considered a find
            matches.append([truth_evt, curr_run_evt])
            cumulative_distance += curr_dist  # sum them up for the avg. distance

    # print(len(matches))

    # get all the numbers ...
    precision = len(matches) / len(run)
    recall = len(matches) / len(truth)
    if len(matches) > 0:
        avg_distance = cumulative_distance / len(matches)
    else:
        avg_distance = -1
    # print("%s, %s, %d, %d, %d, %0.4f, %0.4f, %0.4f, %0.4f"%(runid, filename, len(run), len(truth), len(matches), avg_distance, precision, recall, 2*(precision*recall)/(precision+recall)))
    f1 = 0
    if recall + precision > 0:
        f1 = 2 * (precision * recall) / (precision + recall)
    df.loc[-1] = [runid, filename, len(run), len(truth), len(matches), avg_distance, precision, recall, f1]
    df.index = df.index + 1  # shifting index
    df.sort_index()  # sorting by index


if __name__ == '__main__':
    args = argument_parser.parse_args()

    run_path = args.run_path
    truth_path = args.truth_path

    # check if needed args are here:
    #if run_path is None or truth_path is None:
    #    argument_parser.print_help()
    #    raise Exception("Please provide the paths to run and truth data.")

    # print header
    # print("run identifier, file, events in run, events in truth, number of matches, avg. distance, precision, recall, f1 score")
    df = pd.DataFrame(columns="run identifier, file, events in run, events in truth, number of matches, avg. distance, precision, recall, f1 score".split(sep=", "))
    my_max_distance = 25
    for input_path in infiles_dcu.split('\n'):
        tmp = input_path.strip().split()

        f1 = open(tmp[0])
        run = json.load(f1)

        f2 = open(tmp[1])
        truth = json.load(f2)

        evaluate(run, truth, df, tmp[2], tmp[0], max_distance=my_max_distance)

    grouped = df.groupby('run identifier')
    mp = grouped['precision'].agg(np.mean)
    mr = grouped['recall'].agg(np.mean)
    t1 = pd.DataFrame([mp, mr])
    evaluation = t1.T.assign(f1=lambda x: 2 * x['precision'] * x['recall'] / (x['precision'] + x['recall']))  # computing the f1 score from the averaged values.
    # print results
    print(df.sort_values('run identifier').to_csv())
    print(evaluation.to_csv())
    # write results to file
    file_header = 'team_dcu'
    df.sort_values('run identifier').to_csv('%s_detailed_%s_frames.csv' % ((file_header, my_max_distance)), index=None)
    evaluation.to_csv('%s_overall_%s_frames.csv' % ((file_header, my_max_distance)))