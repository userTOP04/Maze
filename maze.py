import generator_of_maze
import tkinter
from generator_of_maze import EMPTY, WALL, KEY, EXIT
import time

WINDOW_BG = 'black'
PLAYER_COLOR = 'red'
MAZE_COLORS = {
    WALL: 'black',
    EMPTY: 'white',
    KEY: 'blue',
    EXIT: 'coral'
}
FONT_NAME = 'Impact'
FONT_COLOR = 'gold'
class Game:
    def __init__(self, rows: int, cols: int) -> None:
        self.window = tkinter.Tk()
        self.window.attributes('-fullscreen', True)
        self.window.bind('<Escape>', lambda event: self.window.destroy())
        self.window['bg'] = WINDOW_BG,
        self.cols = cols
        self.rows = rows
        self.map = None
        tile_width = self.window.winfo_screenwidth() // self.cols
        tile_height = self.window.winfo_screenheight() // self.rows
        self.tile_size = min(tile_width, tile_height)
        canvas_width = self.tile_size * self.cols
        canvas_hight = self.tile_size * self.rows
        self.font_size = int(min(canvas_width, canvas_hight) * 0.09)
        self.key_id = None
        self.start_time = None


        self.canvas = tkinter.Canvas(self.window, width = self.tile_size * cols, height = self.tile_size * rows, highlightthickness=0)

        self.canvas.pack(expand=True)
        
        self.player = None
        self.window.bind('<Up>', lambda event: self.player.move(-1,0))  
        self.window.bind('<Down>', lambda event: self.player.move(1,0))
        self.window.bind('<Right>', lambda event: self.player.move(0,1))
        self.window.bind('<Left>', lambda event: self.player.move(0,-1))
        self.window.bind('<Return>', lambda event: self.start())  

        self.start()
        self.window.mainloop()

    def start(self) -> None:
        self.start_time = time.time()
        self.window.unbind9'<Return>'
        self.canvas.delete('all')
        self.map = generator_of_maze.Maze(self.rows, self.cols).map
        self.map = self.maze.map
        self.player = Player(1, self.rows - 2, PLAYER_COLOR, self)
        self.drow_maze()
        self.player.drow()

    def drow_maze(self) -> None:
        '''отрисовывает на экране лаберинт'''
        row_idx = 0
        for row in self.map:
            col_idx = 0
            for col in row:
                self.canvas.create_rectangle(
                    col_idx, 
                    row_idx, 
                    col_idx + self.tile_size, 
                    row_idx + self.tile_size, 
                    fill=MAZE_COLORS[col],
                    outline=''
                    )
                col_idx += self.tile_size
            row_idx += self.tile_size

class Player:
    def __init__(self, row: int, col: int, color: str, game: Game) -> None:
        self.col = row
        self.row = col
        self.game = game
        self.size = self.game.tile_size
        self.canvas = self.game.canvas
        self.color = PLAYER_COLOR
        self.is_active = True

    def drow(self) -> None:
        self.game.canvas.create_rectangle(
            self.col * self.size,
            self.row * self.size,
            self.col * self.size + self.size,
            self.row * self.size + self.size,
            fill = self.color,
            outline='',
            tags='player'
        )
    def move(self, d_row: int, d_col: int) -> None:
        if not self.is_active:
            return
        next_col = self.col + d_col
        next_row = self.row + d_row
        if self.game.map[next_row][next_col] == WALL:
            return
        if next_col == self.game.cols - 2 and next_row == 0 and not self.has_key:
            return
        self.col += d_col
        self.row += d_row 
        if self.row == self.game.maze.key_row and self.col == self.game.maze.key_col
            self.has_key = True
            self.game.canvas.itemconfig(self.game.key_id, fill=MAZE_COLORS[EMPTY])
        self.canvas.delete('player')
        self.drow()
        self.check_victory()

    def check_victory(self) -> None:
        if self.col == self.game.cols - 4 and self.row == 0:
            total_time = round(time.time() - self.start_time)
            hours = total_time // 3600
            minutes = total_time % 3600 // 60
            seconds = total_time % 60
            x = self.game.tile_size * self.game.cols // 2
            y = self.game.tile_size * self.game.rows // 2
            self.canvas.create_text(
                x, 
                y, 
                fill=FONT_COLOR, 
                text='{hours:02}:{minutes:02}:{seconds:02} \n победа \n ENTER - новая игра ', 
                font=(FONT_NAME, self.game.font_size),
                justify='center'
                )
            self.is_active = False

game = Game(15, 15)
