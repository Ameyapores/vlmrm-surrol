import pathlib
from typing import Any, Dict, Optional, Tuple

import numpy as np
from gym import utils
from gym.spaces import Box
from numpy.typing import NDArray
from .tasks.needle_pick import NeedlePick
import torch

import threading

from stable_baselines3.common.env_checker import check_env

class CLIPRewardedNeedlePickEnv(NeedlePick):
    def __init__(
        self,
        episode_length: int,
        render_mode: str = "rgb_array",
        **kwargs,
    ):
        super().__init__(render_mode)
        utils.EzPickle.__init__(
            self,
            render_mode=render_mode,
            **kwargs,
        )

        self.episode_length = episode_length
        self.num_steps = 0

        # Define the observation space
        self.observation_space = Box(low=-np.inf, high=np.inf, shape=(25,), dtype=np.float64)

    ### write the step function
    # def step(self, action) -> Tuple[NDArray, float, bool, bool, Dict]:
    def step(self, action) -> Tuple[NDArray, float, bool, Dict]:
        obs, reward, _, info = super().step(action)
        self.num_steps += 1
        # terminated = self.num_steps >= self.episode_length
        done = self.num_steps >= self.episode_length

        # Convert the observation dictionary to a single array
        # obs = np.concatenate([obs['observation'] , obs['desired_goal']])

        return (obs, reward, done, info)
        # return (
        #     obs,  # obs
        #     reward,
        #     terminated,
        #     truncated,
        #     info,
        # )


    # def step(self, action) -> Tuple[NDArray, float, bool, bool, Dict]:
    #     obs, reward, _, truncated, info = super().step(action)
    #     self.num_steps += 1
    #     terminated = self.num_steps >= self.episode_length
    #     # obs_new = np.concatenate([obs['observation'], obs['desired_goal']])
    #     return (
    #         obs_new,  # obs
    #         reward,
    #         terminated,
    #         truncated,
    #         info,
    #     )

    # def reset(self, *, seed: Optional[int] = None, options: Optional[Dict] = None):
    #     self.num_steps = 0
    #     return super().reset(seed=seed, options=options)

    # def reset(self, *, options: Optional[Dict] = None):
    #     self.num_steps = 0
    #     return super().reset(options=options)
    
    def reset(self):
        self.num_steps = 0
        return super().reset()
        # thread = threading.Thread(target=super().reset, args=())
        # thread.start()

# check_env(CLIPRewardedNeedlePickEnv(episode_length=200))