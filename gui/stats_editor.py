from tkinter import *
from openpyxl.workbook import Workbook
from openpyxl import load_workbook
from tkinter import messagebox
from .add_player_window import addPlayerWindow


class statsEditor():
     
    
    def __init__(self, master, seasonName, seasonNo):
        
        
        self.wb = Workbook()
        self.wb = load_workbook('data/volley_stats.xlsx')

        self.ws1 = self.wb[seasonName]
        
        self.ws2 = self.wb['Team Info']
        
        self.seasonList = [1, 2]
        self.seasonNumber = seasonNo

        self.playerNumber = self.ws2[('B' + str(((self.seasonNumber-1) * 5) + 4))].value

        self.weekList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        self.weekNumber = 1
        
        self.selectedPlayer = "None"

        master.title('Volleyball Statistics Input')

        self.titleLabel = Label(master, text="(Get WorkSheet Title)")

        self.newPlayerFrame = LabelFrame(master, text="Add/Remove Player", padx=10, pady=10)
        self.playerAdd = Button(self.newPlayerFrame, text="+", command=lambda: self.addPlayer(), padx=20, pady=15)
        self.playerRemove = Button(self.newPlayerFrame, text="-", command=lambda: self.removePlayer(self.selectedPlayer), padx=20, pady=15)

        self.seasonFrame = LabelFrame(master, text="Season Selection", padx=10, pady=10)
        self.seasonLabel = Label(self.seasonFrame, text="Season: 1 of "+ str(len(self.seasonList)), padx=20, pady=10)
        self.prevSeasonButton = Button(self.seasonFrame, text= "<<", command=lambda: self.prevWeek(), padx=10, pady=10, anchor=W) #
        self.nextSeasonButton = Button(self.seasonFrame, text= ">>", command=lambda: self.nextWeek(), padx=10, pady=10, anchor=W) 


        self.weekFrame = LabelFrame(master, text="Week Selection", padx=10, pady=10)
        self.weekLabel = Label(self.weekFrame, text="Week: 1 of "+ str(len(self.weekList)), padx=20, pady=10)
        self.prevWeekButton = Button(self.weekFrame, text= "<<", command=lambda: self.prevWeek(), padx=10, pady=10, anchor=W) #
        self.nextWeekButton = Button(self.weekFrame, text= ">>", command=lambda: self.nextWeek(), padx=10, pady=10, anchor=W) 
    
        #Initializing Player Selection Buttons
        self.playerSelection = LabelFrame(master, text="Player Selection", padx=5, pady=5)
        self.brandonChan = Button(self.playerSelection, text="Chan", command=lambda: self.playerSelect("brandonChan"), height=4, width=15)
        self.callumAshton = Button(self.playerSelection, text="Callum", command=lambda: self.playerSelect("callumAshton"), height=4, width=15)
        self.danielPark = Button(self.playerSelection, text="Daniel", command=lambda: self.playerSelect("danielPark"), height=4, width=15)
        self.deirdreTruong = Button(self.playerSelection, text="Deirdre", command=lambda: self.playerSelect("deirdreTruong"), height=4, width=15)
        self.edwardKang = Button(self.playerSelection, text="Edward", command=lambda: self.playerSelect("edwardKang"), height=4, width=15)
        self.kevinMa = Button(self.playerSelection, text="Kema", command=lambda: self.playerSelect("kevinMa"), height=4, width=15)
        self.kevinTang = Button(self.playerSelection, text="Ktang", command=lambda: self.playerSelect("kevinTang"), height=4, width=15)
        self.lachlanDenham = Button(self.playerSelection, text="Lachlan", command=lambda: self.playerSelect("lachlanDenham"), height=4, width=15)
        self.mimiChen = Button(self.playerSelection, text="Mimi", command=lambda: self.playerSelect("mimiChen"), height=4, width=15)
        self.willOuyang = Button(self.playerSelection, text="Will", command=lambda: self.playerSelect("willOuyang"), height=4, width=15)
        
        #buttonColor = brandonChan.cget("background")

        #Initializing Statisitic Add and Subtract Buttons
        self.serveErrors = LabelFrame(master, text="Serve Errors", padx=5, pady=5)
        self.serveErrorsAdd = Button(self.serveErrors, text="+", command=lambda: self.statIncrease("serveErrors"), padx=20, pady=15)
        self.serveErrorsRemove = Button(self.serveErrors, text="-", command=lambda: self.statDecrease("serveErrors"), padx=20, pady=15)
  
        self.serveSuccess = LabelFrame(master, text="Serve Successes", padx=5, pady=5)
        self.serveSuccessAdd = Button(self.serveSuccess, text="+", command=lambda: self.statIncrease("serveSuccess"), padx=20, pady=15)
        self.serveSuccessRemove = Button(self.serveSuccess, text="-", command=lambda: self.statDecrease("serveSuccess"), padx=20, pady=15)
  
        self.receiveErrors = LabelFrame(master, text="Receive Errors", padx=5, pady=5)
        self.receiveErrorsAdd = Button(self.receiveErrors, text="+", command=lambda: self.statIncrease("receiveErrors"), padx=20, pady=15)
        self.receiveErrorsRemove = Button(self.receiveErrors, text="-", command=lambda: self.statDecrease("receiveErrors"), padx=20, pady=15)
     
        self.receiveSuccess = LabelFrame(master, text="Receive Successes", padx=5, pady=5)
        self.receiveSuccessAdd = Button(self.receiveSuccess, text="+", command=lambda: self.statIncrease("receiveSuccess"), padx=20, pady=15)
        self.receiveSuccessRemove = Button(self.receiveSuccess, text="-", command=lambda: self.statDecrease("receiveSuccess"), padx=20, pady=15)

        self.setErrors = LabelFrame(master, text="Set Errors", padx=5, pady=5)
        self.setErrorsAdd = Button(self.setErrors, text="+", command=lambda: self.statIncrease("setErrors"), padx=20, pady=15)
        self.setErrorsRemove = Button(self.setErrors, text="-", command=lambda: self.statDecrease("setErrors"), padx=20, pady=15)
     
        self.setSuccess = LabelFrame(master, text="Set Successes", padx=5, pady=5)
        self.setSuccessAdd = Button(self.setSuccess, text="+", command=lambda: self.statIncrease("setSuccess"), padx=20, pady=15)
        self.setSuccessRemove = Button(self.setSuccess, text="-", command=lambda: self.statDecrease("setSuccess"), padx=20, pady=15)
      
        self.spikeErrors = LabelFrame(master, text="Spike Errors", padx=5, pady=5)
        self.spikeErrorsAdd = Button(self.spikeErrors, text="+", command=lambda: self.statIncrease("spikeErrors"), padx=20, pady=15)
        self.spikeErrorsRemove = Button(self.spikeErrors, text="-", command=lambda: self.statDecrease("spikeErrors"), padx=20, pady=15)
     
        self.spikeSuccess = LabelFrame(master, text="Spike Successes", padx=5, pady=5)
        self.spikeSuccessAdd = Button(self.spikeSuccess, text="+", command=lambda: self.statIncrease("spikeSuccess"), padx=20, pady=15)
        self.spikeSuccessRemove = Button(self.spikeSuccess, text="-", command=lambda: self.statDecrease("spikeSuccess"), padx=20, pady=15)

        self.tipErrors = LabelFrame(master, text="Tip Errors", padx=5, pady=5)
        self.tipErrorsAdd = Button(self.tipErrors, text="+", command=lambda: self.statIncrease("tipErrors"), padx=20, pady=15)
        self.tipErrorsRemove = Button(self.tipErrors, text="-", command=lambda: self.statDecrease("tipErrors"), padx=20, pady=15)
     
        self.tipSuccess = LabelFrame(master, text="Tip Successes", padx=5, pady=5)
        self.tipSuccessAdd = Button(self.tipSuccess, text="+", command=lambda: self.statIncrease("tipSuccess"), padx=20, pady=15)
        self.tipSuccessRemove = Button(self.tipSuccess, text="-", command=lambda: self.statDecrease("tipSuccess"), padx=20, pady=15)
     
        self.blockErrors = LabelFrame(master, text="Block Errors", padx=5, pady=5)
        self.blockErrorsAdd = Button(self.blockErrors, text="+", command=lambda: self.statIncrease("blockErrors"), padx=20, pady=15)
        self.blockErrorsRemove = Button(self.blockErrors, text="-", command=lambda: self.statDecrease("blockErrors"), padx=20, pady=15)
    
        self.blockSuccess = LabelFrame(master, text="Block Successes", padx=5, pady=5)
        self.blockSuccessAdd = Button(self.blockSuccess, text="+", command=lambda: self.statIncrease("blockSuccess"), padx=20, pady=15)
        self.blockSuccessRemove = Button(self.blockSuccess, text="-", command=lambda: self.statDecrease("blockSuccess"), padx=20, pady=15)
     
        self.Faults = LabelFrame(master, text="Faults", padx=5, pady=5)
        self.FaultsAdd = Button(self.Faults, text="+", command=lambda: self.statIncrease("Faults"), padx=20, pady=15)
        self.FaultsRemove = Button(self.Faults, text="-", command=lambda: self.statDecrease("Faults"), padx=20, pady=15)
      
        #Initialising Statistics table
        self.statisticsmaster = LabelFrame(master, text="Player Statistics", padx=10, pady=7)
        self.serveErrorsLabel = Label(self.statisticsmaster, text="Serve Errors: ", padx=10, pady=7)
        self.serveSuccessLabel = Label(self.statisticsmaster, text="Serve Successes: ", padx=10, pady=7)
        self.serveRateLabel = Label(self.statisticsmaster, text="Serve Rate: ", padx=10, pady=7)
        self.receiveErrorsLabel = Label(self.statisticsmaster, text="Receive Errors: ", padx=10, pady=7)
        self.receiveSuccessLabel = Label(self.statisticsmaster, text="Receive Successes: ", padx=10, pady=7)
        self.receiveRateLabel = Label(self.statisticsmaster, text="Pass Rate: ", padx=10, pady=7)
        self.setErrorsLabel = Label(self.statisticsmaster, text="Set Errors: ", padx=10, pady=7)
        self.setSuccessLabel = Label(self.statisticsmaster, text="Set Successes: ", padx=10, pady=7)
        self.setRateLabel = Label(self.statisticsmaster, text="Set Rate: ", padx=10, pady=7)
        self.spikeErrorsLabel = Label(self.statisticsmaster, text="Spike Errors: ", padx=10, pady=7)
        self.spikeSuccessLabel = Label(self.statisticsmaster, text="Spike Successes: ", padx=10, pady=7)
        self.spikeRateLabel = Label(self.statisticsmaster, text="Spike Rate: ", padx=10, pady=7)
        self.tipErrorsLabel = Label(self.statisticsmaster, text="Tip Errors: ", padx=10, pady=7)
        self.tipSuccessLabel = Label(self.statisticsmaster, text="Tip Successes: ", padx=10, pady=7)
        self.tipRateLabel = Label(self.statisticsmaster, text="Tip Rate: ", padx=10, pady=7)
        self.blockErrorsLabel = Label(self.statisticsmaster, text="Block Errors: ", padx=10, pady=7)
        self.blockSuccessLabel = Label(self.statisticsmaster, text="Block Successes: ", padx=10, pady=7)
        self.blockRateLabel = Label(self.statisticsmaster, text="Block Rate: ", padx=10, pady=7)
        self.FaultsLabel = Label(self.statisticsmaster, text="Faults: ", padx=10, pady=7)
        
        self.exitButton = Button(master, text= "Exit", command=master.destroy, padx=20, pady=10)
        
        ##Attaching all initial state GUI components to grid
        
        #Initial elements
        self.titleLabel.grid(row=0, column=0)

        self.newPlayerFrame.grid(row=1, column=0, padx=10)
        self.playerAdd.grid(row=0, column=0)
        self.playerRemove.grid(row=0, column=1)
        
        self.weekFrame.grid(row=0, column=3, columnspan=2, padx=(0,20))
        self.prevWeekButton.grid(row=0, column=0)
        self.weekLabel.grid(row=0, column=1)
        self.nextWeekButton.grid(row=0, column=2)
     
        #Player Selection buttons
        self.playerSelection.grid(row=1, column=1, columnspan=4, padx=10, pady=5)
        self.brandonChan.grid(row=0, column=0)
        self.callumAshton.grid(row=0, column=1)
        self.danielPark.grid(row=0, column=2)
        self.deirdreTruong.grid(row=0, column=3)
        self.edwardKang.grid(row=0, column=4)
        self.kevinMa.grid(row=1, column=0)
        self.kevinTang.grid(row=1, column=1)
        self.lachlanDenham.grid(row=1, column=2)
        self.mimiChen.grid(row=1, column=3)
        self.willOuyang.grid(row=1, column=4)
      
        #buttons and frames for changing data
        self.serveErrors.grid(row=2, column=0, padx=10, pady=5)
        self.serveErrorsAdd.grid(row=0, column=0)
        self.serveErrorsRemove.grid(row=0, column=1)
      
        self.serveSuccess.grid(row=2, column=1, padx=10, pady=5)
        self.serveSuccessAdd.grid(row=0, column=0)
        self.serveSuccessRemove.grid(row=0, column=1)
      
        self.receiveErrors.grid(row=2, column=2, padx=10, pady=5)
        self.receiveErrorsAdd.grid(row=0, column=0)
        self.receiveErrorsRemove.grid(row=0, column=1)
      
        self.receiveSuccess.grid(row=2, column=3, padx=10, pady=5)
        self.receiveSuccessAdd.grid(row=0, column=0)
        self.receiveSuccessRemove.grid(row=0, column=1)

        self.setErrors.grid(row=3, column=0, padx=10, pady=5)
        self.setErrorsAdd.grid(row=0, column=0)
        self.setErrorsRemove.grid(row=0, column=1)
      
        self.setSuccess.grid(row=3, column=1, padx=10, pady=5)
        self.setSuccessAdd.grid(row=0, column=0)
        self.setSuccessRemove.grid(row=0, column=1)
   
        self.spikeErrors.grid(row=3, column=2, padx=10, pady=5)
        self.spikeErrorsAdd.grid(row=0, column=0)
        self.spikeErrorsRemove.grid(row=0, column=1)
       
        self.spikeSuccess.grid(row=3, column=3, padx=10, pady=5)
        self.spikeSuccessAdd.grid(row=0, column=0)
        self.spikeSuccessRemove.grid(row=0, column=1)
        
        self.tipErrors.grid(row=4, column=0, padx=10, pady=5)
        self.tipErrorsAdd.grid(row=0, column=0)
        self.tipErrorsRemove.grid(row=0, column=1)
       
        self.tipSuccess.grid(row=4, column=1, padx=10, pady=5)
        self.tipSuccessAdd.grid(row=0, column=0)
        self.tipSuccessRemove.grid(row=0, column=1)
        
        self.blockErrors.grid(row=4, column=2, padx=10, pady=5)
        self.blockErrorsAdd.grid(row=0, column=0)
        self.blockErrorsRemove.grid(row=0, column=1)
       
        self.blockSuccess.grid(row=4, column=3, padx=10, pady=5)
        self.blockSuccessAdd.grid(row=0, column=0)
        self.blockSuccessRemove.grid(row=0, column=1)
      
        self.Faults.grid(row=5, column=0, padx=10, pady=5)
        self.FaultsAdd.grid(row=0, column=0)
        self.FaultsRemove.grid(row=0, column=1)
      
        #Statistics frame and labels
        self.statisticsmaster.grid(row=5, column=1, columnspan=3, padx=5)
        self.serveErrorsLabel.grid(row=0, column=0, padx=10,)
        self.serveSuccessLabel.grid(row=0, column=1, padx=10)
        self.serveRateLabel.grid(row=0, column=2, padx=10)
        self.receiveErrorsLabel.grid(row=1, column=0, padx=8)
        self.receiveSuccessLabel.grid(row=1, column=1, padx=8)
        self.receiveRateLabel.grid(row=1, column=2, padx=8)
        self.setErrorsLabel.grid(row=2, column=0, padx=10)
        self.setSuccessLabel.grid(row=2, column=1, padx=10)
        self.setRateLabel.grid(row=2, column=2, padx=10)
        self.spikeErrorsLabel.grid(row=3, column=0, padx=10)
        self.spikeSuccessLabel.grid(row=3, column=1, padx=10)
        self.spikeRateLabel.grid(row=3, column=2, padx=10)
        self.tipErrorsLabel.grid(row=4, column=0, padx=10)
        self.tipSuccessLabel.grid(row=4, column=1, padx=10)
        self.tipRateLabel.grid(row=4, column=2, padx=10)
        self.blockErrorsLabel.grid(row=5, column=0, padx=10)
        self.blockSuccessLabel.grid(row=5, column=1, padx=10)
        self.blockRateLabel.grid(row=5, column=2, padx=10)
        self.FaultsLabel.grid(row=6, column=0, padx=10)
        
        #self.exitButton.grid(row=99, column=4)
    
    #Function for iterating week forwards once
    def nextWeek(self): 
        self.weekLabel.grid_forget()
        
        if(self.weekNumber >= len(self.weekList)):
            self.weekNumber = 1
        else:
            self.weekNumber += 1
        self.weekLabel = Label(self.weekFrame, text="Week: " + str(self.weekList[self.weekNumber-1]) + " of " + str(len(self.weekList)), padx=20, pady=10, anchor=W)
        self.weekLabel.grid(row=0, column=1)
        self.prevWeekButton.grid(row=0, column=0)
        self.nextWeekButton.grid(row=0, column=2)
        if(self.selectedPlayer != "None"):
            self.updateStatsLabels()
        return
    
    #Function for iterating week backwards once
    def prevWeek(self):
      
        self.weekLabel.grid_forget()
        
        if(self.weekNumber-1 == 0):
            self.weekNumber = 11   
        else:
            self.weekNumber -= 1 
        self.weekLabel = Label(self.weekFrame, text="Week: " + str(self.weekList[self.weekNumber-1]) + " of " + str(len(self.weekList)), padx=20, pady=10, anchor=W)
        self.weekLabel.grid(row=0, column=1)
        self.prevWeekButton.grid(row=0, column=0)
        self.nextWeekButton.grid(row=0, column=2)
        if(self.selectedPlayer != "None"):
            self.updateStatsLabels()
        return
    
    #Function for selecting an individual player's data
    def playerSelect(self, playerName):
        self.selectedPlayer = playerName
        self.buttonReset()
        self.updateStatsLabels()   

        if(self.selectedPlayer == "brandonChan"):
            self.brandonChan = Button(self.playerSelection, text="Chan", command=lambda:self.playerSelect("brandonChan"), bg="blue", height=4, width=15)
            self.brandonChan.grid(row=0, column=0)
        
        if(self.selectedPlayer == "callumAshton"):
            self.callumAshton = Button(self.playerSelection, text="Callum", command=lambda:self.playerSelect("callumAshton"), bg="blue", height=4, width=15)
            self.callumAshton.grid(row=0, column=1)
            
        
        if(self.selectedPlayer == "danielPark"):
            self.danielPark = Button(self.playerSelection, text="Daniel", command=lambda:self.playerSelect("danielPark"), bg="blue", height=4, width=15)   
            self.danielPark.grid(row=0, column=2)
        
        
        if(self.selectedPlayer == "deirdreTruong"):
            self.deirdreTruong = Button(self.playerSelection, text="Deirdre", command=lambda:self.playerSelect("deirdreTruong"), bg="blue", height=4, width=15)
            self.deirdreTruong.grid(row=0, column=3)
        
        if(self.selectedPlayer == "edwardKang"):
            self.edwardKang = Button(self.playerSelection, text="Edward", command=lambda:self.playerSelect("edwardKang"), bg="blue", height=4, width=15)
            self.edwardKang.grid(row=0, column=4)
        
        if(self.selectedPlayer == "kevinMa"):
            self.kevinMa = Button(self.playerSelection, text="Kema", command=lambda:self.playerSelect("kevinMa"), bg="blue", height=4, width=15)
            self.kevinMa.grid(row=1, column=0)
        
        
        if(self.selectedPlayer == "kevinTang"):
            self.kevinTang = Button(self.playerSelection, text="Ktang", command=lambda:self.playerSelect("kevinTang"), bg="blue", height=4, width=15)
            self.kevinTang.grid(row=1, column=1)
        
        if(self.selectedPlayer == "lachlanDenham"):
            self.lachlanDenham = Button(self.playerSelection, text="Lachlan", command=lambda:self.playerSelect("lachlanDenham"), bg="blue", height=4, width=15)
            self.lachlanDenham.grid(row=1, column=2)
    
        
        if(self.selectedPlayer == "mimiChen"):
            self.mimiChen = Button(self.playerSelection, text="Mimi", command=lambda:self.playerSelect("mimiChen"), bg="blue", height=4, width=15)
            self.mimiChen.grid(row=1, column=3)
            
        
        if(self.selectedPlayer == "willOuyang"):
            self.willOuyang = Button(self.playerSelection, text="Will", command=lambda:self.playerSelect("willOuyang"), bg="blue", height=4, width=15)
            self.willOuyang.grid(row=1, column=4)
        
    #Function for reseting existing player selection upon new selection
    def buttonReset(self):
        
        self.brandonChan = Button(self.playerSelection, text="Chan", command=lambda: self.playerSelect("brandonChan"), height=4, width=15)
        self.callumAshton = Button(self.playerSelection, text="Callum", command=lambda: self.playerSelect("callumAshton"), height=4, width=15)
        self.danielPark = Button(self.playerSelection, text="Daniel", command=lambda: self.playerSelect("danielPark"), height=4, width=15)
        self.deirdreTruong = Button(self.playerSelection, text="Deirdre", command=lambda: self.playerSelect("deirdreTruong"), height=4, width=15)
        self.edwardKang = Button(self.playerSelection, text="Edward", command=lambda: self.playerSelect("edwardKang"), height=4, width=15)
        self.kevinMa = Button(self.playerSelection, text="Kema", command=lambda: self.playerSelect("kevinMa"), height=4, width=15)
        self.kevinTang = Button(self.playerSelection, text="Ktang", command=lambda: self.playerSelect("kevinTang"), height=4, width=15)
        self.lachlanDenham = Button(self.playerSelection, text="Lachlan", command=lambda: self.playerSelect("lachlanDenham"), height=4, width=15)
        self.mimiChen = Button(self.playerSelection, text="Mimi", command=lambda: self.playerSelect("mimiChen"), height=4, width=15)
        self.willOuyang = Button(self.playerSelection, text="Will", command=lambda: self.playerSelect("willOuyang"), height=4, width=15)
        
        self.brandonChan.grid(row=0, column=0)
        self.callumAshton.grid(row=0, column=1)
        self.danielPark.grid(row=0, column=2)
        self.deirdreTruong.grid(row=0, column=3)
        self.edwardKang.grid(row=0, column=4)
        self.kevinMa.grid(row=1, column=0)
        self.kevinTang.grid(row=1, column=1)
        self.lachlanDenham.grid(row=1, column=2)
        self.mimiChen.grid(row=1, column=3)
        self.willOuyang.grid(row=1, column=4)
    
    def statIncrease(self, getStatType):
        statTypeList = ["serveErrors", "serveSuccess", "receiveErrors", "receiveSuccess", "setErrors", "setSuccess", "spikeErrors", "spikeSuccess", "tipErrors", "tipSuccess", "blockErrors", "blockSuccess", "Faults"]
        columnList = ['B', 'C', 'E', 'F', 'H', 'I', 'K', 'L', 'N', 'O', 'Q', 'R', 'T']
        columnChar = columnList[statTypeList.index(getStatType)]
        if(self.selectedPlayer == "None"):
            messagebox.showinfo("Error", "No Player Selected")
            return
        
        rowNumber = self.getRowNumber()
        self.ws1[(columnChar + str(rowNumber))] = self.ws1[(columnChar + str(rowNumber))].value + 1
        self.updateStatsLabels()
        return

    def statDecrease(self, getStatType):
        statTypeList = ["serveErrors", "serveSuccess", "receiveErrors", "receiveSuccess", "setErrors", "setSuccess", "spikeErrors", "spikeSuccess", "tipErrors", "tipSuccess", "blockErrors", "blockSuccess", "Faults"]
        columnList = ['B', 'C', 'E', 'F', 'H', 'I', 'K', 'L', 'N', 'O', 'Q', 'R', 'T']
        columnChar = columnList[statTypeList.index(getStatType)]
        if(self.selectedPlayer == "None"):
            messagebox.showinfo("Error", "No Player Selected")
            return
        
        rowNumber = self.getRowNumber()
        if(self.ws1[(columnChar + str(rowNumber))].value >= 1):
            self.ws1[(columnChar + str(rowNumber))] = self.ws1[(columnChar + str(rowNumber))].value - 1
            self.updateStatsLabels()
        else:
            messagebox.showinfo("Error", "You Cannot Decrease This Value Below 0")
        self.updateStatsLabels()
        return

    def getRowNumber(self):
        playerList = ["brandonChan", "callumAshton", "danielPark", "deirdreTruong", "edwardKang", "kevinMa", "kevinTang", "lachlanDenham", "mimiChen", "willOuyang"]
        playerRow = playerList.index(self.selectedPlayer) + 1
        weekRowSelect = ((self.weekNumber-1) * 13)
        rowNumber = playerRow + weekRowSelect + 2
        return rowNumber


    def updateStatsLabels(self):
        
        rowNumber = self.getRowNumber()
        
        self.serveErrorsLabel.grid_forget()
        self.serveSuccessLabel.grid_forget()
        self.serveRateLabel.grid_forget()
        self.receiveErrorsLabel.grid_forget()
        self.receiveSuccessLabel.grid_forget()
        self.receiveRateLabel.grid_forget()
        self.setErrorsLabel.grid_forget()
        self.setSuccessLabel.grid_forget()
        self.setRateLabel.grid_forget()
        self.spikeErrorsLabel.grid_forget()
        self.spikeSuccessLabel.grid_forget()
        self.spikeRateLabel.grid_forget()
        self.tipErrorsLabel.grid_forget()
        self.tipSuccessLabel.grid_forget()
        self.tipRateLabel.grid_forget()
        self.blockErrorsLabel.grid_forget()
        self.blockSuccessLabel.grid_forget()
        self.blockRateLabel.grid_forget()
        self.FaultsLabel.grid_forget()

        if((self.ws1[('B' + str(rowNumber))].value + self.ws1[('C' + str(rowNumber))].value) != 0):
            self.ws1[('D' + str(rowNumber))].value = str(round((self.ws1[('C' + str(rowNumber))].value) / (self.ws1[('B' + str(rowNumber))].value + self.ws1[('C' + str(rowNumber))].value)*100)) + "%"
        else:
            self.ws1[('D' + str(rowNumber))].value = "0%"
        

        if((self.ws1[('E' + str(rowNumber))].value + self.ws1[('F' + str(rowNumber))].value) != 0):
            self.ws1[('G' + str(rowNumber))].value = str(round((self.ws1[('F' + str(rowNumber))].value) / (self.ws1[('E' + str(rowNumber))].value + self.ws1[('F' + str(rowNumber))].value)*100)) + "%"
        else:
            self.ws1[('G' + str(rowNumber))].value = "0%"


        if((self.ws1[('H' + str(rowNumber))].value + self.ws1[('I' + str(rowNumber))].value) != 0):
            self.ws1[('J' + str(rowNumber))].value = str(round((self.ws1[('I' + str(rowNumber))].value) / (self.ws1[('H' + str(rowNumber))].value + self.ws1[('I' + str(rowNumber))].value)*100)) + "%"
        else:
            self.ws1[('J' + str(rowNumber))].value = "0%"


        if((self.ws1[('K' + str(rowNumber))].value + self.ws1[('L' + str(rowNumber))].value) != 0):
            self.ws1[('M' + str(rowNumber))].value = str(round((self.ws1[('L' + str(rowNumber))].value) / (self.ws1[('K' + str(rowNumber))].value + self.ws1[('L' + str(rowNumber))].value)*100)) + "%"
        else:
            self.ws1[('M' + str(rowNumber))].value = "0%"

        
        if((self.ws1[('N' + str(rowNumber))].value + self.ws1[('O' + str(rowNumber))].value) != 0):
            self.ws1[('P' + str(rowNumber))].value = str(round((self.ws1[('O' + str(rowNumber))].value) / (self.ws1[('N' + str(rowNumber))].value + self.ws1[('O' + str(rowNumber))].value)*100)) + "%"
        else:
            self.ws1[('P' + str(rowNumber))].value = "0%"

        if((self.ws1[('Q' + str(rowNumber))].value + self.ws1[('R' + str(rowNumber))].value) != 0):
            self.ws1[('S' + str(rowNumber))].value = str(round((self.ws1[('R' + str(rowNumber))].value) / (self.ws1[('Q' + str(rowNumber))].value + self.ws1[('R' + str(rowNumber))].value)*100)) + "%"
        else:
            self.ws1[('S' + str(rowNumber))].value = "0%"

        self.serveErrorsLabel = Label(self.statisticsmaster, text="Serve Errors: " + str(self.ws1[('B' + str(rowNumber))].value), padx=10, pady=7)
        self.serveSuccessLabel = Label(self.statisticsmaster, text="Serve Successes: " + str(self.ws1[('C' + str(rowNumber))].value), padx=10, pady=7)
        self.serveRateLabel = Label(self.statisticsmaster, text="Serve Rate: " + str(self.ws1[('D' + str(rowNumber))].value), padx=10, pady=7)
        self.receiveErrorsLabel = Label(self.statisticsmaster, text="Receive Errors: " + str(self.ws1[('E' + str(rowNumber))].value), padx=8, pady=7)
        self.receiveSuccessLabel = Label(self.statisticsmaster, text="Receive Successes: " + str(self.ws1[('F' + str(rowNumber))].value), padx=8, pady=7)
        self.receiveRateLabel = Label(self.statisticsmaster, text="Receive Rate: " + str(self.ws1[('G' + str(rowNumber))].value), padx=8, pady=7)
        self.setErrorsLabel = Label(self.statisticsmaster, text="Set Errors: " + str(self.ws1[('H' + str(rowNumber))].value), padx=10, pady=7)
        self.setSuccessLabel = Label(self.statisticsmaster, text="Set Successes: " + str(self.ws1[('I' + str(rowNumber))].value), padx=10, pady=7)
        self.setRateLabel = Label(self.statisticsmaster, text="Set Rate: " + str(self.ws1[('J' + str(rowNumber))].value), padx=10, pady=7)
        self.spikeErrorsLabel = Label(self.statisticsmaster, text="Spike Errors: " + str(self.ws1[('K' + str(rowNumber))].value), padx=10, pady=7)
        self.spikeSuccessLabel = Label(self.statisticsmaster, text="Spike Successes: " + str(self.ws1[('L' + str(rowNumber))].value), padx=10, pady=7)
        self.spikeRateLabel = Label(self.statisticsmaster, text="Spike Rate: " + str(self.ws1[('M' + str(rowNumber))].value), padx=10, pady=7)
        self.tipErrorsLabel = Label(self.statisticsmaster, text="Tip Errors: " + str(self.ws1[('N' + str(rowNumber))].value), padx=10, pady=7)
        self.tipSuccessLabel = Label(self.statisticsmaster, text="Tip Successes: " + str(self.ws1[('O' + str(rowNumber))].value), padx=10, pady=7)
        self.tipRateLabel = Label(self.statisticsmaster, text="Tip Rate: " + str(self.ws1[('P' + str(rowNumber))].value), padx=10, pady=7)
        self.blockErrorsLabel = Label(self.statisticsmaster, text="Block Errors: " + str(self.ws1[('Q' + str(rowNumber))].value), padx=10, pady=7)
        self.blockSuccessLabel = Label(self.statisticsmaster, text="Block Successes: " + str(self.ws1[('R' + str(rowNumber))].value), padx=10, pady=7)
        self.blockRateLabel = Label(self.statisticsmaster, text="Block Rate: " + str(self.ws1[('S' + str(rowNumber))].value), padx=10, pady=7)
        self.FaultsLabel = Label(self.statisticsmaster, text="Faults: " + str(self.ws1[('T' + str(rowNumber))].value), padx=10, pady=7)

        self.statisticsmaster.grid(row=5, column=1, columnspan=3, padx=5)
        self.serveErrorsLabel.grid(row=0, column=0, padx=10)
        self.serveSuccessLabel.grid(row=0, column=1, padx=10)
        self.serveRateLabel.grid(row=0, column=2, padx=10)
        self.receiveErrorsLabel.grid(row=1, column=0, padx=8)
        self.receiveSuccessLabel.grid(row=1, column=1, padx=8)
        self.receiveRateLabel.grid(row=1, column=2, padx=8)
        self.setErrorsLabel.grid(row=2, column=0, padx=10)
        self.setSuccessLabel.grid(row=2, column=1, padx=10)
        self.setRateLabel.grid(row=2, column=2, padx=10)
        self.spikeErrorsLabel.grid(row=3, column=0, padx=10)
        self.spikeSuccessLabel.grid(row=3, column=1, padx=10)
        self.spikeRateLabel.grid(row=3, column=2, padx=10)
        self.tipErrorsLabel.grid(row=4, column=0, padx=10)
        self.tipSuccessLabel.grid(row=4, column=1, padx=10)
        self.tipRateLabel.grid(row=4, column=2, padx=10)
        self.blockErrorsLabel.grid(row=5, column=0, padx=10)
        self.blockSuccessLabel.grid(row=5, column=1, padx=10)
        self.blockRateLabel.grid(row=5, column=2, padx=10)
        self.FaultsLabel.grid(row=6, column=0, padx=10)

        self.wb.save('data/volley_stats.xlsx')

        return
    
    def addPlayer(self):
        top = Toplevel()
        b = addPlayerWindow(top)
        top.mainloop()

        return

    def removePlayer(self, playerName):
        return