Author: MacKenzie K. Cooper (mkc@pdx.edu)
Project: Command Line Synth Generator

## RUNNING THE CODE
```python3 project```

For help using the flags:

 ```python3 project --help```

To run the example csv:

```python3 project -f project/csv_files/funky_town.csv```

## ABOUT THE CODE
The project began as a GUI pitch trainer that would output notes and the user would attempt to discern the pitch of that note. However, as I went through design the project, I got caught up in the sound synthesis portion of the project, specifically having to do with generating different kinds of chords and how they are composed and might be modified by octave or other means. Right now, the project is a command line synth generator that takes in a CSV file composed of lines that represent notes, their relative octave (relative to the core octave the tune takes), and the relative length of each of the notes (relative to whatever note length that might be input). It uses the `argparse` library, so supports the –help flag to help explain its capabilities. It can also output the series of different kinds of chords as an example run by default. 

The testing was mostly conducted by running and reviewing the code to see what sounded nice. In terms of what work, I was very pleased with the generalizability of much of the code, and I plan to make further use of it to create a more fully realized synthesizer. There is an attempt in the code to replicate a piano note wave form using a formula found on stack overflow ([see page here](https://dsp.stackexchange.com/questions/46598/mathematical-equation-for-the-sound-wave-that-a-piano-makes)), but this ended up sounding rather unpleasant and so is not part of the functional project as yet. Additionally, I made use of an article describing the various kinds of chords and how they are constructed to inform my design ([see page here](https://www.edmprod.com/different-chord-types/)). Finally, I found a website that gave the notes and their length in order to construct `funky_town.csv` and its shortened version ([see page here](https://www.hooktheory.com/theorytab/view/lipps-inc/funky-town)). 

Given more time, I would like to implement more of the different kinds of wave forms and maybe find some way to generate tunes programmatically, either from scratch or based off other music. In terms of what didn’t work: the GUI didn’t make it into the final project as I felt it added nothing substantial to what I was trying to make as yet, and the command line felt like a sufficient place for the project in its current stage. Additionally, I think it could be further generalized into libraries for generating various kinds of notes and handling errors at the lower levels of the program. In the future, I would like to explore testing much further to validate my outputs. In terms of what worked, I am pleased with the programs error handling and how generalizable the functions are already. Finally, I would like to make further attempts to synthesize real instruments. I had a ton of fun working on this project and became very familiar with many aspects of music. I came into this project with almost no understanding of the mathematical structure of sound, the different types of scales, or any music theory whatsoever, so I feel I have gained a significant amount of knowledge by working on it. 