from replay_buffer import ReplayBuffer
from actor import Actor
from learner import Learner

if __name__ == '__main__':
    config = {
        'replay_buffer_size': 50000,
        'replay_buffer_episode': 400,
        'model_pool_size': 20,
        'model_pool_name': 'model-pool',
        'num_actors': 4,
        'episodes_per_actor': 20000,
        'gamma': 0.98,
        'lambda': 0.95,
        'min_sample': 200,
        'batch_size': 256,
        'epochs': 5,
        'clip': 0.2,
        'lr': 3e-5,
        'value_coeff': 1,
        'entropy_coeff': 0.01,
        'kl_coeff': 0.5,
        'kl_target': 0.01,
        'device': 'cuda',
        'ckpt_save_interval': 1000,
        'ckpt_save_path': 'checkpoint-pnt2/'
    }
    
    replay_buffer = ReplayBuffer(config['replay_buffer_size'], config['replay_buffer_episode'])
    
    actors = []
    for i in range(config['num_actors']):
        config['name'] = 'Actor-%d' % i
        actor = Actor(config, replay_buffer)
        actors.append(actor)
    learner = Learner(config, replay_buffer)
    
    for actor in actors: actor.start()
    learner.start()
    
    for actor in actors: actor.join()
    learner.terminate()