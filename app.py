import gradio as gr
import random
import pandas as pd

# ============================ LINEAR SEARCH (DISTINCT DESIGN) ============================

# generate unsorted list
def generate_list(size=15):
    LOWER_BOUND = 1
    UPPER_BOUND = 200
    return random.sample(range(LOWER_BOUND, UPPER_BOUND + 1), int(size))

# clean, simple linear search (no binary-style variables)
def linear_search(data_list, target):
    steps = []

    for step, (idx, value) in enumerate(zip(range(len(data_list)), data_list), start=1):
        if value == target:
            steps.append([step, idx, value, "MATCH ✅ — stop searching"])
            return idx, steps
        else:
            steps.append([step, idx, value, "Not match → continue"])

    steps.append([len(data_list) + 1, "-", "-", "Reached end → NOT FOUND ❌"])
    return -1, steps

# ============================ UI HELPERS ============================

def update_search(target, current_list):
    if not current_list:
        return "Generate a list first.", pd.DataFrame()

    try:
        target = int(target)
    except:
        return "Enter a valid integer.", pd.DataFrame()

    index, steps_log = linear_search(current_list, target)

    if index != -1:
        result_msg = f"### Found at position {index} ✅"
    else:
        result_msg = f"### Value {target} not found ❌"

    df = pd.DataFrame(steps_log, columns=["Step", "Index Checked", "Value", "Result"])
    return result_msg, df


def create_new_list_ui():
    new_list = generate_list()
    return new_list, f"🎲 List: {new_list}"

# ============================ UI ============================

with gr.Blocks() as demo:
    gr.Markdown("""
    # 🔎 Linear Search Explorer
    This demo shows how linear search scans each element one-by-one.
    """)

    state = gr.State([])

    with gr.Row():
        gen_btn = gr.Button("Generate List")
        list_view = gr.Markdown("Click to generate list")

    with gr.Row():
        target_input = gr.Number(label="Target")
        search_btn = gr.Button("Search")

    result = gr.Markdown("Waiting...")

    table = gr.Dataframe(
        headers=["Step", "Index Checked", "Value", "Result"],
        interactive=False
    )

    gen_btn.click(create_new_list_ui, None, [state, list_view])
    search_btn.click(update_search, [target_input, state], [result, table])


if __name__ == "__main__":
    demo.launch()
