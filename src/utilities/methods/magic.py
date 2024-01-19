import time
from status_socket import StatusSocket
import utilities.api.item_ids_dict as item_dict
import pytweening
from utilities.random_util import truncated_normal_sample

def highAlch(self, item: str, api_s: StatusSocket):
    id = item_dict[item.upper]
    slots = api_s.get_inv_item_indices(id)
    
    self.log_msg(f"High Alching Item: {item}...")
    self.mouse.move_to(self.win.cp_tab(6), mouseSpeed='medium')
    self.mouse.click()
    time.sleep(0.5)

    for slot in slots:
        self.mouse.move_to(self.win.spellbook_normal(36), mouseSpeed='medium')
        self.mouse.click()
        time.sleep(0.5)

        p = self.win.inventory_slots[slot].random_point()
        self.mouse.move_to(
            (p[0], p[1]),
            mouseSpeed="fastest",
            knotsCount=1,
            offsetBoundaryY=40,
            offsetBoundaryX=40,
            tween=pytweening.easeInOutQuad,
        )
        self.mouse.click()
        LOWER_BOUND_CLICK = 3
        UPPER_BOUND_CLICK = 5
        AVERAGE_CLICK = 4
        time.sleep(truncated_normal_sample(LOWER_BOUND_CLICK, UPPER_BOUND_CLICK, AVERAGE_CLICK))