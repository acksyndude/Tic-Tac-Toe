"""First but not working""" 
"""After Few Days Later -> It's Working Fine And it's "MINE" """ """But 2 dimensional (2D) array is inherited"""
from tkinter import * 
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror, showwarning, askyesno
import random as r

class Application(Tk):
	
	def __init__(self):
		super(Application, self).__init__()
		self.setWindow()
		self.createWidgets()

	def setWindow(self):
		self.title("Tic-Tak-Toe")
		self.resizable(False, False)
		self.geometry('644x444')


	def createWidgets(self):
		self.mainFrame = Frame(self)

		ttk.Label(self.mainFrame, text="Welcome To Tic-Tak-Toe", font=('sans-serif', 20, 'bold')).grid(pady=20, row=0, column=2)
		ttk.Label(self.mainFrame, text="Enter First Player Name (X): ").grid(row=1, column=1)
		ttk.Label(self.mainFrame, text="Enter Second Player Name (O): ").grid(row=2, column=1)

		self.playerFirstName = StringVar()
		self.playerSecondName = StringVar()

		self.enterFirstName = ttk.Entry(self.mainFrame, textvariable=self.playerFirstName)
		self.enterFirstName.grid(row=1, column=2, pady=3)
		self.enterSecondName = ttk.Entry(self.mainFrame, textvariable=self.playerSecondName)
		self.enterSecondName.grid(row=2, column=2)

		self.submitNames = ttk.Button(self.mainFrame, text="Start! Tic-Tak-Toe", command=self.startGame)
		self.submitNames.grid(row=3, column=2, ipadx=2, ipady=2, pady=10)
		self.mainFrame.pack(fill=BOTH)


	def startGame(self):
		# Forgetting main frame
		self.mainFrame.pack_forget()
		
		if self.playerFirstName.get() == "":
			self.playerFirstName.set("First Player")
		if self.playerSecondName.get() == "":
			self.playerSecondName.set("Second Player")
		

		self.scoreX = Label(self, text="Score of Player X : 0")
		self.scoreO = Label(self, text="Score of Player O : 0")
		self.scoreX.grid(row=0, column=2, padx=10)
		self.scoreO.grid(row=0, column=0)

		# 1 = X else O
		randomChoiceForPlayers = r.choice([1, 2])
		# print(randomChoiceForPlayers)
		self.defaultPlayer = randomChoiceForPlayers

		if self.defaultPlayer == 1:
			self.playerTurn = Label(self, text=f"Player Turn : {self.playerFirstName.get()}")
		else:
			self.playerTurn = Label(self, text=f"Player Turn : {self.playerSecondName.get()}")
		self.playerTurn.grid(row=1, column=3)

		self.toeFrame = Frame(self)
		self.toeFrame.grid(row=2, column=2)
		self.create_grid()	


	def create_grid(self):
		# defining here so just not reset when clik function run again
		self.buttons = [ [0, 0, 0], [0, 0, 0], [0, 0, 0] ]
		print(self.buttons)
		for i in range(1, 4):
			self.btnColumnZero = ttk.Button(self.toeFrame, text="")
			# make sure that it is in seprate line then it will work because the same time variable is getting defined
			self.btnColumnZero['command'] = lambda btnColumnZero=self.btnColumnZero: self.clik(btnColumnZero)
			self.btnColumnZero.grid(ipadx=20, ipady=20, row=i, column=0)

			self.btnColumnOne = ttk.Button(self.toeFrame, text="")
			self.btnColumnOne['command'] = lambda btnColumnOne=self.btnColumnOne: self.clik(btnColumnOne)
			self.btnColumnOne.grid(ipadx=20, ipady=20, row=i, column=1)

			self.btnColumnTwo = ttk.Button(self.toeFrame, text="")
			self.btnColumnTwo['command'] = lambda btnColumnTwo=self.btnColumnTwo: self.clik(btnColumnTwo)
			self.btnColumnTwo.grid(ipadx=20, ipady=20, row=i, column=2)

	def clik(self, num):
  
		if num['text'] == "":
			if self.defaultPlayer == 1:
				# print(self.defaultPlayer)
				self.defaultPlayer = 1+1
				# print(self.defaultPlayer)
				num["text"]= "X"
				self.playerTurn['text'] = f"Player Turn : {self.playerSecondName.get()}"

				if str(num)[9:] == "!button": self.buttons[0][0] = "X"
				if str(num)[9:] == "!button2": self.buttons[0][1] = "X"
				if str(num)[9:] == "!button3": self.buttons[0][2] = "X"

				if str(num)[9:] == "!button4": self.buttons[1][0] = "X"
				if str(num)[9:] == "!button5": self.buttons[1][1] = "X"
				if str(num)[9:] == "!button6": self.buttons[1][2] = "X"

				if str(num)[9:] == "!button7": self.buttons[2][0] = "X"
				if str(num)[9:] == "!button8": self.buttons[2][1] = "X"
				if str(num)[9:] == "!button9": self.buttons[2][2] = "X"
				self.check_win(num)
			else:				
				self.playerTurn['text'] = f"Player Turn : {self.playerFirstName.get()}"
				num["text"]= "O"
				self.defaultPlayer = self.defaultPlayer-1
				if str(num)[9:] == "!button": self.buttons[0][0] = "O"
				if str(num)[9:] == "!button2": self.buttons[0][1] = "O"
				if str(num)[9:] == "!button3": self.buttons[0][2] = "O"

				if str(num)[9:] == "!button4": self.buttons[1][0] = "O"
				if str(num)[9:] == "!button5": self.buttons[1][1] = "O"
				if str(num)[9:] == "!button6": self.buttons[1][2] = "O"

				if str(num)[9:] == "!button7": self.buttons[2][0] = "O"
				if str(num)[9:] == "!button8": self.buttons[2][1] = "O"
				if str(num)[9:] == "!button9": self.buttons[2][2] = "O"
				self.check_win(num)

	def reset_window(self):
		self.btnColumnZero['text'] = ""
		self.btnColumnOne['text'] = ""
		self.btnColumnTwo['text'] = ""

		self.btnColumnZero.grid_forget()
		self.btnColumnOne.grid_forget()
		self.btnColumnTwo.grid_forget()

		self.toeFrame.grid_forget()
		self.playerTurn.grid_forget()
		self.scoreX.grid_forget()
		self.scoreO.grid_forget()
		self.mainFrame.pack(fill=BOTH)

	def show_winner(self, winner):
		if winner == "X":
			showinfo(title=f'Some One Wins',
				message=f"{self.playerFirstName.get()} X Wins")
		else:
			showinfo(title="Some One Wins",
				message=f"{self.playerSecondName.get()} O Wins")
		self.reset_window()

		
	def check_win(self, num):
		check_win_value = self.buttons

		# Horizontal
		if check_win_value[0][0] == check_win_value[0][1] == check_win_value[0][2] and check_win_value[0][1] != 0:
			self.show_winner(check_win_value[0][1])

		if check_win_value[1][0] == check_win_value[1][1] == check_win_value[1][2] and check_win_value[1][1] != 0:
			self.show_winner(check_win_value[1][0])

		if check_win_value[2][0] == check_win_value[2][1] == check_win_value[2][2] and check_win_value[2][1] != 0:
			self.show_winner(check_win_value[2][0])

		# Vertical
		if check_win_value[0][0] == check_win_value[1][0] == check_win_value[2][0] and check_win_value[0][0] != 0:
			self.show_winner(check_win_value[1][0])
		if check_win_value[0][1] == check_win_value[1][1] == check_win_value[2][1] and check_win_value[1][1] != 0:
			self.show_winner(check_win_value[1][1])
		if check_win_value[0][2] == check_win_value[1][2] == check_win_value[2][2] and check_win_value[2][2] != 0:
			self.show_winner(check_win_value[2][2])

		# Cross
		if check_win_value[0][0] == check_win_value[1][1] == check_win_value[2][2] != 0:
			self.show_winner(check_win_value[0][0])
		if check_win_value[0][2] == check_win_value[1][1] == check_win_value[2][0] != 0:
			self.show_winner(check_win_value[2][0])

if __name__ == '__main__': 
	app = Application()
	app.mainloop()
