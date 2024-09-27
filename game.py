import tkinter
import generetor

WINDOW_BG = 'black'


class Game:
	def __init__(self, rows: int, cols: int) -> None
		self.window = tkinter.Tk()
		self.window.attributes('-fullscreen', True)
		self.window.bind('<Escape>', lambda evemt: self.window.destroy())
		self.window['bg'] = WINDOW_BG
		self.map = generator.Maze(rows, cols).map
		tile_width = self.window.winfo_screenwidth() // cols
		tile_height = self.window.winfo_screenheidht() // rows
		self.tile_size = min(tile_widht, tile_height)
		self.canvas = tkinter.Canvas(
			self.window,
		 	width=self.tile_size * cols,
		 	height=self.tile_size * rows,
		 	heightlightthickness=0
		)

		self.canvas.pack(expend=True)
		self.draw_maze()
		self.window.mainloop()

	def draw_maze(self) -> None:
		row_idx = 0
		for row in self.map:
			col_idx = 0
			for col in row:
				self.canvas.create_rectangle(col_idx, row_idx, col_idx + self.tile_size, row_idx + self.tile_size, outline='')
				col_idx += self.tile_size
			row_idx += self.tile_size
				

class Player:
	def __init__(self) -> None:
		pass


game = Game(11, 33)
