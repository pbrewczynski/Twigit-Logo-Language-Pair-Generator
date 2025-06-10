#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# svg_styler_ui.py

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk
import io
import os

# --- Import core logic and data ---
try:
    from svg_styler_core import process_svg, COUNTRY_CODES, COUNTRY_NAMES_SORTED, cairosvg
except ImportError:
    # A simple tk root to show the error if core module fails
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror("Initialization Error", "Could not import from svg_styler_core.py.\nPlease ensure it is in the same directory and all its dependencies (like CairoSVG) are installed.")
    exit()

# --- UI Application Class (mostly unchanged, just uses imported functions/data) ---
class SvgStylerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("SVG Leaf Styler")
        self.geometry("800x650")
        self.minsize(650, 550)
        self.last_svg_content = None

        main_paned_window = ttk.PanedWindow(self, orient='horizontal')
        main_paned_window.pack(fill='both', expand=True, padx=10, pady=10)

        controls_frame = ttk.Frame(main_paned_window, width=350)
        main_paned_window.add(controls_frame, weight=1)

        preview_frame = ttk.LabelFrame(main_paned_window, text=" Live Preview ", padding="10")
        main_paned_window.add(preview_frame, weight=2)
        self.preview_label = ttk.Label(preview_frame, text="Enable a leaf to see a preview.")
        self.preview_label.pack(fill='both', expand=True)

        self.controls = {}
        self.controls['Top Leaf'] = self._create_leaf_controls(controls_frame, "Top Leaf")
        ttk.Separator(controls_frame, orient='horizontal').pack(fill='x', pady=10, padx=5)
        self.controls['Right Leaf'] = self._create_leaf_controls(controls_frame, "Right Leaf")

        action_frame = ttk.Frame(controls_frame)
        action_frame.pack(side='bottom', fill='x', pady=(20, 0), padx=5)
        self.save_button = ttk.Button(action_frame, text="Save As...", command=self.save_files, state='disabled')
        self.save_button.pack(side="right")

        self.update_preview()

    def _create_leaf_controls(self, parent, leaf_name):
        frame = ttk.LabelFrame(parent, text=f" {leaf_name} Controls ", padding="10")
        frame.pack(fill="x", expand=True, padx=5, pady=5)

        vars_dict = {
            "enabled": tk.BooleanVar(value=False),
            "country_name": tk.StringVar(),
            "fill_type": tk.StringVar(value="gradient"),
            "direction": tk.StringVar(value="horizontal"),
            "transition": tk.DoubleVar(value=20.0),
            "zoom": tk.DoubleVar(value=100.0),
            "pan_x": tk.DoubleVar(value=0.0),
            "pan_y": tk.DoubleVar(value=0.0)
        }
        
        for var in vars_dict.values():
            var.trace_add("write", lambda *args: self.update_preview())
            
        widgets_dict = {}

        main_controls_frame = ttk.Frame(frame)
        main_controls_frame.pack(fill='x', expand=True)
        enabled_check = ttk.Checkbutton(main_controls_frame, text="Enable this Leaf", variable=vars_dict['enabled'], command=lambda: self.toggle_controls_state(widgets_dict, vars_dict['enabled'].get()))
        enabled_check.grid(row=0, column=0, columnspan=2, sticky='w', pady=(0,10))
        
        ttk.Label(main_controls_frame, text="Country:").grid(row=1, column=0, sticky='w', padx=5, pady=2)
        widgets_dict['country_combo'] = ttk.Combobox(main_controls_frame, textvariable=vars_dict['country_name'], values=COUNTRY_NAMES_SORTED, state="readonly")
        widgets_dict['country_combo'].grid(row=1, column=1, sticky='ew', padx=5, pady=2)
        
        ttk.Label(main_controls_frame, text="Fill Type:").grid(row=2, column=0, sticky='w', padx=5, pady=2)
        widgets_dict['fill_combo'] = ttk.Combobox(main_controls_frame, textvariable=vars_dict['fill_type'], values=["gradient", "flag-svg"], state="readonly")
        widgets_dict['fill_combo'].grid(row=2, column=1, sticky='ew', padx=5, pady=2)
        main_controls_frame.columnconfigure(1, weight=1)
        
        widgets_dict['gradient_frame'] = ttk.Frame(frame)
        widgets_dict['flag_frame'] = ttk.Frame(frame)

        grad_frame = widgets_dict['gradient_frame']
        ttk.Label(grad_frame, text="Direction:").grid(row=0, column=0, sticky='w', padx=5)
        ttk.Combobox(grad_frame, textvariable=vars_dict['direction'], values=["horizontal", "vertical"], state="readonly").grid(row=0, column=1, sticky='ew', padx=5, pady=2)
        ttk.Label(grad_frame, text="Transition:").grid(row=1, column=0, sticky='w', padx=5)
        ttk.Scale(grad_frame, from_=1, to=99, orient='horizontal', variable=vars_dict['transition']).grid(row=1, column=1, sticky='ew', padx=5, pady=5)
        transition_label = ttk.Label(grad_frame, text="20%", width=5)
        transition_label.grid(row=1, column=2, sticky='w', padx=5)
        grad_frame.columnconfigure(1, weight=1)

        flag_frame = widgets_dict['flag_frame']
        ttk.Label(flag_frame, text="Zoom:").grid(row=0, column=0, sticky='w', padx=5)
        ttk.Scale(flag_frame, from_=25, to=400, orient='horizontal', variable=vars_dict['zoom']).grid(row=0, column=1, sticky='ew', padx=5, pady=2)
        zoom_label = ttk.Label(flag_frame, text="100%", width=5)
        zoom_label.grid(row=0, column=2, sticky='w', padx=5)
        ttk.Label(flag_frame, text="Pan X:").grid(row=1, column=0, sticky='w', padx=5)
        ttk.Scale(flag_frame, from_=-100, to=100, orient='horizontal', variable=vars_dict['pan_x']).grid(row=1, column=1, sticky='ew', padx=5, pady=2)
        pan_x_label = ttk.Label(flag_frame, text="0%", width=5)
        pan_x_label.grid(row=1, column=2, sticky='w', padx=5)
        ttk.Label(flag_frame, text="Pan Y:").grid(row=2, column=0, sticky='w', padx=5)
        ttk.Scale(flag_frame, from_=-100, to=100, orient='horizontal', variable=vars_dict['pan_y']).grid(row=2, column=1, sticky='ew', padx=5, pady=2)
        pan_y_label = ttk.Label(flag_frame, text="0%", width=5)
        pan_y_label.grid(row=2, column=2, sticky='w', padx=5)
        flag_frame.columnconfigure(1, weight=1)

        def on_fill_type_change(*args):
            is_gradient = vars_dict['fill_type'].get() == "gradient"
            if is_gradient:
                widgets_dict['gradient_frame'].pack(fill='x', expand=True, pady=(5,0))
                widgets_dict['flag_frame'].pack_forget()
            else:
                widgets_dict['gradient_frame'].pack_forget()
                widgets_dict['flag_frame'].pack(fill='x', expand=True, pady=(5,0))

        def on_slider_change(var, label, suffix): label.config(text=f"{var.get():.0f}{suffix}")
        
        vars_dict['fill_type'].trace_add("write", on_fill_type_change)
        vars_dict['transition'].trace_add("write", lambda *args: on_slider_change(vars_dict['transition'], transition_label, "%"))
        vars_dict['zoom'].trace_add("write", lambda *args: on_slider_change(vars_dict['zoom'], zoom_label, "%"))
        vars_dict['pan_x'].trace_add("write", lambda *args: on_slider_change(vars_dict['pan_x'], pan_x_label, "%"))
        vars_dict['pan_y'].trace_add("write", lambda *args: on_slider_change(vars_dict['pan_y'], pan_y_label, "%"))
        
        vars_dict['widgets'] = widgets_dict
        
        self.toggle_controls_state(widgets_dict, False) 
        on_fill_type_change()
        return vars_dict

    def toggle_controls_state(self, widgets_to_toggle, enabled):
        state = 'normal' if enabled else 'disabled'
        widgets_to_toggle['country_combo'].config(state=state)
        widgets_to_toggle['fill_combo'].config(state=state)
        for w in widgets_to_toggle['gradient_frame'].winfo_children(): w.config(state=state)
        for w in widgets_to_toggle['flag_frame'].winfo_children(): w.config(state=state)

    def update_preview(self):
        params_list = []
        for leaf_name_key in ['Top Leaf', 'Right Leaf']:
            leaf_controls = self.controls[leaf_name_key]
            if leaf_controls['enabled'].get() and leaf_controls['country_name'].get():
                params = {
                    'leaf_name': leaf_name_key.split(" ")[0],
                    'country_code': COUNTRY_CODES[leaf_controls['country_name'].get()],
                    'fill_type': leaf_controls['fill_type'].get(),
                    'direction': leaf_controls['direction'].get(),
                    'transition': leaf_controls['transition'].get(),
                    'zoom': leaf_controls['zoom'].get(),
                    'pan_x': leaf_controls['pan_x'].get(),
                    'pan_y': leaf_controls['pan_y'].get()
                }
                params_list.append(params)
        
        top_params = next((p for p in params_list if p['leaf_name'] == 'Top'), None)
        right_params = next((p for p in params_list if p['leaf_name'] == 'Right'), None)
        
        status, svg_content = process_svg(top_params, right_params)
        
        if not svg_content:
            self.preview_label.config(image=None, text=f"Error generating SVG:\n{status}")
            return

        self.last_svg_content = svg_content
        try:
            if not cairosvg:
                raise RuntimeError("CairoSVG is not installed, cannot render preview.")
            png_data = cairosvg.svg2png(bytestring=svg_content.encode('utf-8'), output_height=400)
            img = Image.open(io.BytesIO(png_data))
            self.photo_image = ImageTk.PhotoImage(img)
            self.preview_label.config(image=self.photo_image, text="")
            self.save_button.config(state='normal' if (top_params or right_params) else 'disabled')
        except Exception as e:
            self.preview_label.config(image=None, text=f"Error rendering preview:\n{e}")
            self.save_button.config(state='disabled')

    def save_files(self):
        if not self.last_svg_content: return
        filepath = filedialog.asksaveasfilename( defaultextension=".svg", filetypes=[("SVG Vector Image", "*.svg"), ("PNG Image", "*.png"), ("All Files", "*.*")], title="Save Logo As..." )
        if not filepath: return
        base_path, _ = os.path.splitext(filepath)
        try:
            with open(f"{base_path}.svg", "w", encoding="utf-8") as f: f.write(self.last_svg_content)
            if not cairosvg:
                raise RuntimeError("CairoSVG is not installed, cannot save PNG.")
            cairosvg.svg2png(bytestring=self.last_svg_content.encode('utf-8'), write_to=f"{base_path}.png", output_width=1200)
            messagebox.showinfo("Success", f"Successfully saved:\n{base_path}.svg\n{base_path}.png")
        except Exception as e:
            messagebox.showerror("Save Error", f"An error occurred while saving files:\n{e}")

if __name__ == "__main__":
    app = SvgStylerApp()
    app.mainloop()