import pyautogui as pag
import time
import item_ids

from model.runelite_bot import RuneLiteWindow

def highAlch(self, item: str, count: int):
    win: RuneLiteWindow = None
    self.log_msg(f"High Alching Item: {item}...")
    self.mouse.move_to(self.win.cp_tab(6), mouseSpeed='medium')
    pag.click()
    time.sleep(0.5)

    for i in range(0, count):
        self.mouse.move_to(self.win.spellbook_normal(36), mouseSpeed='medium')
        pag.click()
        time.sleep(.5)

        #Find item in inv
        id = item_ids[]

    return True