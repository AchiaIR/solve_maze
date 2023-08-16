"""
A video display configuration.
"""
import os
import time
import base64
import imageio
import IPython
import subprocess
import numpy as np


def embed_mp4(filename):
  """Embeds an mp4 file"""
  video = open(filename,'rb').read()
  b64 = base64.b64encode(video)
  tag = '''
  <video width="640" height="480" controls>
    <source src="data:video/mp4;base64,{0}" type="video/mp4">
  Your browser does not support the video tag.
  </video>'''.format(b64.decode())

  return IPython.display.HTML(tag)


def DisplayVideo(algo, env, name, is_model_based, max_time=10):
  start_time = time.time()
  done = False
  state = env.reset()
  video_filename = name + '.mp4'
  with imageio.get_writer(video_filename, fps=10) as video:
    while not done:
      time_passed = int(time.time() - start_time)
      if done or time_passed > max_time:
        break
      if is_model_based:
        action = algo.π[tuple(np.int32(state))]
      else:
        action = np.argmax(algo.Q[tuple(np.int32(state))])
      state, reward, done, info = env.step(action)
      video.append_data(env.render(mode='rgb_array'))
  embed_mp4(video_filename)
  try:
    if os.name == 'nt':
        os.startfile(video_filename)  # Windows
    else:
        # Try xdg-open first
        try:
            subprocess.call(['xdg-open', video_filename])
        # Fallback to gio open
        except FileNotFoundError:
            subprocess.call(['gio', 'open', video_filename])
  except Exception as e:
    print("Error opening the video:", e)

