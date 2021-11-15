import json
import argparse

argument_parser = argparse.ArgumentParser(description="The evaluation script for the Emotional Mario Task at MediaEval 2021")

argument_parser.add_argument("-i", "--input-path", type=str, default=None)
argument_parser.add_argument("-o", "--output-path", type=str, default=None)

infiles = """D:\\DataSets\\EmotionalMario21\\runs\\team_dcu\\participant_2.csv
D:\\DataSets\\EmotionalMario21\\runs\\team_dcu\\participant_4.csv
D:\\DataSets\\EmotionalMario21\\runs\\team_dcu\\participant_7.csv"""

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

if __name__ == '__main__':
    args = argument_parser.parse_args()

    input_path = args.input_path
    output_path = args.output_path

    for input_path in infiles.split('\n'):
        output_path = replace_last(input_path, ".csv", ".json")
        convert(input_path, output_path)
