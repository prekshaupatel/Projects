import matplotlib.pyplot as plt
import numpy as np

frac = 0.00001
max_time = 0
init_pop = -1
time = 0
growth_rates = list()
time_interval = 0

def main():
    K = 1
    r = 0
    x = ''
    cnt = 0

    while True:
        try:
            x = input('Enter per capita growth rate = ')
            r = float(x) 
            assert(r >= 0)
            assert (r <= 1)
            growth_rates.append(r)
            cnt = cnt + 1
        except:
            if x == '':
                break
            print('Invalid Arguments. per capita growth rate must be in the range (0, 1]')

    for i in range(cnt):
        max_time_sigmoidal(i)

    global max_time, time, time_interval
    time_interval = max_time/1000
    time = np.arange(0, max_time, time_interval)
    
    for i in range(cnt):
        plot_sigmoidal_growth(i)

    plt.xlabel('Time (yrs)')
    plt.ylabel('Population Size (%)')
    plt.title('Sigmoid Population Growth')
    plt.legend()
    plt.show()            



def plot_sigmoidal_growth(index):
    
    K = 1
    r = growth_rates[index]
    
    label_plot = 'per capita growth rate = %.3f' % r 

    population_size = list()
    
    for i in time:
        population_size.append(next_N(init_pop, K, r, i))

    plt.plot(time, population_size, label = label_plot)



def max_time_sigmoidal(index):
    
    global init_pop, max_time
    
    K = 1
    r = growth_rates[index]
    N_0 = frac * K
    N_t = (1-frac) * K

    if N_0 < init_pop or init_pop == -1:
        init_pop = N_0

    term_t = (K/N_t) - 1
    term_0 = (K/N_0) - 1
    t = np.log(term_t/term_0) / -r
    if t > max_time:
        max_time = t

    
    
def next_N(N_0, K, r, t):
    temp_1 = ((K/N_0)-1) * np.exp(-r*t)
    N_t = K/(1+temp_1)
    return N_t



main()
