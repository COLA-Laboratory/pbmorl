import argparse

def get_parser():
    parser = argparse.ArgumentParser(description='RL')

    # MORL parameters
    parser.add_argument('--env-name',
        default='MO-Swimmer-v2',
        help='environment to train on')
    parser.add_argument('--obj-num',
        type=int,
        default=2,
        help='number of objectives')
    parser.add_argument('--preference-setting',
                        default=[1.0,0.0],
                        help='preference setting')
    parser.add_argument('--interaction-num',
                        type=int,
                        default=40,
                        help='number of interaction with the DM')
    parser.add_argument('--population-ratio',
                        type=int,
                        default=0.2,
                        help='ratio of population construction')
    parser.add_argument(
        '--num-env-steps',
        type=int,
        default=5e7,
        help='number of environment steps to train (default: 5e6)')
    parser.add_argument('--num-tasks',
        type=int,
        help='number of rl task in each epoch')
    parser.add_argument('--seed', 
        type=int, 
        default=0, 
        help='random seed (default: 1)')
    parser.add_argument('--min-weight',
        type=float,
        default=0.0,
        help='minimum of weight range')
    parser.add_argument('--max-weight',
        type=float,
        default=1.0,
        help='maximum of weight range')
    parser.add_argument('--delta-weight',
        type=float,
        default=0.2,
        help='granularity of weight combinations in warm-up stage')
    parser.add_argument('--warmup-iter',
        type=int,
        default=100,
        help='number of RL iterations to run for warm up')
    parser.add_argument('--update-iter',
        type=int, 
        default=10,
        help='number of RL iterations between evolutionary processes')
    parser.add_argument('--eval-num',
        type=int,
        default=1,
        help='number of fitness evaluation times')
    parser.add_argument('--pbuffer-num',
        type=int,
        default=100,
        help='number of performance buffers')
    parser.add_argument('--pbuffer-size',
        type=int,
        default=2,
        help='size of each performance buffer')
    parser.add_argument('--obj-rms',
                        default=False,
                        action='store_true',
                        help='if use running mean std on objectives')
    parser.add_argument('--ob-rms',
                        default=False,
                        action='store_true',
                        help='if use running mean std on observations')
    parser.add_argument('--raw',
        default=False,
        action='store_true',
        help='use undiscounted evaluation')
    parser.add_argument(
        '--save-dir',
        default='./trained_models/',
        help='directory to save agent logs (default: ./trained_models/)')

    # PPO parameters
    parser.add_argument(
        '--algo', default='ppo')
    parser.add_argument(
        '--lr', type=float, default=3e-4, help='learning rate (default: 3e-4)')
    parser.add_argument(
        '--use-linear-lr-decay',
        action='store_true',
        default=False,
        help='use a linear schedule on the learning rate')
    parser.add_argument('--lr-decay-ratio',
        type=float,
        default=1.0,
        help='ratio of lr decay from beginning to the end (e.g., 1.0 means lr finally decays to 0, 0.0 means lr stays constant)')
    parser.add_argument(
        '--gamma',
        type=float,
        default=0.995,
        help='discount factor for rewards (default: 0.995)')
    parser.add_argument(
        '--use-gae',
        action='store_true',
        default=False,
        help='use generalized advantage estimation')
    parser.add_argument(
        '--gae-lambda',
        type=float,
        default=0.95,
        help='gae lambda parameter (default: 0.95)')
    parser.add_argument(
        '--entropy-coef',
        type=float,
        default=0.0,
        help='entropy term coefficient (default: 0.01)')
    parser.add_argument(
        '--value-loss-coef',
        type=float,
        default=0.5,
        help='value loss coefficient (default: 0.5)')
    parser.add_argument(
        '--max-grad-norm',
        type=float,
        default=0.5,
        help='max norm of gradients (default: 0.5)')
    parser.add_argument(
        '--num-steps',
        type=int,
        default=2048,
        help='timesteps per epoch.')
    parser.add_argument(
        '--num-processes',
        type=int,
        default=1,
        help='how many training CPU processes to use (default: 4)')
    parser.add_argument(
        '--ppo-epoch',
        type=int,
        default=10,
        help='number of ppo epochs (default: 10)')
    parser.add_argument(
        '--num-mini-batch',
        type=int,
        default=32,
        help='number of batches for ppo (default: 32)')
    parser.add_argument(
        '--clip-param',
        type=float,
        default=0.15,
        help='ppo clip parameter (default: 0.2)') 
    parser.add_argument(
        '--use-proper-time-limits',
        action='store_true',
        default=False,
        help='compute returns taking into account time limits')
    parser.add_argument(
        '--layernorm', 
        action='store_true',
        default=False,
        help='if use layernorm')

    return parser
