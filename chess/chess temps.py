if current_king.side and m == new_cord(current_king, 2, 0):  # short white
    wr2.cords = new_cord(current_king, -1, 0)
    wr2.rect.topleft = ((m[0] - 1) * unit_w, m[1] * unit_h)

if not current_king.side and m == new_cord(current_king, -2, 0):  # long black
    br1.cords = new_cord(current_king, 1, 0)
    br1.rect.topleft = ((m[0] + 1) * unit_w, m[1] * unit_h)

if not current_king.side and m == new_cord(current_king, 2, 0):  # short black
    br2.cords = new_cord(current_king, -1, 0)
    br2.rect.topleft = ((m[0] - 1) * unit_w, m[1] * unit_h)

if current_king.side and m == new_cord(current_king, -2, 0):  # long white
    wr1.cords = new_cord(current_king, 1, 0)
    wr1.rect.topleft = ((m[0] + 1) * unit_w, m[1] * unit_h)