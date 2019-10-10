import os
import subprocess
from time import time

import numpy as np


def on_sherlock():
    return 'GROUP_SCRATCH' in os.environ


def get_id(prefix="wgan", commit=True):
    rnd = int(time() * 1e8 % 1e8)
    if commit:
        out = subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD'])
        hash = out.strip().decode('ascii')
    else:
        hash = ''
    if on_sherlock():
        sid = os.environ['SLURM_JOB_ID']
        tid = os.environ['SLURM_LOCALID']
        jid = os.environ['SLURM_JOB_NAME']
        fname = f'{prefix}_{hash}_{jid}_{sid}_{tid}_{rnd}'
    else:
        fname = f'{prefix}_{hash}_{rnd}'
    return fname


def get_write_dir(file=None, project="wgan"):
    if file is None:
        file = "file"
    out_dirname = file.split('.')[0].split('/')[-1] + '_out/'
    if on_sherlock():
        out_dir = os.environ['GROUP_SCRATCH']
        write_path = os.path.join(out_dir, project, out_dirname)
    else:
        out_dir = os.path.abspath(os.path.dirname(file))
        write_path = os.path.join(out_dir, out_dirname)

    return write_path
