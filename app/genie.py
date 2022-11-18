from app.genie_gui import genie_guis
import time
import threading


genie = genie_guis()
genie.splash_for_genie("./app/imgs/welgenie.png")

time.sleep(0.5)
newgenie = genie_guis()
newgenie.create_window("Genie","400x70")
newgenie.genie_config("#3EB4F1")
newgenie.genie_half_screen(newgenie.genie,400,70)
newgenie.genie_resize(1,0)
newgenie.genie_entry_box(newgenie.genie)
newgenie.genie_protocols("WM_DELETE_WINDOW", newgenie.genie_close)
newgenie.genie_icon(newgenie.genie)
newgenie.end_genie()