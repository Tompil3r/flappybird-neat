from neat import Neat
from neat.callbacks import TimeTermination, GenerationTermination
from flappybird import FlappyBirdEnv


population = 1

env = FlappyBirdEnv(population)
neat = Neat(env.bird_state_len, 1, population, init_population=False)

genome = neat.load_genome('genome.gnc')

callbacks = [
    TimeTermination(0, 10, 0),
    GenerationTermination(1)
]

neat.test_env(env, genomes=[genome], callbacks=callbacks, verbose=1, visualize=True)