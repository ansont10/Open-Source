init python:
    class PlayerStats:
        def __init__(self):
            # starting money for testing
            self.currency = 100
            self.charm = 0
            self.affection = 0

    # global player instance for the shop to use
    player = PlayerStats()

    class ItemShop:
        def __init__(self):
            # boolean flags to track purchases
            self.owns_charm_compiler = False
            self.owns_debuggers_toolkit = False
            self.owns_git_checkout = False
            
            self.cache_cleaner_purchases = 0
            self.cache_cleaner_max = 3
            
            self.message = "Welcome to the item shop. Select an item to buy."

        def buy_item(self, item_name, price):
            if player.currency < price:
                self.message = "Not enough currency."
                return

            # item purchasing logic
            if item_name == "Charm Compiler":
                if self.owns_charm_compiler:
                    self.message = "You already own the Charm Compiler."
                else:
                    player.currency -= price
                    self.owns_charm_compiler = True
                    player.charm += 10
                    self.message = "Bought Charm Compiler! Charm +10."

            elif item_name == "Cache Cleaner":
                if self.cache_cleaner_purchases >= self.cache_cleaner_max:
                    self.message = "Maximum Cache Cleaners purchased."
                else:
                    player.currency -= price
                    self.cache_cleaner_purchases += 1
                    player.affection += 20
                    self.message = "Bought Cache Cleaner! Affection +20."

            elif item_name == "Debugger's Toolkit":
                if self.owns_debuggers_toolkit:
                    self.message = "You already own the Debugger's Toolkit."
                else:
                    player.currency -= price
                    self.owns_debuggers_toolkit = True
                    self.message = "Bought Debugger's Toolkit!"

            elif item_name == "Git Checkout":
                if self.owns_git_checkout:
                    self.message = "You already own Git Checkout."
                else:
                    player.currency -= price
                    self.owns_git_checkout = True
                    self.message = "Bought Git Checkout!"

    # initialize shop instance
    shop = ItemShop()

# ui implementation
screen item_shop_ui():
    modal True
    frame:
        xalign 0.5 yalign 0.5
        vbox:
            spacing 15
            text "Item Shop" size 40 bold True xalign 0.5
            text "Currency: [player.currency]" xalign 0.5
            text "[shop.message]" color "#ffcc00" xalign 0.5
            
            null height 10

            hbox:
                spacing 20
                text "Charm Compiler (50c)" 
                if not shop.owns_charm_compiler:
                    textbutton "Buy" action Function(shop.buy_item, "Charm Compiler", 50)
                else:
                    text "SOLD OUT" color "#ff0000"

            hbox:
                spacing 20
                text "Cache Cleaner (30c) [{shop.cache_cleaner_purchases}/3]" 
                if shop.cache_cleaner_purchases < shop.cache_cleaner_max:
                    textbutton "Buy" action Function(shop.buy_item, "Cache Cleaner", 30)
                else:
                    text "SOLD OUT" color "#ff0000"

            hbox:
                spacing 20
                text "Debugger's Toolkit (100c)" 
                if not shop.owns_debuggers_toolkit:
                    textbutton "Buy" action Function(shop.buy_item, "Debugger's Toolkit", 100)
                else:
                    text "SOLD OUT" color "#ff0000"

            hbox:
                spacing 20
                text "Git Checkout (75c)" 
                if not shop.owns_git_checkout:
                    textbutton "Buy" action Function(shop.buy_item, "Git Checkout", 75)
                else:
                    text "SOLD OUT" color "#ff0000"

            null height 20
            textbutton "Close Shop" action Hide("item_shop_ui") xalign 0.5
