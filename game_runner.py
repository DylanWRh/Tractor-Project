import subprocess
import json

i = 0

# 初始化玩家
bot_models = {
    0: './checkpoint-base/model_3284.pt',
    1: './checkpoint-base/model_3284.pt',
    2: './checkpoint-base/model_3284.pt',
    3: './checkpoint-base/model_3284.pt',
}
bot_logs = {
    0: {
        "requests": [],
        "responses": []
    },
    1: {
        "requests": [],
        "responses": []
    },
    2: {
        "requests": [],
        "responses": []
    },
    3: {
        "requests": [],
        "responses": []
    },
}

# 初始化对局
judge_log = {
    "log": [],
    "initdata": {
        "seed": "969877809"
    }
}
judge_output = subprocess.run(
    ['python', 'judge_step.py', json.dumps(judge_log)], 
    stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True).stdout
judge_output = json.loads(judge_output)
judge_log.update({
    "initdata": judge_output["initdata"]
})

# 发牌
while True:
    print(f'Round {i}')
    i += 1

    # 通过judge_output判断该给哪位玩家发牌并更新玩家输入
    cur_bot = list(judge_output['content'].keys())[0]
    bot_logs[int(cur_bot)]['requests'].append(
        judge_output['content'][str(cur_bot)]
    )
    # 玩家接受发牌
    bot_output = subprocess.run(
        ['python', 'bot_step.py', json.dumps(bot_logs[int(cur_bot)]), bot_models[int(cur_bot)]],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True).stdout
    bot_output = json.loads(bot_output)

    # 更新玩家输入
    bot_logs[int(cur_bot)]["responses"].append(
        bot_output["response"]
    )
    # 更新裁判输入
    judge_log['log'].append({
        "keep_running": False,
		"memory": 242,
        "output": {
            'command': judge_output['command'],
            'content': judge_output['content'],
            'display': judge_output['display'],
        },
        "time": 175,
		"verdict": "OK"
    })
    judge_log['log'].append({
        cur_bot: {
            "keep_running": False,
			"memory": 326,
			"time": 1046,
			"verdict": "OK",
            "response": bot_output["response"]
        }
    })
    # 裁判准备给下一个玩家发牌
    judge_output = subprocess.run(
        ['python', 'judge_step.py', json.dumps(judge_log)], 
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True).stdout
    judge_output = json.loads(judge_output)
    # 结束发牌
    if judge_output['display']['event']['action'] != 'deal':
        break

# 完成发牌
judge_output = subprocess.run(
    ['python', 'judge_step.py', json.dumps(judge_log)], 
    stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True).stdout
judge_output = json.loads(judge_output)

# 开始出牌
while True:
    print(f'Round {i}')
    i += 1

    # 通过裁判输出判断该哪位玩家出牌并更新玩家输入
    cur_bot = list(judge_output['content'].keys())[0]
    bot_logs[int(cur_bot)]['requests'].append(
        judge_output['content'][str(cur_bot)]
    )

    # 玩家出牌
    bot_output = subprocess.run(
        ['python', 'bot_step.py', json.dumps(bot_logs[int(cur_bot)]), bot_models[int(cur_bot)]],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True).stdout
    bot_output = json.loads(bot_output)
    # 更新玩家输入
    bot_logs[int(cur_bot)]["responses"].append(
        bot_output["response"]
    )
    # 更新裁判输入
    judge_log['log'].append({
        "keep_running": False,
		"memory": 242,
        "output": {
            'command': judge_output['command'],
            'content': judge_output['content'],
            'display': judge_output['display'],
        },
        "time": 175,
		"verdict": "OK"
    })
    judge_log['log'].append({
        cur_bot: {
            "keep_running": False,
			"memory": 333,
			"time": 768,
			"verdict": "OK",
			"response": bot_output["response"]
        }
    })
    # 裁判准备让下一个玩家出牌
    judge_output = subprocess.run(
        ['python', 'judge_step.py', json.dumps(judge_log)], 
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True).stdout
    judge_output = json.loads(judge_output)
    if judge_output['command'] == 'finish':
        break

print('Score', judge_output['score'])

