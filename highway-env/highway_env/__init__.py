# Import the envs module so that envs register themselves
import highway_env.envs
from gym.envs.registration import register

# register(
#     id='highway-v0',                                   # Format should be xxx-v0, xxx-v1....
#     entry_point='highway_env.envs:highway_env',
#     max_episode_steps=2000,
#     reward_threshold=0.0,
#     nondeterministic=True,
# )

# register(
#     id='highway-v3',                                   # Format should be xxx-v0, xxx-v1....
#     entry_point='highway_env.envs:highway_env3',
#     max_episode_steps=2000,
#     reward_threshold=0.0,
#     nondeterministic=True,
# )

# register(
#     id='highway-v5',                                   # Format should be xxx-v0, xxx-v1....
#     entry_point='highway_env.envs:highway_env5',
#     max_episode_steps=2000,
#     reward_threshold=0.0,
#     nondeterministic=True,
# )

