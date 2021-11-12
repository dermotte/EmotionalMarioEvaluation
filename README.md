# Emotional Mario 2021 - Evaluation
Find more information on https://multimediaeval.github.io/editions/2021/tasks/emotionalmario/

## Data Explained
The JSON file contains a JSON list of events, with each event having an event name and a frame_number.

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