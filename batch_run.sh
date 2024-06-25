#!/bin/bash

# for i in $(seq 0 25); do
#     python -u game_runner.py --model1 './checkpoint-base/model_3284.pt' \
#                              --model2 './checkpoint-pnt/model_2898.pt' \
#                              --model3 './checkpoint-base/model_3284.pt' \
#                              --model4 './checkpoint-pnt/model_2898.pt' >> clp1-pnt1.out
#     python -u game_runner.py --model2 './checkpoint-base/model_3284.pt' \
#                              --model3 './checkpoint-pnt/model_2898.pt' \
#                              --model4 './checkpoint-base/model_3284.pt' \
#                              --model1 './checkpoint-pnt/model_2898.pt' >> pnt1-clp1.out

#     python -u game_runner.py --model1 './checkpoint-base/model_3284.pt' \
#                              --model2 './checkpoint-pnt/model_28456.pt' \
#                              --model3 './checkpoint-base/model_3284.pt' \
#                              --model4 './checkpoint-pnt/model_28456.pt' >> clp1-pnt10.out
#     python -u game_runner.py --model2 './checkpoint-base/model_3284.pt' \
#                              --model3 './checkpoint-pnt/model_28456.pt' \
#                              --model4 './checkpoint-base/model_3284.pt' \
#                              --model1 './checkpoint-pnt/model_28456.pt' >> pnt10-clp1.out

#     python -u game_runner.py --model1 './checkpoint-base/model_28864.pt' \
#                              --model2 './checkpoint-pnt/model_28456.pt' \
#                              --model3 './checkpoint-base/model_28864.pt' \
#                              --model4 './checkpoint-pnt/model_28456.pt' >> clp10-pnt10.out
#     python -u game_runner.py --model2 './checkpoint-base/model_28864.pt' \
#                              --model3 './checkpoint-pnt/model_28456.pt' \
#                              --model4 './checkpoint-base/model_28864.pt' \
#                              --model1 './checkpoint-pnt/model_28456.pt' >> pnt10-clp10.out

#     python -u game_runner.py --model1 './checkpoint-base/model_28864.pt' \
#                              --model2 './checkpoint-pnt/model_2898.pt' \
#                              --model3 './checkpoint-base/model_28864.pt' \
#                              --model4 './checkpoint-pnt/model_2898.pt' >> clp10-pnt1.out
#     python -u game_runner.py --model2 './checkpoint-base/model_28864.pt' \
#                              --model3 './checkpoint-pnt/model_2898.pt' \
#                              --model4 './checkpoint-base/model_28864.pt' \
#                              --model1 './checkpoint-pnt/model_2898.pt' >> pnt1-clp10.out
    
#     python -u game_runner.py --model1 './checkpoint-base/model_3284.pt' \
#                              --model2 './checkpoint-base/model_28864.pt' \
#                              --model3 './checkpoint-base/model_3284.pt' \
#                              --model4 './checkpoint-base/model_28864.pt' >> clp1-clp10.out
#     python -u game_runner.py --model2 './checkpoint-base/model_3284.pt' \
#                              --model3 './checkpoint-base/model_28864.pt' \
#                              --model4 './checkpoint-base/model_3284.pt' \
#                              --model1 './checkpoint-base/model_28864.pt' >> clp10-clp1.out
    
#     python -u game_runner.py --model1 './checkpoint-pnt/model_2898.pt' \
#                              --model2 './checkpoint-pnt/model_28456.pt' \
#                              --model3 './checkpoint-pnt/model_2898.pt' \
#                              --model4 './checkpoint-pnt/model_28456.pt' >> pnt1-pnt10.out
#     python -u game_runner.py --model2 './checkpoint-pnt/model_2898.pt' \
#                              --model3 './checkpoint-pnt/model_28456.pt' \
#                              --model4 './checkpoint-pnt/model_2898.pt' \
#                              --model1 './checkpoint-pnt/model_28456.pt' >> pnt10-pnt1.out
# done

for i in $(seq 0 10); do
    python -u game_runner.py --model1 './checkpoint-base/model_62860.pt' \
                             --model2 './checkpoint-pnt/model_62301.pt' \
                             --model3 './checkpoint-base/model_62860.pt' \
                             --model4 './checkpoint-pnt/model_62301.pt' >> clpmax-pntmax.out
    python -u game_runner.py --model2 './checkpoint-base/model_62860.pt' \
                             --model3 './checkpoint-pnt/model_62301.pt' \
                             --model4 './checkpoint-base/model_62860.pt' \
                             --model1 './checkpoint-pnt/model_62301.pt' >> pntmax-clpmax.out 
    
    python -u game_runner.py --model1 './checkpoint-pnt/model_28456.pt' \
                             --model2 './checkpoint-pnt/model_62301.pt' \
                             --model3 './checkpoint-pnt/model_28456.pt' \
                             --model4 './checkpoint-pnt/model_62301.pt' >> pnt10-pntmax.out
    python -u game_runner.py --model2 './checkpoint-pnt/model_28456.pt' \
                             --model3 './checkpoint-pnt/model_62301.pt' \
                             --model4 './checkpoint-pnt/model_28456.pt' \
                             --model1 './checkpoint-pnt/model_62301.pt' >> pntmax-pnt10.out 
done 