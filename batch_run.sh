#!/bin/bash

# Loop from 0 to 99 (100 iterations)
for i in $(seq 0 99); do
    python -u game_runner.py --model1 './checkpoint-base/model_3284.pt' --model2 './checkpoint-base/model_3284.pt' --model3 './checkpoint-base/model_3284.pt' --model4 './checkpoint-base/model_3284.pt' >> batch_run_output
done
