# import sys
# sys.path.append('../')
from neat import Neat
from neat.callbacks import GenomeSaving, TimeTermination, EnvStopper, FileLogger
from flappybird import FlappyBirdEnv


population = 200

env = FlappyBirdEnv(population)
neat = Neat(env.bird_state_len, 1, population)

callbacks = [
    GenomeSaving(population, best_only=True, filenames=['genome.gnc']),
    TimeTermination(0, 30, 0),
    EnvStopper(10_000, differentiate_genomes=True, use_scores=False, alive_fitness=10_000),
    FileLogger('log.csv', population, 5)
]

neat.fit_env(env, callbacks=callbacks, threads=1, verbose=1, visualize=False)
