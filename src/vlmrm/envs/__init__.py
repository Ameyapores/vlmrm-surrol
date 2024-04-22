import gym

from vlmrm.envs.base import *  # noqa F401
from vlmrm.envs.base import get_clip_rewarded_env_name

gym.register(
    id=get_clip_rewarded_env_name("MountainCarContinuous-v0"),
    entry_point="vlmrm.envs.classic_control.clip_rewarded_mountain_car_continuous:CLIPRewardedContinuousMountainCarEnv",  # noqa: E501
)

gym.register(
    id=get_clip_rewarded_env_name("CartPole-v1"),
    entry_point="vlmrm.envs.classic_control.clip_rewarded_cart_pole:CLIPRewardedCartPoleEnv",
)


gym.register(
    id=get_clip_rewarded_env_name("Humanoid-v4"),
    entry_point="vlmrm.envs.mujoco.clip_rewarded_humanoid:CLIPRewardedHumanoidEnv",
)

gym.register(
    id=get_clip_rewarded_env_name("NeedlePick-v0"),
    entry_point="vlmrm.envs.surrol.clip_rewarded_needlepick:CLIPRewardedNeedlePickEnv",
)
