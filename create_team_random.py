import json
import argparse
import random

argument_parser = argparse.ArgumentParser(description="The evaluation script for the Emotional Mario Task at MediaEval 2021")

argument_parser.add_argument("-i", "--input-path", type=str, default=None)
argument_parser.add_argument("-o", "--output-path", type=str, default=None)

infiles = """D:\\DataSets\\EmotionalMario21\\truth\\participant_2_events.json
D:\\DataSets\\EmotionalMario21\\truth\\participant_4_events.json
D:\\DataSets\\EmotionalMario21\\truth\\participant_7_events.json"""

event_types = ["new_stage", "flag_reached", "status_up", "status_down", "life_lost"]

def convert(input_path, output_path):
    f1 = open(input_path)
    lines = f1.readlines()
    out = []
    for line in lines:
        s = line.split(';')
        out.append({"frame_number": int(s[0]), "event": s[1].strip()})

    # write them to out file
    with open(output_path, 'w') as out_file:
        json.dump(out, out_file)

def replace_last(string, find, replace):
    reversed = string[::-1]
    replaced = reversed.replace(find[::-1], replace[::-1], 1)
    return replaced[::-1]


def create_run(input_path, runid="run01"):
    f1 = open(input_path)
    truth = json.load(f1)
    # find maximum frame number and number of events
    maxframe = 0
    for truth_evt in truth:
        if truth_evt['frame_number'] > maxframe:
            maxframe = truth_evt['frame_number']
    # print(maxframe, len(truth))
    out = []
    number_of_events = len(truth) + random.randint(int(-len(truth)/2), int(len(truth)/2))
    for i in range(number_of_events):
        print(random.randint(0, maxframe + 100))
        out.append({"frame_number": random.randint(0, maxframe + 100), "event": event_types[random.randint(0, len(event_types)-1)]})
    # write to file: input_path.split('\\')[-1].replace("events", "run1")

    with open(input_path.split('\\')[-1].replace("events", runid), 'w') as out_file:
        json.dump(out, out_file)

if __name__ == '__main__':

    for input_path in infiles.split('\n'):
        create_run(input_path, "run04")
