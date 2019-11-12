from pylab import rand,plot,show,norm

class Perceptron:
    def __init__(self):
        """ inicializacao do perception """
        self.w = rand(2)*2-1 # pesos
        self.learningRate = 0.1

    def response(self,x):
        """ saida do perception """
        y = x[0]*self.w[0]+x[1]*self.w[1] # produto escalar de pesos e x
        if y >= 0:
            return 1
        else:
            return -1

    def updateWeights(self,x,iterError):
        self.w[0] += self.learningRate*iterError*x[0]
        self.w[1] += self.learningRate*iterError*x[1]

    def train(self,data):
        learned = False
        iteration = 0
        while not learned:
            globalError = 0.0
            for x in data: 
                r = self.response(x)    
                if x[2] != r: 
                    iterError = x[2] - r 
                    self.updateWeights(x,iterError)
                    globalError += abs(iterError)
                iteration += 1
                if globalError == 0.0 or iteration >= 1000: 
                    print ('iterations ', iteration)
                    learned = True





def generateData(n):
    xb = (rand(n)*2-1)/2-0.5
    yb = (rand(n)*2-1)/2+0.5
    xr = (rand(n)*2-1)/2+0.5
    yr = (rand(n)*2-1)/2-0.5
    inputs = []
    for i in range(len(xb)):
        inputs.append([xb[i],yb[i],1])
        inputs.append([xr[i],yr[i],-1])
    return inputs



trainset = generateData(40) 
perceptron = Perceptron()  
perceptron.train(trainset)  
dataPlot = generateData(20) 

print(dataPlot)


for x in dataPlot:
    r = perceptron.response(x)
    if r == 1:
        plot(x[0],x[1],'ob')  
    else:
        plot(x[0],x[1],'xr')

n = norm(perceptron.w)
ww = perceptron.w/n
ww1 = [ww[1],-ww[0]]
ww2 = [-ww[1],ww[0]]
plot([ww1[0], ww2[0]],[ww1[1], ww2[1]],'-')
show()