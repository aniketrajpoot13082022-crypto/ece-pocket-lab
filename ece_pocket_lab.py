import tkinter as tk
from tkinter import ttk, messagebox

# ECE Pocket Lab - a beginner-friendly electronics toolkit
# Runs in Thonny with Python's built-in tkinter library.

BG = "#10141D"
PANEL = "#191F2B"
PANEL_LIGHT = "#222B3A"
TEXT = "#F2F5FA"
MUTED = "#A7B3C6"
GREEN = "#72E3B1"
BLUE = "#75B9FF"
RED = "#FF8585"

root = tk.Tk()
root.title("ECE Pocket Lab | Electronics Toolkit")
root.geometry("900x700")
root.minsize(760, 620)
root.configure(bg=BG)

style = ttk.Style()

try:
    style.theme_use("clam")
except tk.TclError:
    pass

style.configure(
    "TNotebook",
    background=BG,
    borderwidth=0
)

style.configure(
    "TNotebook.Tab",
    background=PANEL_LIGHT,
    foreground=TEXT,
    padding=(18, 10),
    font=("Arial", 10, "bold"),
    borderwidth=0
)

style.map(
    "TNotebook.Tab",
    background=[("selected", GREEN)],
    foreground=[("selected", BG)]
)

style.configure(
    "TCombobox",
    fieldbackground=PANEL_LIGHT,
    background=PANEL_LIGHT,
    foreground=TEXT,
    arrowcolor=TEXT,
    padding=6
)

style.map(
    "TCombobox",
    fieldbackground=[("readonly", PANEL_LIGHT)],
    foreground=[("readonly", TEXT)]
)


def make_label(parent, text, size=11, color=TEXT, bold=False):
    return tk.Label(
        parent,
        text=text,
        bg=parent.cget("bg"),
        fg=color,
        font=("Arial", size, "bold" if bold else "normal")
    )


def make_entry(parent, default="", width=24):
    entry = tk.Entry(
        parent,
        width=width,
        bg=PANEL_LIGHT,
        fg=TEXT,
        insertbackground=TEXT,
        relief="flat",
        font=("Arial", 11),
        highlightthickness=1,
        highlightbackground="#354154",
        highlightcolor=GREEN
    )

    entry.insert(0, default)
    entry.configure(highlightthickness=1)

    return entry


def make_button(parent, text, command, color=GREEN):
    return tk.Button(
        parent,
        text=text,
        command=command,
        bg=color,
        fg=BG,
        activebackground="#B2F5D8",
        activeforeground=BG,
        relief="flat",
        padx=16,
        pady=9,
        font=("Arial", 10, "bold"),
        cursor="hand2"
    )


def make_card(parent, title, subtitle=None):
    card = tk.Frame(
        parent,
        bg=PANEL,
        padx=20,
        pady=18,
        highlightthickness=1,
        highlightbackground="#2B3547"
    )

    make_label(
        card, title, 14, GREEN, True
    ).pack(anchor="w")

    if subtitle:
        make_label(
            card, subtitle, 10, MUTED
        ).pack(anchor="w", pady=(5, 12))
    else:
        tk.Frame(
            card, bg=PANEL, height=12
        ).pack()

    return card


def add_field(parent, label_text, default=""):
    field = tk.Frame(parent, bg=PANEL)

    make_label(
        field, label_text, 10, MUTED, True
    ).pack(anchor="w", pady=(0, 6))

    entry = make_entry(field, default)
    entry.pack(anchor="w", fill="x")

    return field, entry


def parse_positive(entry, field_name, allow_zero=False):
    raw = entry.get().strip()

    try:
        value = float(raw)
    except ValueError:
        raise ValueError(
            f"Enter a valid number for {field_name}."
        )

    if value < 0 or (value == 0 and not allow_zero):
        raise ValueError(
            f"{field_name} must be "
            f"{'zero or greater' if allow_zero else 'greater than zero'}."
        )

    return value


def format_ohms(value):
    if value >= 1_000_000:
        return f"{value / 1_000_000:.3g} MΩ"

    if value >= 1_000:
        return f"{value / 1_000:.3g} kΩ"

    return f"{value:.4g} Ω"


# ============================================================
# HEADER
# ============================================================

header = tk.Frame(root, bg=BG, padx=26, pady=20)
header.pack(fill="x")

left_header = tk.Frame(header, bg=BG)
left_header.pack(side="left", fill="x", expand=True)

make_label(
    left_header,
    "ECE POCKET LAB",
    22,
    GREEN,
    True
).pack(anchor="w")

make_label(
    left_header,
    "A mini electronics toolkit for engineering students",
    10,
    MUTED
).pack(anchor="w", pady=(4, 0))

tk.Label(
    header,
    text="PROJECT 02  •  PYTHON",
    bg=PANEL_LIGHT,
    fg=BLUE,
    padx=12,
    pady=7,
    font=("Arial", 9, "bold")
).pack(side="right", anchor="n")


notebook = ttk.Notebook(root)

notebook.pack(
    fill="both",
    expand=True,
    padx=22,
    pady=(0, 20)
)


# ============================================================
# TAB 1: OHM'S LAW CALCULATOR
# ============================================================

ohms_tab = tk.Frame(
    notebook,
    bg=BG,
    padx=18,
    pady=18
)

notebook.add(ohms_tab, text="  Ohm's Law  ")

make_label(
    ohms_tab,
    "01  /  OHM'S LAW CALCULATOR",
    14,
    TEXT,
    True
).pack(anchor="w")

make_label(
    ohms_tab,
    "Choose what you want to find, then enter the other two values.",
    10,
    MUTED
).pack(anchor="w", pady=(5, 15))


ohms_card = make_card(
    ohms_tab,
    "Calculate a circuit value",
    "All values should use the units shown."
)

ohms_card.pack(fill="x", pady=(0, 14))


mode_row = tk.Frame(ohms_card, bg=PANEL)
mode_row.pack(fill="x", pady=(0, 15))

make_label(
    mode_row,
    "I want to calculate:",
    10,
    MUTED,
    True
).pack(side="left", padx=(0, 12))


mode_var = tk.StringVar(value="Voltage (V)")

mode_combo = ttk.Combobox(
    mode_row,
    textvariable=mode_var,
    state="readonly",
    width=20,
    values=[
        "Voltage (V)",
        "Current (A)",
        "Resistance (Ω)"
    ]
)

mode_combo.pack(side="left")


fields_row = tk.Frame(ohms_card, bg=PANEL)
fields_row.pack(fill="x")

fields_row.columnconfigure(0, weight=1)
fields_row.columnconfigure(1, weight=1)


field_one_label = tk.StringVar()
field_two_label = tk.StringVar()


make_label(
    fields_row,
    "INPUT 1",
    9,
    MUTED,
    True
).grid(row=0, column=0, sticky="w", pady=(0, 4))


input_one_title = tk.Label(
    fields_row,
    text="Current (A)",
    bg=PANEL,
    fg=TEXT,
    font=("Arial", 10)
)

input_one_title.grid(
    row=1,
    column=0,
    sticky="w",
    pady=(0, 7)
)


input_one = make_entry(fields_row, "0.02")

input_one.grid(
    row=2,
    column=0,
    sticky="ew",
    padx=(0, 14),
    ipady=5
)


make_label(
    fields_row,
    "INPUT 2",
    9,
    MUTED,
    True
).grid(row=0, column=1, sticky="w", pady=(0, 4))


input_two_title = tk.Label(
    fields_row,
    text="Resistance (Ω)",
    bg=PANEL,
    fg=TEXT,
    font=("Arial", 10)
)

input_two_title.grid(
    row=1,
    column=1,
    sticky="w",
    pady=(0, 7)
)


input_two = make_entry(fields_row, "220")

input_two.grid(
    row=2,
    column=1,
    sticky="ew",
    ipady=5
)


ohms_result = tk.Label(
    ohms_tab,
    text="Your answer will appear here.",
    bg=PANEL_LIGHT,
    fg=TEXT,
    font=("Arial", 12, "bold"),
    padx=16,
    pady=16,
    anchor="w",
    justify="left"
)

ohms_result.pack(fill="x", pady=(0, 12))


def change_ohms_mode(_event=None):
    mode = mode_var.get()

    defaults = {
        "Voltage (V)": (
            "Current (A)",
            "Resistance (Ω)",
            "0.02",
            "220"
        ),

        "Current (A)": (
            "Voltage (V)",
            "Resistance (Ω)",
            "5",
            "220"
        ),

        "Resistance (Ω)": (
            "Voltage (V)",
            "Current (A)",
            "5",
            "0.02"
        )
    }

    label1, label2, default1, default2 = defaults[mode]

    input_one_title.config(text=label1)
    input_two_title.config(text=label2)

    input_one.delete(0, tk.END)
    input_one.insert(0, default1)

    input_two.delete(0, tk.END)
    input_two.insert(0, default2)

    ohms_result.config(
        text="Enter your values and press Calculate.",
        fg=TEXT
    )


def calculate_ohms():
    try:
        a = parse_positive(
            input_one,
            input_one_title.cget("text")
        )

        b = parse_positive(
            input_two,
            input_two_title.cget("text")
        )

        mode = mode_var.get()

        if mode == "Voltage (V)":
            current = a
            resistance = b

            answer = current * resistance

            result_text = (
                f"Voltage = {answer:.4g} V\n"
                f"Power = {current ** 2 * resistance:.4g} W\n"
                f"Formula: V = I × R"
            )

        elif mode == "Current (A)":
            voltage = a
            resistance = b

            answer = voltage / resistance

            result_text = (
                f"Current = {answer:.4g} A\n"
                f"Power = {voltage ** 2 / resistance:.4g} W\n"
                f"Formula: I = V ÷ R"
            )

        else:
            voltage = a
            current = b

            answer = voltage / current

            result_text = (
                f"Resistance = {format_ohms(answer)}\n"
                f"Power = {voltage * current:.4g} W\n"
                f"Formula: R = V ÷ I"
            )

        ohms_result.config(
            text=result_text,
            fg=GREEN
        )

    except ValueError as error:
        messagebox.showerror(
            "Check your input",
            str(error)
        )


make_button(
    ohms_card,
    "Calculate  →",
    calculate_ohms
).pack(anchor="w", pady=(16, 0))

mode_combo.bind(
    "<<ComboboxSelected>>",
    change_ohms_mode
)


# ============================================================
# TAB 2: LED RESISTOR CALCULATOR
# ============================================================

led_tab = tk.Frame(
    notebook,
    bg=BG,
    padx=18,
    pady=18
)

notebook.add(led_tab, text="  LED Resistor  ")

make_label(
    led_tab,
    "02  /  LED RESISTOR CALCULATOR",
    14,
    TEXT,
    True
).pack(anchor="w")

make_label(
    led_tab,
    "Estimate a series resistor to help protect an LED from excessive current.",
    10,
    MUTED
).pack(anchor="w", pady=(5, 15))


led_card = make_card(
    led_tab,
    "LED circuit inputs",
    "Use volts (V) for voltage and milliamps (mA) for LED current."
)

led_card.pack(fill="x", pady=(0, 14))


led_fields = tk.Frame(led_card, bg=PANEL)
led_fields.pack(fill="x")

for i in range(3):
    led_fields.columnconfigure(i, weight=1)


_, supply_entry = add_field(
    led_fields,
    "SUPPLY VOLTAGE (V)",
    "5"
)

supply_entry.master.grid(
    row=0,
    column=0,
    sticky="ew",
    padx=(0, 10)
)


_, led_voltage_entry = add_field(
    led_fields,
    "LED VOLTAGE (V)",
    "2"
)

led_voltage_entry.master.grid(
    row=0,
    column=1,
    sticky="ew",
    padx=5
)


_, led_current_entry = add_field(
    led_fields,
    "LED CURRENT (mA)",
    "20"
)

led_current_entry.master.grid(
    row=0,
    column=2,
    sticky="ew",
    padx=(10, 0)
)


led_result = tk.Label(
    led_tab,
    text="Your resistor recommendation will appear here.",
    bg=PANEL_LIGHT,
    fg=TEXT,
    font=("Arial", 11, "bold"),
    padx=16,
    pady=16,
    anchor="w",
    justify="left"
)

led_result.pack(fill="x", pady=(0, 10))


def next_e12(value):
    # Find the next E12 preferred resistor value
    # that is not below the calculation.

    series = [
        1.0, 1.2, 1.5, 1.8,
        2.2, 2.7, 3.3, 3.9,
        4.7, 5.6, 6.8, 8.2
    ]

    for exponent in range(-2, 10):
        for number in series:
            candidate = number * (10 ** exponent)

            if candidate >= value:
                return candidate

    return value


def calculate_led():
    try:
        supply = parse_positive(
            supply_entry,
            "Supply voltage"
        )

        led_v = parse_positive(
            led_voltage_entry,
            "LED voltage",
            allow_zero=True
        )

        current_ma = parse_positive(
            led_current_entry,
            "LED current"
        )

        if supply <= led_v:
            raise ValueError(
                "Supply voltage must be higher than the LED voltage."
            )

        current_a = current_ma / 1000

        drop = supply - led_v

        required_r = drop / current_a

        recommended_r = next_e12(required_r)

        actual_current_ma = (
            drop / recommended_r
        ) * 1000

        resistor_power = (
            drop ** 2
        ) / recommended_r

        safe_power = resistor_power * 2

        ratings = [
            0.125,
            0.25,
            0.5,
            1,
            2,
            5,
            10
        ]

        rating = next(
            (
                r for r in ratings
                if r >= safe_power
            ),
            10
        )

        led_result.config(
            text=(
                f"Calculated resistance: "
                f"{format_ohms(required_r)}\n"

                f"Suggested standard resistor: "
                f"{format_ohms(recommended_r)}\n"

                f"Estimated LED current with suggested resistor: "
                f"{actual_current_ma:.2f} mA\n"

                f"Resistor power dissipation: "
                f"{resistor_power:.3f} W\n"

                f"Suggested power rating: at least "
                f"{rating:g} W "
                f"(includes a simple safety margin)\n\n"

                "Note: This is an estimate. "
                "Check the LED datasheet and circuit conditions."
            ),
            fg=GREEN
        )

    except ValueError as error:
        messagebox.showerror(
            "Check your input",
            str(error)
        )


make_button(
    led_card,
    "Find resistor  →",
    calculate_led
).pack(anchor="w", pady=(16, 0))


# ============================================================
# TAB 3: RESISTOR COLOUR-CODE DECODER
# ============================================================

color_tab = tk.Frame(
    notebook,
    bg=BG,
    padx=18,
    pady=18
)

notebook.add(
    color_tab,
    text="  Colour Code  "
)

make_label(
    color_tab,
    "03  /  RESISTOR COLOUR-CODE DECODER",
    14,
    TEXT,
    True
).pack(anchor="w")

make_label(
    color_tab,
    "Pick the four bands on a common 4-band resistor to decode its value.",
    10,
    MUTED
).pack(anchor="w", pady=(5, 15))


color_card = make_card(
    color_tab,
    "Choose the colour bands",
    "Band 1 and Band 2 are digits, Band 3 is the multiplier, and Band 4 is tolerance."
)

color_card.pack(fill="x", pady=(0, 12))


COLOR_HEX = {
    "Black": "#111111",
    "Brown": "#795548",
    "Red": "#F44336",
    "Orange": "#FF9800",
    "Yellow": "#FFEB3B",
    "Green": "#4CAF50",
    "Blue": "#2196F3",
    "Violet": "#9C27B0",
    "Grey": "#9E9E9E",
    "White": "#F5F5F5",
    "Gold": "#D4AF37",
    "Silver": "#C0C0C0",
    "No band": PANEL_LIGHT
}


DIGITS = {
    name: i
    for i, name in enumerate([
        "Black",
        "Brown",
        "Red",
        "Orange",
        "Yellow",
        "Green",
        "Blue",
        "Violet",
        "Grey",
        "White"
    ])
}


MULTIPLIERS = {
    "Black": 1,
    "Brown": 10,
    "Red": 100,
    "Orange": 1_000,
    "Yellow": 10_000,
    "Green": 100_000,
    "Blue": 1_000_000,
    "Violet": 10_000_000,
    "Grey": 100_000_000,
    "White": 1_000_000_000,
    "Gold": 0.1,
    "Silver": 0.01
}


TOLERANCES = {
    "Brown": 1,
    "Red": 2,
    "Green": 0.5,
    "Blue": 0.25,
    "Violet": 0.1,
    "Grey": 0.05,
    "Gold": 5,
    "Silver": 10,
    "No band": 20
}


color_fields = tk.Frame(color_card, bg=PANEL)
color_fields.pack(fill="x")

for i in range(4):
    color_fields.columnconfigure(i, weight=1)


vars_by_band = [
    tk.StringVar(value="Brown"),
    tk.StringVar(value="Black"),
    tk.StringVar(value="Red"),
    tk.StringVar(value="Gold")
]


band_options = [
    list(DIGITS.keys()),
    list(DIGITS.keys()),
    list(MULTIPLIERS.keys()),
    list(TOLERANCES.keys())
]


band_titles = [
    "BAND 1",
    "BAND 2",
    "MULTIPLIER",
    "TOLERANCE"
]


combos = []


for index in range(4):
    col = tk.Frame(color_fields, bg=PANEL)

    col.grid(
        row=0,
        column=index,
        sticky="ew",
        padx=(0 if index == 0 else 5, 5)
    )

    make_label(
        col,
        band_titles[index],
        9,
        MUTED,
        True
    ).pack(anchor="w", pady=(0, 6))

    combo = ttk.Combobox(
        col,
        state="readonly",
        textvariable=vars_by_band[index],
        values=band_options[index],
        width=12
    )

    combo.pack(fill="x")

    combos.append(combo)


resistor_canvas = tk.Canvas(
    color_card,
    height=82,
    bg=PANEL,
    highlightthickness=0
)

resistor_canvas.pack(
    fill="x",
    pady=(16, 0)
)


def draw_resistor(*_args):
    resistor_canvas.delete("all")

    resistor_canvas.create_line(
        25, 41, 155, 41,
        fill="#B7C2D2",
        width=5
    )

    resistor_canvas.create_line(
        325, 41, 455, 41,
        fill="#B7C2D2",
        width=5
    )

    resistor_canvas.create_rectangle(
        130, 21, 350, 61,
        fill="#D6B77A",
        outline="#B7945D",
        width=2
    )

    x_positions = [
        164,
        210,
        256,
        302
    ]

    for pos, variable in zip(
        x_positions,
        vars_by_band
    ):
        shade = COLOR_HEX.get(
            variable.get(),
            "#111111"
        )

        outline = (
            "#EDEDED"
            if variable.get() in (
                "White",
                "Silver",
                "Yellow",
                "Gold"
            )
            else shade
        )

        resistor_canvas.create_rectangle(
            pos, 21,
            pos + 18, 61,
            fill=shade,
            outline=outline,
            width=1
        )


def decode_resistor():
    try:
        band1, band2, multiplier, tolerance = [
            var.get()
            for var in vars_by_band
        ]

        digits = (
            DIGITS[band1] * 10
            + DIGITS[band2]
        )

        resistance = (
            digits * MULTIPLIERS[multiplier]
        )

        tolerance_percent = TOLERANCES[tolerance]

        low = resistance * (
            1 - tolerance_percent / 100
        )

        high = resistance * (
            1 + tolerance_percent / 100
        )

        color_result.config(
            text=(
                f"Resistance: "
                f"{format_ohms(resistance)} "
                f"± {tolerance_percent:g}%\n"

                f"Possible range: "
                f"{format_ohms(low)} to "
                f"{format_ohms(high)}\n"

                "Reading direction: digits → multiplier → tolerance"
            ),
            fg=GREEN
        )

    except (KeyError, ValueError):
        messagebox.showerror(
            "Check bands",
            "Choose a valid colour for each band."
        )


for variable in vars_by_band:
    variable.trace_add(
        "write",
        draw_resistor
    )


draw_resistor()


make_button(
    color_card,
    "Decode resistance  →",
    decode_resistor
).pack(anchor="w", pady=(16, 0))


color_result = tk.Label(
    color_tab,
    text="Choose the bands, then press Decode resistance.",
    bg=PANEL_LIGHT,
    fg=TEXT,
    font=("Arial", 11, "bold"),
    padx=16,
    pady=16,
    anchor="w",
    justify="left"
)

color_result.pack(fill="x")


# ============================================================
# FOOTER
# ============================================================

footer = tk.Label(
    root,
    text=(
        "Built for learning • Always verify real circuit designs "
        "before connecting components."
    ),
    bg=BG,
    fg=MUTED,
    font=("Arial", 9)
)

footer.pack(pady=(0, 12))


# ============================================================
# START THE APPLICATION
# ============================================================

root.mainloop()