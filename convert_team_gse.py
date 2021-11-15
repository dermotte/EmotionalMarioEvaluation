import json
import argparse

argument_parser = argparse.ArgumentParser(description="The evaluation script for the Emotional Mario Task at MediaEval 2021")

argument_parser.add_argument("-i", "--input-path", type=str, default=None)
argument_parser.add_argument("-o", "--output-path", type=str, default=None)

infiles = """/d/DataSets/EmotionalMario21/runs/team_gse/new0.5/participant2_Method1.json
/d/DataSets/EmotionalMario21/runs/team_gse/new0.5/participant2_Method2.json
/d/DataSets/EmotionalMario21/runs/team_gse/new0.5/participant4_Method1.json
/d/DataSets/EmotionalMario21/runs/team_gse/new0.5/participant4_Method2.json
/d/DataSets/EmotionalMario21/runs/team_gse/new0.5/participant7_Method1.json
/d/DataSets/EmotionalMario21/runs/team_gse/new0.5/participant7_Method2.json
/d/DataSets/EmotionalMario21/runs/team_gse/new0.7/participant2_Method1.json
/d/DataSets/EmotionalMario21/runs/team_gse/new0.7/participant2_Method2.json
/d/DataSets/EmotionalMario21/runs/team_gse/new0.7/participant4_Method1.json
/d/DataSets/EmotionalMario21/runs/team_gse/new0.7/participant4_Method2.json
/d/DataSets/EmotionalMario21/runs/team_gse/new0.7/participant7_Method1.json
/d/DataSets/EmotionalMario21/runs/team_gse/new0.7/participant7_Method2.json
/d/DataSets/EmotionalMario21/runs/team_gse/new0.9/participant2_Method2.json
/d/DataSets/EmotionalMario21/runs/team_gse/new0.9/participant4_Method2.json
/d/DataSets/EmotionalMario21/runs/team_gse/new0.9/participant7_Method2.json
"""

def convert(input_path, output_path):
    f1 = open(input_path)
    run = json.load(f1)
    print("hello world")

    out = []

    # convert all entries
    for key in run:
        # print(key, '->', run[key])
        out.append({"frame_number": int(key), "event": run[key]})

    # write them to out file
    with open(output_path, 'w') as out_file:
        json.dump(out, out_file)

def replace_last(string, find, replace):
    reversed = string[::-1]
    replaced = reversed.replace(find[::-1], replace[::-1], 1)
    return replaced[::-1]

if __name__ == '__main__':
    args = argument_parser.parse_args()

    input_path = args.input_path
    output_path = args.output_path

    for input_path in infiles.split('\n'):
        output_path = replace_last(input_path, ".csv", ".json")
        convert(input_path, output_path)
