# Tractor-Project

Term project for the course **An Introduction to Multi-Agent Systems**, Peking University, 24 Spring

RL-based AI for [Trackter game on Botzone](https://www.botzone.org.cn/game/Tractor)

## Files

- `__main__.py`, `utils.py`, `mvGen.py`, `wrapper.py`, `model.py`: the interface for Botzone, modfied from the original HW framework
- `actor.py`, `env.py`, `learner.py`, `model_pool.py`, `model.py`, `train.py`, `replay_buffer.py`: environment for local model training, modfied from the original HW framework
- `batch_run.sh`, `bot_step.py`, `judge_step.py`, `game_runner.py`: support local game running for convenient ablation study, added by myself

## Usage

Run the following script to train a model
```bash
python train.py
```

Run the following script to run local game, the args in `bash_run.sh` should be changed to your trained model paths
```bash
./bash_run.sh
```