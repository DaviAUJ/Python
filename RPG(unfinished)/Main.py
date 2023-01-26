import combat

main = combat.Char("Pigas", 200, 30, 50, "Rock")
enemy = combat.Char("Liiv", 300, 20, 40, "Scissors")

combat.call_battle(main, enemy)
