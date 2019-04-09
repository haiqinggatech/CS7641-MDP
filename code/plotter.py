import matplotlib.pyplot as plt
import pandas

colors = ['r', 'b', 'g', 'k', 'm', 'c', 'y', '#eeefff', '.75', '.25']

OPTIMAL_Q_EASY = 'Easy Q-Learning L0.1 q0.0 E0.1.csv'
OPTIMAL_Q_HARD = 'Hard Q-Learning L0.1 q0.0 E0.1.csv'

def get_df(path, headerVal=0):
  return pandas.read_csv('../../results/' + path, header=headerVal)


def find_best_q_learning(difficulty):
  bestResults = list()

  for lr in [0.1,0.9]:
    for qInit in [-100,0,100]:
      for epsilon in [0.1,0.3,0.5]:
        params = 'L' + str(lr) + ' q' + str(qInit) + '.0 E' + str(epsilon)
        path = difficulty + '/' + difficulty.title() + ' Q-Learning ' + params + '.csv'
        # print(path)
        df = get_df(path)

        df = df.sort_values('iter', ascending=False)
        max_reward = df['reward'].idxmax()
        max_row = df.ix[max_reward]
        max_row['params'] = params
        bestResults.append(max_row)

  df = pandas.DataFrame(bestResults)
  df = df.sort_values('iter', ascending=False)
  df = df.sort_values('reward', ascending=False)
  print(df)

  count = 0
  for index, row in df.iterrows():
    count = count + 1
    if count > 10:
      continue

    sig = 4
    sigString = '{:0.' + str(sig) + 'f}'
    vals = map(lambda x: sigString.format(x).replace(".0000", ''), [ row['iter'], row['time'], row['reward'], row['steps'], row['convergence'] ])
    print('\\textbf{' + row['params'] + '} & ' + ' & '.join(vals) + ' \\\\ \\hline')


def print_value_results(difficulty, policy):
  path = difficulty + '/' + difficulty.title() + ' ' + policy + '.csv' 
  print(path)
  df = get_df(path)

  count = 0
  for index, row in df.iterrows():
    if count == 0 or (count + 1) % 5 == 0 or count + 1 == len(df):
      sig = 4
      sigString = '{:0.' + str(sig) + 'f}'
      vals = map(lambda x: sigString.format(x).replace(".0000", ''), [ row['iter'], row['time'], row['reward'], row['steps'], row['convergence'] ])
      print(' & '.join(vals) + ' \\\\ \\hline')

    count = count + 1
  print('')

def save_plot(plot, title):
    plot.savefig('../../results/vis/' + title.replace(' ', '_').replace('.', 'pt').lower() + '.jpg')

def get_main_dfs(difficulty):
  q_path = OPTIMAL_Q_EASY if difficulty == 'easy' else OPTIMAL_Q_HARD
  value_path = difficulty.title() + ' Value.csv'
  policy_path = difficulty.title() + ' Policy.csv'

  q_df = get_df(difficulty + '/' + q_path)
  value_df = get_df(difficulty + '/' + value_path)
  policy_df = get_df(difficulty + '/' + policy_path)

  return (q_df, value_df, policy_df)

def plot_convergence(difficulty):
  easy = difficulty == 'easy'
  q_df, value_df, policy_df = get_main_dfs(difficulty)


  plt.figure(figsize=(8,5))
  plt.title(difficulty.title() + ' Gridworld Convergence by Algorithm') 

  plt.xlabel('# Iterations')
  plt.ylabel('Convergence Delta')

  if easy:
    plt.ylim((0, 15))
    plt.xlim((0, 250))
  else:  
    plt.ylim((0, 15))
    plt.xlim((0, 250))
  
  plt.grid()

  plt.plot(q_df['iter'].values, q_df['convergence'].values, 'o-', color="b",
           label='Q-Learning Optimal')

  plt.plot(value_df['iter'].values, value_df['convergence'].values, 'o-', color="r",
           label='Value Iteration')

  plt.plot(policy_df['iter'].values, policy_df['convergence'].values, 'o-', color="g",
           label='Policy Iteration')
  
  plt.legend(loc="best")


def plot_time(difficulty):
  easy = difficulty == 'easy'
  q_df, value_df, policy_df = get_main_dfs(difficulty)


  plt.figure(figsize=(8,5))
  plt.title(difficulty.title() + ' Gridworld Time by Algorithm') 

  plt.xlabel('# Iterations')
  plt.ylabel('Time')

  if easy:
    plt.ylim((0, .45))
    plt.xlim((0, 250))
  else:  
    plt.ylim((0, 2.55))
    plt.xlim((0, 250))
  
  plt.grid()

  plt.plot(q_df['iter'].values, q_df['time'].values, 'o-', color="b",
           label='Q-Learning Optimal')

  plt.plot(value_df['iter'].values, value_df['time'].values, 'o-', color="r",
           label='Value Iteration')

  plt.plot(policy_df['iter'].values, policy_df['time'].values, 'o-', color="g",
           label='Policy Iteration')
  
  plt.legend(loc="best")


  save_plot(plt, difficulty + ' time')
  plt.close()


def plot_reward(difficulty):
  easy = difficulty == 'easy'
  q_df, value_df, policy_df = get_main_dfs(difficulty)


  plt.figure(figsize=(8,5))
  plt.title(difficulty.title() + ' Gridworld Reward by Algorithm') 

  plt.xlabel('# Iterations')
  plt.ylabel('Reward')

  if easy:
    plt.ylim((-30, 55))
    plt.xlim((0, 300))
  else:  
    plt.ylim((-350, 50))
    plt.xlim((0, 800))
  
  plt.grid()

  plt.plot(q_df['iter'].values, q_df['reward'].values, 'o-', color="b",
           label='Q-Learning Optimal')

  plt.plot(value_df['iter'].values, value_df['reward'].values, 'o-', color="r",
           label='Value Iteration')

  plt.plot(policy_df['iter'].values, policy_df['reward'].values, 'o-', color="g",
           label='Policy Iteration')
  
  plt.legend(loc="best")


  save_plot(plt, difficulty + ' reward')
  plt.close()



# find_best_q_learning('easy')
# print(' ')
# find_best_q_learning('hard')

# print_value_results('easy', 'Value')
# print_value_results('easy', 'Policy')

# print_value_results('hard', 'Value')
# print_value_results('hard', 'Policy')

plot_convergence('easy')
plot_convergence('hard')

plot_time('easy')
plot_time('hard')

plot_reward('easy')
plot_reward('hard')



