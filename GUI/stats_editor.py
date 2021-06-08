

from tkinter import *

root = Tk()
root.title('Volleyball Statistics Input')

weekList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

titleLabel = Label(root, text="Volleyball Statistics Input", padx=10, pady=10)
weekLabel = Label(root, text="Week: 1 of "+ str(len(weekList)), padx=20, pady=10)


prevWeekButton = Button(root, text= "<<", command=lambda: prevWeek(0), padx=10, pady=10, anchor=W)
nextWeekButton = Button(root, text= ">>", command=lambda: nextWeek(2), padx=10, pady=10, anchor=W)

#Initializing Player Selection Buttons
playerSelection = LabelFrame(root, text="Player Selection", padx=10, pady=10)
brandonChan = Button(playerSelection, text="Chan", command=lambda:playerSelect("brandonChan"), height=4, width=15)
callumAshton = Button(playerSelection, text="Callum", command=lambda:playerSelect("callumAshton"), height=4, width=15)
danielPark = Button(playerSelection, text="Daniel", command=lambda:playerSelect("danielPark"), height=4, width=15)
deirdreTruong = Button(playerSelection, text="Deirdre", command=lambda:playerSelect("deirdreTruong"), height=4, width=15)
edwardKang = Button(playerSelection, text="Edward", command=lambda:playerSelect("edwardKang"), height=4, width=15)
kevinMa = Button(playerSelection, text="Kema", command=lambda:playerSelect("kevinMa"), height=4, width=15)
kevinTang = Button(playerSelection, text="Ktang", command=lambda:playerSelect("kevinTang"), height=4, width=15)
lachlanDenham = Button(playerSelection, text="Lachlan", command=lambda:playerSelect("lachlanDenham"), height=4, width=15)
mimiChen = Button(playerSelection, text="Mimi", command=lambda:playerSelect("mimiChen"), height=4, width=15)
willOuyang = Button(playerSelection, text="Will", command=lambda:playerSelect("willOuyang"), height=4, width=15)

buttonColor = brandonChan.cget("background")

#Initializing Statisitic Add and Subtract Buttons
serveErrors = LabelFrame(root, text="Serve Errors: ", padx=10, pady=10)
serveErrorsAdd = Button(serveErrors, text="+", padx=20, pady=15)
serveErrorsRemove = Button(serveErrors, text="-", padx=20, pady=15)

serveSuccess = LabelFrame(root, text="Serve Successes: ", padx=10, pady=10)
serveSuccessAdd = Button(serveSuccess, text="+", padx=20, pady=15)
serveSuccessRemove = Button(serveSuccess, text="-", padx=20, pady=15)

receiveErrors = LabelFrame(root, text="Receive Errors: ", padx=10, pady=10)
receiveErrorsAdd = Button(receiveErrors, text="+", padx=20, pady=15)
receiveErrorsRemove = Button(receiveErrors, text="-", padx=20, pady=15)

receiveSuccess = LabelFrame(root, text="Receive Successes: ", padx=10, pady=10)
receiveSuccessAdd = Button(receiveSuccess, text="+", padx=20, pady=15)
receiveSuccessRemove = Button(receiveSuccess, text="-", padx=20, pady=15)

spikeErrors = LabelFrame(root, text="Spike Errors: ", padx=10, pady=10)
spikeErrorsAdd = Button(spikeErrors, text="+", padx=20, pady=15)
spikeErrorsRemove = Button(spikeErrors, text="-", padx=20, pady=15)

spikeSuccess = LabelFrame(root, text="Spike Successes: ", padx=10, pady=10)
spikeSuccessAdd = Button(spikeSuccess, text="+", padx=20, pady=15)
spikeSuccessRemove = Button(spikeSuccess, text="-", padx=20, pady=15)

blockErrors = LabelFrame(root, text="Block Errors: ", padx=10, pady=10)
blockErrorsAdd = Button(blockErrors, text="+", padx=20, pady=15)
blockErrorsRemove = Button(blockErrors, text="-", padx=20, pady=15)

blockSuccess = LabelFrame(root, text="Block Successes: ", padx=10, pady=10)
blockSuccessAdd = Button(blockSuccess, text="+", padx=20, pady=15)
blockSuccessRemove = Button(blockSuccess, text="-", padx=20, pady=15)

Faults = LabelFrame(root, text="Faults: ", padx=10, pady=10)
FaultsAdd = Button(Faults, text="+", padx=20, pady=15)
FaultsRemove = Button(Faults, text="-", padx=20, pady=15)


statisticsFrame = LabelFrame(root, text="Player Statistics", padx=10, pady=10)
serveErrorsLabel = Label(statisticsFrame, text="Serve Errors: ", padx=10, pady=10)
serveSuccessLabel = Label(statisticsFrame, text="Serve Successes: ", padx=10, pady=10)
serveRateLabel = Label(statisticsFrame, text="Serve Rate: " + "TO FILL" + "%", padx=10, pady=10)
receiveErrorsLabel = Label(statisticsFrame, text="Receive Errors: ", padx=10, pady=10)
receiveSuccessLabel = Label(statisticsFrame, text="Receive Successes: ", padx=10, pady=10)
receiveRateLabel = Label(statisticsFrame, text="Receive Rate: " + "TO FILL" + "%", padx=10, pady=10)
spikeErrorsLabel = Label(statisticsFrame, text="Spike Errors: ", padx=10, pady=10)
spikeSuccessLabel = Label(statisticsFrame, text="Spike Successes: ", padx=10, pady=10)
spikeRateLabel = Label(statisticsFrame, text="Spike Rate: " + "TO FILL" + "%", padx=10, pady=10)
blockErrorsLabel = Label(statisticsFrame, text="Block Errors: ", padx=10, pady=10)
blockSuccessLabel = Label(statisticsFrame, text="Block Successes: ", padx=10, pady=10)
blockRateLabel = Label(statisticsFrame, text="Block Rate: " + "TO FILL" + "%", padx=10, pady=10)
FaultsLabel = Label(statisticsFrame, text="Faults: ", padx=10, pady=10)


def nextWeek(weekNumber):
    global weekLabel
    global nextWeekButton
    global prevWeekButton
    
    
    weekLabel.grid_forget()
    weekLabel = Label(root, text="Week: " + str(weekList[weekNumber-1]) + " of " + str(len(weekList)), padx=20, pady=10, anchor=W)
    prevWeekButton = Button(root, text= "<<", command=lambda: prevWeek(weekList[weekNumber-2]), padx=10, pady=10, anchor=W)
        
    if(weekNumber >= len(weekList)):
        nextWeekButton = Button(root, text= ">>", command=lambda: nextWeek(1), padx=10, pady=10, anchor=W)
        prevWeekButton = Button(root, text= "<<", command=lambda: prevWeek(len(weekList)-1), padx=10, pady=10, anchor=W)
    else:
        nextWeekButton = Button(root, text= ">>", command=lambda: nextWeek(weekList[weekNumber]), padx=10, pady=10, anchor=W)
    
    weekLabel.grid(row=0, column=3)
    prevWeekButton.grid(row=0, column=2)
    nextWeekButton.grid(row=0, column=4)
    
    


def prevWeek(weekNumber):
    global weekLabel
    global nextWeekButton
    global prevWeekButton
    
    weekLabel.grid_forget()
    weekLabel = Label(root, text="Week: " + str(weekList[weekNumber-1]) + " of " + str(len(weekList)), padx=20, pady=10, anchor=W)
    prevWeekButton = Button(root, text= "<<", command=lambda: prevWeek(weekList[weekNumber-2]), padx=10, pady=10, anchor=W)
    
    if(weekNumber >= len(weekList)):
        nextWeekButton = Button(root, text= ">>", command=lambda: nextWeek(1), padx=10, pady=10, anchor=W)
    else:
        nextWeekButton = Button(root, text= ">>", command=lambda: nextWeek(weekList[weekNumber]), padx=10, pady=10, anchor=W)
    
    weekLabel.grid(row=0, column=3)
    prevWeekButton.grid(row=0, column=2)
    nextWeekButton.grid(row=0, column=4)
        

def playerSelect(selectedPlayer):
    global brandonChan
    global callumAshton
    global danielPark
    global deirdreTruong
    global edwardKang
    global kevinMa
    global kevinTang
    global lachlanDenham
    global mimiChen
    global willOuyang
   
    if(selectedPlayer == "brandonChan"):
        buttonReset()
        brandonChan = Button(playerSelection, text="Chan", command=lambda:[self.color_change, buttonChange("brandonChan")], bg="blue", height=4, width=15)
        brandonChan.grid(row=0, column=0)
    
    if(selectedPlayer == "callumAshton"):
        buttonReset()
        callumAshton = Button(playerSelection, text="Callum", command=lambda:[self.color_change, buttonChange("callumAshton")], bg="blue", height=4, width=15)
        callumAshton.grid(row=0, column=1)
        
    
    if(selectedPlayer == "danielPark"):
        buttonReset()
        danielPark = Button(playerSelection, text="Daniel", command=lambda:[self.color_change, buttonChange("danielPark")], bg="blue", height=4, width=15)   
        danielPark.grid(row=0, column=2)
    
    
    if(selectedPlayer == "deirdreTruong"):
        buttonReset()
        deirdreTruong = Button(playerSelection, text="Deirdre", command=lambda:[self.color_change, buttonChange("deirdreTruong")], bg="blue", height=4, width=15)
        deirdreTruong.grid(row=0, column=3)
    
    if(selectedPlayer == "edwardKang"):
        buttonReset()
        edwardKang = Button(playerSelection, text="Edward", command=lambda:[self.color_change, buttonChange("edwardKang")], bg="blue", height=4, width=15)
        edwardKang.grid(row=0, column=4)
    
    if(selectedPlayer == "kevinMa"):
        buttonReset()
        kevinMa = Button(playerSelection, text="Kema", command=lambda:[self.color_change, buttonChange("kevinMa")], bg="blue", height=4, width=15)
        kevinMa.grid(row=1, column=0)
    
    
    if(selectedPlayer == "kevinTang"):
        buttonReset()
        kevinTang = Button(playerSelection, text="Ktang", command=lambda:[self.color_change, buttonChange("kevinTang")], bg="blue", height=4, width=15)
        kevinTang.grid(row=1, column=1)
    
    if(selectedPlayer == "lachlanDenham"):
        buttonReset()
        lachlanDenham = Button(playerSelection, text="Lachlan", command=lambda:[self.color_change, buttonChange("lachlanDenham")], bg="blue", height=4, width=15)
        lachlanDenham.grid(row=1, column=2)

    
    if(selectedPlayer == "mimiChen"):
        buttonReset()
        mimiChen = Button(playerSelection, text="Mimi", command=lambda:[self.color_change, buttonChange("mimiChen")], bg="blue", height=4, width=15)
        mimiChen.grid(row=1, column=3)
        
    
    if(selectedPlayer == "willOuyang"):
        buttonReset()
        willOuyang = Button(playerSelection, text="Will", command=lambda:[self.color_change, buttonChange("willOuyang")], bg="blue", height=4, width=15)
        willOuyang.grid(row=1, column=4)
    

def buttonReset():
    global brandonChan
    global callumAshton
    global danielPark
    global deirdreTruong
    global edwardKang
    global kevinMa
    global kevinTang
    global lachlanDenham
    global mimiChen
    global willOuyang
    
    brandonChan = Button(playerSelection, text="Chan", command=lambda:playerSelect("brandonChan"), height=4, width=15)
    callumAshton = Button(playerSelection, text="Callum", command=lambda:playerSelect("callumAshton"), height=4, width=15)
    danielPark = Button(playerSelection, text="Daniel", command=lambda:playerSelect("danielPark"), height=4, width=15)
    deirdreTruong = Button(playerSelection, text="Deirdre", command=lambda:playerSelect("deirdreTruong"), height=4, width=15)
    edwardKang = Button(playerSelection, text="Edward", command=lambda:playerSelect("edwardKang"), height=4, width=15)
    kevinMa = Button(playerSelection, text="Kema", command=lambda:playerSelect("kevinMa"), height=4, width=15)
    kevinTang = Button(playerSelection, text="Ktang", command=lambda:playerSelect("kevinTang"), height=4, width=15)
    lachlanDenham = Button(playerSelection, text="Lachlan", command=lambda:playerSelect("lachlanDenham"), height=4, width=15)
    mimiChen = Button(playerSelection, text="Mimi", command=lambda:playerSelect("mimiChen"), height=4, width=15)
    willOuyang = Button(playerSelection, text="Will", command=lambda:playerSelect("willOuyang"), height=4, width=15)
    
    brandonChan.grid(row=0, column=0)
    callumAshton.grid(row=0, column=1)
    danielPark.grid(row=0, column=2)
    deirdreTruong.grid(row=0, column=3)
    edwardKang.grid(row=0, column=4)
    kevinMa.grid(row=1, column=0)
    kevinTang.grid(row=1, column=1)
    lachlanDenham.grid(row=1, column=2)
    mimiChen.grid(row=1, column=3)
    willOuyang.grid(row=1, column=4)


def buttonChange(playerName):
    
    
    return


exitButton = Button(root, text= "Exit", command=root.quit, padx=20, pady=10)


titleLabel.grid(row=0, column=0, padx=(20,0), pady=(0, 20))
prevWeekButton.grid(row=0, column=2)
weekLabel.grid(row=0, column=3)
nextWeekButton.grid(row=0, column=4)

#Player Selection buttons
playerSelection.grid(row=1, column=0, columnspan=5, padx=10, pady=5)
brandonChan.grid(row=0, column=0)
callumAshton.grid(row=0, column=1)
danielPark.grid(row=0, column=2)
deirdreTruong.grid(row=0, column=3)
edwardKang.grid(row=0, column=4)
kevinMa.grid(row=1, column=0)
kevinTang.grid(row=1, column=1)
lachlanDenham.grid(row=1, column=2)
mimiChen.grid(row=1, column=3)
willOuyang.grid(row=1, column=4)


#buttons and frames for changing data
serveErrors.grid(row=2, column=0, padx=10, pady=5)
serveErrorsAdd.grid(row=0, column=0)
serveErrorsRemove.grid(row=0, column=1)

serveSuccess.grid(row=2, column=1, padx=10, pady=5)
serveSuccessAdd.grid(row=0, column=0)
serveSuccessRemove.grid(row=0, column=1)

receiveErrors.grid(row=2, column=2, padx=10, pady=5)
receiveErrorsAdd.grid(row=0, column=0)
receiveErrorsRemove.grid(row=0, column=1)

receiveSuccess.grid(row=2, column=3, padx=10, pady=5)
receiveSuccessAdd.grid(row=0, column=0)
receiveSuccessRemove.grid(row=0, column=1)

spikeErrors.grid(row=3, column=0, padx=10, pady=5)
spikeErrorsAdd.grid(row=0, column=0)
spikeErrorsRemove.grid(row=0, column=1)

spikeSuccess.grid(row=3, column=1, padx=10, pady=5)
spikeSuccessAdd.grid(row=0, column=0)
spikeSuccessRemove.grid(row=0, column=1)

blockErrors.grid(row=3, column=2, padx=10, pady=5)
blockErrorsAdd.grid(row=0, column=0)
blockErrorsRemove.grid(row=0, column=1)

blockSuccess.grid(row=3, column=3, padx=10, pady=5)
blockSuccessAdd.grid(row=0, column=0)
blockSuccessRemove.grid(row=0, column=1)

Faults.grid(row=4, column=0, padx=10, pady=5)
FaultsAdd.grid(row=0, column=0)
FaultsRemove.grid(row=0, column=1)

#Statistics frame and labels
statisticsFrame.grid(row=4, column=1, columnspan=3, padx=5)
serveErrorsLabel.grid(row=0, column=0, padx=10,)
serveSuccessLabel.grid(row=0, column=1, padx=10)
serveRateLabel.grid(row=0, column=2, padx=10)
receiveErrorsLabel.grid(row=1, column=0, padx=10)
receiveSuccessLabel.grid(row=1, column=1, padx=10)
receiveRateLabel.grid(row=1, column=2, padx=10)
spikeErrorsLabel.grid(row=2, column=0, padx=10)
spikeSuccessLabel.grid(row=2, column=1, padx=10)
spikeRateLabel.grid(row=2, column=2, padx=10)
blockErrorsLabel.grid(row=3, column=0, padx=10)
blockSuccessLabel.grid(row=3, column=1, padx=10)
blockRateLabel.grid(row=3, column=2, padx=10)
FaultsLabel.grid(row=4, column=0, padx=10)
exitButton.grid(row=99, column=4)


root.mainloop()

