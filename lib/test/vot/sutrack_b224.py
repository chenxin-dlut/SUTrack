import os
import sys
env_path = os.path.join(os.path.dirname(__file__), '../../..')
if env_path not in sys.path:
    sys.path.append(env_path)
from lib.test.vot.sutrack_class import run_vot_exp

run_vot_exp('sutrack', 'sutrack_b224', vis=False, out_conf=True, channel_type='rgbd')