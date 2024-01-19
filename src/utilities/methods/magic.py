import pyautogui as pag
import time

from model.runelite_bot import RuneLiteBot, RuneLiteWindow

def highAlch(self, item: str):
    # Remove this win
    win: RuneLiteWindow = None

    # win.cp_tabs
    # self.log_msg(f"High Alching Item: {item}...")
    # self.mouse.move_to(self.win.cp_tab(6), mouseSpeed='medium')
    # pag.click()
    # time.sleep(0.5)

    # Figure out how to find the spell icon. This doesn't work
    # self.mouse.move_to(self.win.teleport_menu_search(), mouseSpeed='medium')
    # pag.click()
    # time.sleep(1)
    # result = self.win.teleport_menu_search_result()
    # no_result_rgb = pag.pixel(result.x, result.y)
    # pag.typewrite(location, interval=0.05)

    # time.sleep(1.5)
    # new_result = self.win.teleport_menu_search_result()
    # if no_result_rgb == pag.pixel(new_result.x, new_result.y):
    #     self.log_msg(f"No results found for {location}.")
    #     return False
    # self.mouse.move_to(new_result, mouseSpeed='medium')
    # pag.click()
    # self.log_msg("Teleport successful.")
    # return True