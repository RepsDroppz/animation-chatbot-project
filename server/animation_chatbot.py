from transformers import pipeline
import tensorflow as tf
import numpy as np
from moviepy.editor import TextClip, CompositeVideoClip
import base64

class AnimationChatbot:
    def __init__(self):
        self.nlp_processor = pipeline("text-generation", model="gpt-2")

    def create_animation_from_text(self, text):
        generated_text = self.nlp_processor(text, max_length=50)[0]['generated_text']
        
        # Create a simple text animation
        clip = TextClip(generated_text, fontsize=70, color='white')
        clip = clip.set_duration(10).set_position('center').on_color(color=(0, 0, 0), col_opacity=1)
        
        # Generate the animation video
        animation = CompositeVideoClip([clip])
        animation_file = "/tmp/animation.mp4"
        animation.write_videofile(animation_file, fps=24)

        with open(animation_file, "rb") as video_file:
            video_base64 = base64.b64encode(video_file.read()).decode('utf-8')

        return f"data:video/mp4;base64,{video_base64}"
