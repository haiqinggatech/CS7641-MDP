import matplotlib.pyplot as plt
import pandas

def plot_learning_curve(input1, input2, input3, title):
#     _, _, test_scores_base = base_curve

    plt.figure()
    plt.title(title)
    plt.ylim((0, 3))
    
    # if datasetNum == 1:
    plt.xlim((0,250))

    plt.xlabel("# Iterations")
    plt.ylabel("Time")
    
    plt.grid()
    plt.plot(input1['iter'], input1['time'],  color="r",
             label="Value Iterations")
#     plt.plot(train_sizes, test_scores_base_mean, 'o-', color="b",
#              label="Test Score without CV")
    plt.plot(input2['iter'], input2['time'],  color="g",
             label="Policy Iterations")
    plt.plot(input3['iter'], input3['time'],  color="b",label="Q-Learning")

    plt.legend(loc="best")
    return plt


def plot_mse(input1, input2, input3, title):
#     _, _, test_scores_base = base_curve

    plt.figure()
    plt.title(title)
    # plt.ylim((-2000, 200))
    
    # if datasetNum == 1:
    plt.xlim((0,250))

    plt.xlabel("# Iterations")
    plt.ylabel("Rewards")
    
    plt.grid()
    plt.plot(input1['iter'], input1['reward'],  color="r",
             label="Value Iterations")
#     plt.plot(train_sizes, test_scores_base_mean, 'o-', color="b",
#              label="Test Score without CV")
    plt.plot(input2['iter'], input2['reward'],  color="g",
             label="Policy Iterations")
    plt.plot(input3['iter'], input3['reward'],  color="b",label="Q-Learning")

    plt.legend(loc="best")
    return plt









def plot_timing_curve(input1, input2, input3, title):
#     _, _, test_scores_base = base_curve

    plt.figure()
    plt.title(title)
    # plt.ylim((-2000, 200))
    
    # if datasetNum == 1:
    plt.xlim((0,250))

    plt.xlabel("# Iterations")
    plt.ylabel("Steps")
    
    plt.grid()
    plt.plot(input1['iter'], input1['steps'],  color="r",
             label="Value Iterations")
#     plt.plot(train_sizes, test_scores_base_mean, 'o-', color="b",
#              label="Test Score without CV")
    plt.plot(input2['iter'], input2['steps'],  color="g",
             label="Policy Iterations")
    plt.plot(input3['iter'], input3['steps'],  color="b",label="Q-Learning")

    plt.legend(loc="best")
    return plt


def plot_converge(input1, input2, input3, title):
#     _, _, test_scores_base = base_curve

    plt.figure()
    plt.title(title)
    # plt.ylim((-2000, 200))
    
    # if datasetNum == 1:
    plt.xlim((0,250))

    plt.xlabel("# Iterations")
    plt.ylabel("Convergence")
    
    plt.grid()
    plt.plot(input1['iter'], input1['convergence'],  color="r",
             label="Value Iterations")
#     plt.plot(train_sizes, test_scores_base_mean, 'o-', color="b",
#              label="Test Score without CV")
    plt.plot(input2['iter'], input2['convergence'],  color="g",
             label="Policy Iterations")
    plt.plot(input3['iter'], input3['convergence'],  color="b",label="Q-Learning")

    plt.legend(loc="best")
    return plt



df_value= pandas.read_csv('Easy Value.csv')
df_policy= pandas.read_csv('Easy Policy.csv')
df_Q = pandas.read_csv('Easy Q-Learning L0.1 q0.0 E0.5.csv')

title  = 'Easy Problem Time by Algorithm'
plot = plot_learning_curve(df_value, df_policy, df_Q, title)
plot.savefig(title+ '.png')
plot.close()


title  = 'Easy Problem Reward by Algorithm'
plot = plot_mse(df_value, df_policy, df_Q, title)
plot.savefig(title+ '.png')
plot.close()

title  = 'Easy Problem Steps by Algorithm'
plot = plot_timing_curve(df_value, df_policy, df_Q, title)
plot.savefig(title+ '.png')
plot.close()


title  = 'Easy Problem Convergence by Algorithm'
plot = plot_converge(df_value, df_policy, df_Q, title)
plot.savefig(title+ '.png')
plot.close()

