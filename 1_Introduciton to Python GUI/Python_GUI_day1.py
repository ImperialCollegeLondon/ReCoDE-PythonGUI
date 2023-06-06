import dearpygui.dearpygui as dpg
import math

dpg.create_context()
dpg.create_viewport(title='demonstration of dearpygui widgets', width=1000, height=700)

sindatax = []
sindatay = []
for i in range(0, 500):
    sindatax.append(i / 1000)
    sindatay.append(0.5 + 0.5 * math.sin(50 * i / 1000))

def print_me(sender):
    print(f"Menu Item: {sender}")

with dpg.window(label="Window1", width=500, height=700,pos=[0,0]):
    dpg.add_text("Text widget")
    dpg.add_button(label="Button widget")
    dpg.add_input_text(label="Input text widget", default_value="Input text box widgets")
    dpg.add_slider_float(label="Slider widget", default_value=0.273, max_value=1)
    dpg.add_text("Text widget")
    dpg.add_checkbox(label="Checkbox widget - option 1")
    dpg.add_checkbox(label="Checkbox widget - option 2")
    dpg.add_checkbox(label="Checkbox widget - option 3")
    dpg.add_radio_button(["Radio button widget - option 1", "Radio button widget - option 2", "Radio button widget - option 3"], horizontal=False)
   
    with dpg.plot(label="Line Series", height=300, width=400):
    # optionally create legend
        dpg.add_plot_legend()

        # REQUIRED: create x and y axes
        dpg.add_plot_axis(dpg.mvXAxis, label="x")
        dpg.add_plot_axis(dpg.mvYAxis, label="y", tag="y_axis")

        # series belong to a y axis
        dpg.add_line_series(sindatax, sindatay, label="0.5 + 0.5 * sin(x)", parent="y_axis")    

with dpg.window(label="Window2", width=500, height=500,pos=[500,0]):
    with dpg.drawlist(width=500, height=500, tag="_demo_advanced_drawing"):

        with dpg.draw_layer():

            dpg.draw_circle([250, 250], 150, color=[0, 255, 0])
            dpg.draw_circle([250, 250], 200, color=[0, 255, 255])
            with dpg.draw_node(tag="_drawing_sun"):
                dpg.apply_transform(dpg.last_item(), dpg.create_translation_matrix([250, 250]))
                dpg.draw_circle([0, 0], 15, color=[255, 255, 0], fill=[255, 255, 0])
                with dpg.draw_node(tag="_drawing_planet1", user_data=45.0):
                    dpg.apply_transform(dpg.last_item(), dpg.create_rotation_matrix(math.pi*45.0/180.0 , [0, 0, -1])*dpg.create_translation_matrix([150, 0]))
                    dpg.draw_circle([0, 0], 10, color=[0, 255, 0], fill=[0, 255, 0])
                    dpg.draw_circle([0, 0], 25, color=[255, 0, 255])
                    with dpg.draw_node(tag="_drawing_moon1", user_data=45.0):
                        dpg.apply_transform(dpg.last_item(), dpg.create_rotation_matrix(math.pi*45.0/180.0 , [0, 0, -1])*dpg.create_translation_matrix([25, 0]))
                        dpg.draw_circle([0, 0], 5, color=[255, 0, 255], fill=[255, 0, 255])

                with dpg.draw_node(tag="_drawing_planet2", user_data=0.0):
                    dpg.apply_transform(dpg.last_item(), dpg.create_rotation_matrix(math.pi*0.0/180.0 , [0, 0, -1])*dpg.create_translation_matrix([200, 0]))
                    dpg.draw_circle([0, 0], 10, color=[0, 255, 255], fill=[0, 255, 255])
                    dpg.draw_circle([0, 0], 25, color=[255, 0, 255])
                    dpg.draw_circle([0, 0], 45, color=[255, 255, 255])
                    with dpg.draw_node(tag="_drawing_moon2", user_data=45.0):
                        dpg.apply_transform(dpg.last_item(), dpg.create_rotation_matrix(math.pi*45.0/180.0 , [0, 0, -1])*dpg.create_translation_matrix([25, 0]))
                        dpg.draw_circle([0, 0], 5, color=[255, 0, 255], fill=[255, 0, 255])

                    with dpg.draw_node(tag="_drawing_moon3", user_data=120.0):
                        dpg.apply_transform(dpg.last_item(), dpg.create_rotation_matrix(math.pi*120.0/180.0 , [0, 0, -1])*dpg.create_translation_matrix([45, 0]))
                        dpg.draw_circle([0, 0], 5, color=[255, 255, 255], fill=[255, 255, 255])

    def _demo_live_drawing():
        planet_rot1 = dpg.get_item_user_data("_drawing_planet1") + 1.0
        planet_rot2 = dpg.get_item_user_data("_drawing_planet2") + 2.0
        moon_rot1 = dpg.get_item_user_data("_drawing_moon1") + 3.0
        moon_rot2 = dpg.get_item_user_data("_drawing_moon2") + 7.0
        moon_rot3 = dpg.get_item_user_data("_drawing_moon3") + 10.0
        dpg.apply_transform("_drawing_planet1", dpg.create_rotation_matrix(math.pi*planet_rot1/180.0 , [0, 0, -1])*dpg.create_translation_matrix([150, 0]))
        dpg.apply_transform("_drawing_planet2", dpg.create_rotation_matrix(math.pi*planet_rot2/180.0 , [0, 0, -1])*dpg.create_translation_matrix([200, 0]))
        dpg.apply_transform("_drawing_moon1", dpg.create_rotation_matrix(math.pi*moon_rot1/180.0 , [0, 0, -1])*dpg.create_translation_matrix([25, 0]))
        dpg.apply_transform("_drawing_moon2", dpg.create_rotation_matrix(math.pi*moon_rot2/180.0 , [0, 0, -1])*dpg.create_translation_matrix([25, 0]))
        dpg.apply_transform("_drawing_moon3", dpg.create_rotation_matrix(math.pi*moon_rot3/180.0 , [0, 0, 1])*dpg.create_translation_matrix([45, 0]))
        dpg.set_item_user_data("_drawing_planet1", planet_rot1)
        dpg.set_item_user_data("_drawing_planet2", planet_rot2)
        dpg.set_item_user_data("_drawing_moon1", moon_rot1)
        dpg.set_item_user_data("_drawing_moon2", moon_rot2)
        dpg.set_item_user_data("_drawing_moon3", moon_rot3)

    with dpg.item_handler_registry(tag="__demo_item_reg6"):
        dpg.add_item_visible_handler(callback=_demo_live_drawing)
    dpg.bind_item_handler_registry("_demo_advanced_drawing", dpg.last_container())


    size = 5
    demo_verticies = [
            [-size, -size, -size],  # 0 near side
            [ size, -size, -size],  # 1
            [-size,  size, -size],  # 2
            [ size,  size, -size],  # 3
            [-size, -size,  size],  # 4 far side
            [ size, -size,  size],  # 5
            [-size,  size,  size],  # 6
            [ size,  size,  size],  # 7
            [-size, -size, -size],  # 8 left side
            [-size,  size, -size],  # 9
            [-size, -size,  size],  # 10
            [-size,  size,  size],  # 11
            [ size, -size, -size],  # 12 right side
            [ size,  size, -size],  # 13
            [ size, -size,  size],  # 14
            [ size,  size,  size],  # 15
            [-size, -size, -size],  # 16 bottom side
            [ size, -size, -size],  # 17
            [-size, -size,  size],  # 18
            [ size, -size,  size],  # 19
            [-size,  size, -size],  # 20 top side
            [ size,  size, -size],  # 21
            [-size,  size,  size],  # 22
            [ size,  size,  size],  # 23
        ]

    demo_colors = [
            [255,   0,   0, 150],
            [255, 255,   0, 150],
            [255, 255, 255, 150],
            [255,   0, 255, 150],
            [  0, 255,   0, 150],
            [  0, 255, 255, 150],
            [  0,   0, 255, 150],
            [  0, 125,   0, 150],
            [128,   0,   0, 150],
            [128,  70,   0, 150],
            [128, 255, 255, 150],
            [128,   0, 128, 150]
        ]


with dpg.viewport_menu_bar():
    with dpg.menu(label="File"):
        dpg.add_menu_item(label="Save", callback=print_me)
        dpg.add_menu_item(label="Save As", callback=print_me)

        with dpg.menu(label="Settings"):
            dpg.add_menu_item(label="Setting 1", callback=print_me, check=True)
            dpg.add_menu_item(label="Setting 2", callback=print_me)

    dpg.add_menu_item(label="Help", callback=print_me)

    with dpg.menu(label="Widget Items"):
        dpg.add_checkbox(label="Pick Me", callback=print_me)
        dpg.add_button(label="Press Me", callback=print_me)
        dpg.add_color_picker(label="Color Me", callback=print_me)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()