from tkinter import *
from .season_selector import seasonSelectionWindow


def app():
    root = Tk()
    root.title('Volleyball Statistics Viewer')



    def openEditor():
        top = Toplevel()
        b = seasonSelectionWindow(top)
        top.mainloop()
        return



    def openPlayerStats():
        return

    def openTeamStats():
        return

    titleLabel = Label(root, text="Main Menu", padx=5, pady=10, anchor=W)

    statsEditorFrame = LabelFrame(root, text="Statistics Editor", padx=10, pady=10)
    statsEditorButton = Button(statsEditorFrame, command=openEditor, height=4, width=15)

    playerStatisticsViewer = LabelFrame(root, text="View Player Statistics", padx=10, pady=10)
    playerStatisticsButton = Button(playerStatisticsViewer, command=openPlayerStats, height=4, width=15)

    teamStatisticsViewer = LabelFrame(root, text="View Team Statistics", padx=10, pady=10)
    teamStatisticsButton = Button(teamStatisticsViewer, command=openTeamStats, height=4, width=15)


    titleLabel.grid(row=0, column=0, pady=(10, 20), columnspan=5)

    statsEditorFrame.grid(row=2, column=0, padx=10, pady=5)
    statsEditorButton.grid(row=0, column=0)

    playerStatisticsViewer.grid(row=2, column=1, padx=10, pady=5)
    playerStatisticsButton.grid(row=0, column=0)

    teamStatisticsViewer.grid(row=3, column=0, columnspan=4, padx=10, pady=5)
    teamStatisticsButton.grid(row=0, column=0)





    root.mainloop()