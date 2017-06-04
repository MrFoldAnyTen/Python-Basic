import matplotlib.pyplot as plt

def go():
    x = [1,2,3,4,5,6,7,8,9]
    y = [5,7,8,8,9,10,10,11,12]

    x2 = [1,2,3,4,5,6,7,8,9]
    y2 = [8,9,12,13,15,17,18,18,17]


    plt.plot(x,y,label='nazis')
    plt.plot(x2,y2,label='alligators')
    plt.xlabel('Years')
    plt.ylabel('Incidents')
    plt.title('The EvidenceProvided\nyesterday')
    plt.legend()
    plt.show()
