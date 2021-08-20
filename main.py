def stage_reset():

    blocks.fill(AIR, world(-5, 5, 13), world(4, 7, 22))
    blocks.fill(SOUL_SAND, world(-5, 6, 13), world(4, 6, 22))
    
    x = randint(1, 10) -5
    z = randint(1, 10) + 13
    blocks.place(SOUL_SAND, world(x, 5, z))

def user_init():
    player.execute("give @s netherite_sword 1")
    player.execute("give @s bow 1")
    player.execute('give @s skull 128 1 {"minecraft:can_place_on":{"blocks":["soul_sand"]}}')
    player.execute("give @s netherite_helmet 1")
    player.execute("give @s netherite_chestplate 1")
    player.execute("give @s netherite_leggings 1")
    player.execute("give @s netherite_boots 1")
    player.execute("give @s arrow 64")

player.on_chat("stage-reset", stage_reset)
player.on_chat("user-init", user_init)
