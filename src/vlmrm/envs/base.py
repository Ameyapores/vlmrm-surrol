from typing import Callable

import gym


def get_clip_rewarded_env_name(env_name: str) -> str:
    return "vlmrm/CLIPRewarded" + env_name


RENDER_DIM = {
    "CartPole-v1": (400, 600),
    "MountainCarContinuous-v0": (400, 600),
    "Humanoid-v4": (480, 480),
    "NeedlePick-v0": (480, 640),
}


def get_make_env(
    env_name: str,
    *,
    render_mode: str = "rgb_array",
    **kwargs,
) -> Callable:
    def make_env_wrapper() -> gym.Env:
        env: gym.Env
        env = gym.make(
            env_name,
            render_mode=render_mode,
            **kwargs,
        )
        return env

    return make_env_wrapper


def is_3d_env(env_name: str) -> bool:
    return env_name == "Humanoid-v4"
