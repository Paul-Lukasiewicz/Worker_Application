import streamlit as st
from audio_processing import *



def vocal_capture():
    audio_value = st.audio_input("Enregistrez vous")
    if audio_value:
        print(type(audio_value))
        return audio_value
    
    
def main():
    st.title("Nouveau rapport")
    audio_file = vocal_capture()
    
    if audio_file is not None:
        transcript = transcribe_audio(audio_file)
        st.write("Transcription :", transcript)
    
if __name__ == "__main__":
    main()
