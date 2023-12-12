import matplotlib.pyplot as plt
import numpy as np

def manchester_to_ask(M): 
    Fe = 44100                            
    Fp = 2000                            

    baud = 300                            
    Nbits = len(M)                            
    Ns = int(Fe/baud)                              
    N = int(Nbits * Ns)    

    M_duplique= np.repeat(M, Ns)                     
                                        
    t= np.linspace(0,N/Fe, N)                      

    Ap= 1                                           
    Fp= 2000                                         
    Porteuse = Ap*np.sin(2*np.pi*Fp*t)               

    ASK = M_duplique*Porteuse

    plt.figure (figsize = (10,6))
    plt.plot(t,M_duplique,'red')
    plt.title('Message binaire')
    plt.xlabel('temps (s)')
    plt.ylabel('Amplitude')
    plt.grid()
    # plt.show()

    #Affichage de la porteuse 
        
    plt.figure (figsize = (10,6))
    plt.plot(t,Porteuse,'green')
    plt.title('Onde Porteuse')
    plt.xlabel('temps (s)')
    plt.ylabel('Amplitude')
    plt.grid()
    # plt.show()
    #Affichage du résultat de la modulmation ASK
        
    plt.figure (figsize = (10,6))
    plt.plot(t,ASK,'b')
    plt.title('Résultat ASK')
    plt.xlabel('temps (s)')
    plt.ylabel('Amplitude')
    plt.grid()
    # plt.show()
    return M

def ask_to_manchester(M):
    Fe = 44100                            
    Fp = 2000                            

    baud = 300                            
    Nbits = len(M)                            
    Ns = int(Fe/baud)                              
    N = int(Nbits * Ns)    

    M_duplique= np.repeat(M, Ns)                     
                                        
    t= np.linspace(0,N/Fe, N)                      

    Ap= 1                                           
    Fp= 2000                                         
    Porteuse = Ap*np.sin(2*np.pi*Fp*t)               

    ASK = M_duplique*Porteuse

    Produit= ASK*Porteuse

    Res = []                        

    for i in range(0,N,Ns):
        Res.append(np.trapz(Produit[i:i+Ns]))
                    
    message_demodule_ASK= []

    for ii in range (0,len(Res)):
        
        if Res[ii] > 0:
            message_demodule_ASK.extend([int(1)])
                
        if Res[ii] <= 0:
            message_demodule_ASK.extend([int(0)])

    Erreur = (np.array(M)==np.array(message_demodule_ASK))

    for i in range(len(Erreur)):
        if Erreur[i] == False:
            return f"Une erreur est survenue lors de la reception : {Erreur}"

    return M