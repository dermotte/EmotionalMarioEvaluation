# Emotional Mario - Training Data Ground Truth
The ground truth has been generated for each of the 10 participants, but 3 out of 10 have been selected for the final runs, so only 7 are released for training. Selection of the training data has been done using the random number generator at https://www.random.org/integers/. Find more information on EmotionalMario https://multimediaeval.github.io/editions/2021/tasks/emotionalmario/. Find the Toadstool data set, to which this event data is referring at https://github.com/simula/toadstool


## Data Format
The JSON file contains a JSON list of events, with each event having an event name and a frame_number of the gameplay videos.

    [
        {"event": "status_up", "frame_number": 812},
        {"event": "flag_reached", "frame_number": 4229},
        {"event": "new_stage", "frame_number": 4230},
        {"event": "status_up", "frame_number": 4719},
        {"event": "status_down", "frame_number": 5849},
        ...
    ]

Available events are

* `new_stage` .. at the very beginning of a new stage, except the first one, which starts at frame_number 1
* `flag_reached` .. when the flag, i.e. the level end is reached.
* `status_up` .. when a mushroom or flower (power up) is consumed by the player.
* `status_down` .. when a player encounters a monster and looses a power up.
* `life_lost` .. when a player looses one of Mario's lifes, note that the game is in endless mode.

## Installation Guide for the Toadstool Data for Windows
Make sure you’ve got Python 3.8 installed (3.9 does not work with the required version of Pillow)

Download and install "Microsoft C++ Build Tools": https://visualstudio.microsoft.com/visual-cpp-build-tools/ for the nes_py package

Use e.g. Pycharm on Windows to create a project with a new virtualenv.

Install gym-super-mario-bros: https://github.com/Kautenja/gym-super-mario-bros

     $> pip install gym-super-mario-bros

Install OpenCV

    $> pip install opencv-python
