# %% Import libraries
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from classes import Sonifier, Grammar_Sequence, metronome_grammar

# %%
ex_i_grammar={
    "S":["M", "SM"],
    "M": [["H","H"], ["q", "h", "q"]],    
    "H": ["h", ["q","q"]],
    "Q": [["q"], ["o","o"]]
}

ex_i_word_dur={"h":0.5, # half-measure
              "q":0.25, # quarter-measure
              "o": 0.125,
}


if __name__=="__main__":
    fn_out="basic_composition.wav"

    NUM_M=8
    START_SEQUENCE=["M",]*NUM_M
    G=Grammar_Sequence(ex_i_grammar)        
        
    final_sequence, seqs=G.create_sequence(START_SEQUENCE)
    for seq in seqs:
        print(" ".join(seq))
    print(f"Final sequence: {' '.join(final_sequence)}")    
    
    S= Sonifier("sounds/cymb.wav", BPM=174, word_dur=ex_i_word_dur)
    audio_array=S.create_audio(final_sequence, add_metronome=True)
    S.write("out/"+fn_out, audio_sequence=audio_array)

# %%
