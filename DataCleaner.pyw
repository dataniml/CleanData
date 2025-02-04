import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import tempfile, base64, zlib
import tkinter.simpledialog
from tkinter import messagebox
import datetime
import pandas as pd
import csv

# Console output at startup
print("PassContainer v. 1.0\n2025 © Data Animal")

# Global variables
global column_labels, data_labels, pddata, col_names, filepath
anything_modified = False
filepath = None

# Transparent icon settings
ICON = zlib.decompress(base64.b64decode('eJxjYGAEQgEBBiDJwZDBy'
                                        'sAgxsDAoAHEQCEGBQaIOAg4sDIgACMUj4JRMApGwQgF/ykEAFXxQRc='))
_, ICON_PATH = tempfile.mkstemp()
with open(ICON_PATH, 'wb') as icon_file:
    icon_file.write(ICON)

# Load a CSV file and print the first 10 rows of the data
def load_file():
    global pddata, col_names, filepath, column_labels, data_labels, anything_modified
    try:
        filepath = filedialog.askopenfilename(filetypes=(("CSV files", "*.csv"), ("All files", "*.*")))
        if filepath:
            pddata = pd.read_csv(filepath)
            col_names = list(pddata.columns)
            datacolumns['values'] = col_names

            column_labels = []
            data_labels = []

            canvas = tk.Canvas(root)
            scrollbar_x = tk.Scrollbar(root, orient="horizontal", command=canvas.xview)
            canvas.configure(xscrollcommand=scrollbar_x.set)

            canvas.place(x=0, y=0, width=root.winfo_width(), height=270)
            scrollbar_x.place(x=0, y=270, width=root.winfo_width())

            frame_grid = tk.Frame(canvas)
            canvas.create_window((0, 0), window=frame_grid, anchor=tk.NW)

            col_name_frame = tk.Frame(frame_grid)
            col_name_frame.grid(row=2, columnspan=len(col_names))
            for i, col_name in enumerate(col_names):
                label = tk.Label(col_name_frame, text=col_name)
                label.grid(row=0, column=i, padx=40)
                column_labels.append(label)

            tk.Label(frame_grid).grid(row=3)

            for i in range(min(10, len(pddata))):
                row_labels = []
                for j, col_name in enumerate(col_names):
                    try:
                        text = pddata.iloc[i, j]
                    except IndexError:
                        text = ""
                    label = tk.Label(frame_grid, text=text)
                    label.grid(row=i + 4, column=j, padx=10)
                    row_labels.append(label)
                data_labels.append(row_labels)

            frame_grid.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
            datacolumns.current(0)
            clear_console()
            anything_modified = False
            return pddata
        else:
            return None
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load the file: {e}")
        return None

# Load file, generate the header row and print the first 10 rows of the data
def load_file_with_row():
    global pddata, col_names, filepath, column_labels, data_labels, anything_modified
    try:
        filepath = filedialog.askopenfilename(filetypes=(("CSV files", "*.csv"), ("All files", "*.*")))
        if filepath:
            pddata = pd.read_csv(filepath, header=None)

            default_headers = [str(i + 1) for i in range(len(pddata.columns))]
            pddata.columns = default_headers

            col_names = list(pddata.columns)
            datacolumns['values'] = col_names

            column_labels = []
            data_labels = []

            canvas = tk.Canvas(root)
            scrollbar_x = tk.Scrollbar(root, orient="horizontal", command=canvas.xview)
            canvas.configure(xscrollcommand=scrollbar_x.set)

            canvas.place(x=0, y=0, width=root.winfo_width(), height=270)
            scrollbar_x.place(x=0, y=270, width=root.winfo_width())

            frame_grid = tk.Frame(canvas)
            canvas.create_window((0, 0), window=frame_grid, anchor=tk.NW)

            col_name_frame = tk.Frame(frame_grid)
            col_name_frame.grid(row=2, columnspan=len(col_names))
            for i, col_name in enumerate(col_names):
                label = tk.Label(col_name_frame, text=col_name)
                label.grid(row=0, column=i, padx=40)
                column_labels.append(label)

            tk.Label(frame_grid).grid(row=3)

            for i in range(min(10, len(pddata))):
                row_labels = []
                for j, col_name in enumerate(col_names):
                    try:
                        text = pddata.iloc[i, j]
                    except IndexError:
                        text = ""
                    label = tk.Label(frame_grid, text=text)
                    label.grid(row=i + 4, column=j, padx=10)
                    row_labels.append(label)
                data_labels.append(row_labels)

            frame_grid.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

            datacolumns.current(0)
            clear_console()
            anything_modified = False
            return pddata
        else:
            return None
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load the file: {e}")
        return None

# Update column name and data labels
def update_display():
    global column_labels, data_labels, pddata, col_names

    if pddata is not None:
        col_names = list(pddata.columns)
        datacolumns['values'] = col_names

        for i, col_name in enumerate(col_names):
            if i < len(column_labels):
                column_labels[i].config(text=col_name)

        for i in range(min(10, len(pddata))):
            if i < len(data_labels):
                for j, col_name in enumerate(col_names):
                    if j < len(data_labels[i]):
                        try:
                            text = pddata.iloc[i, j]
                        except IndexError:
                            text = ""
                        data_labels[i][j].config(text=text)

# Save the CSV file as new file
def save_as_file():
    global pddata, anything_modified
    try:
        if 'pddata' in globals() and pddata is not None:
            file = filedialog.asksaveasfile(defaultextension=".csv",
                                            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")])
            if file:
                pddata.to_csv(file.name, index=False)
                file.close()
                console.insert('end', f"Saved as: {file.name}")
                anything_modified = False
        else:
            messagebox.showinfo("Error", "Please load a CSV file first.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save the file: {e}")
        print(f"Error: {e}")

# Save the CSV file
def save_file():
    global pddata, filepath, anything_modified
    try:
        if pddata is not None and filepath is not None:
            pddata.to_csv(filepath, index=False)
            console.insert('end', f"Saved as: {filepath}")
            anything_modified = False
        else:
            messagebox.showinfo("Error", "Please load a CSV file first.")
    except:
        messagebox.showinfo("Error", "Please load a CSV file first.")

# Describe the data on console window
def describe_data():
    if 'pddata' in globals():
        console.insert('end', pddata.describe())
        console.insert('end', "\n\n")
        console.insert('end', pddata.dtypes)
        current_text = console.get("1.0", 'end-1c')
        console.delete("1.0", 'end')
        console.insert('end', current_text[:-13])
    else:
        messagebox.showinfo("Error", "Please load a CSV file first.")

# Describe the selected column on console window
def describe_column():
    if 'pddata' in globals():
        selection_index = datacolumns.current()
        if selection_index != -1:
            try:
                column_name = col_names[selection_index]
                console.insert('end', pddata[column_name].describe())
                console.insert('end', "\n")
            except KeyError:
                console.insert('end', "Column not found.\n")
        else:
            messagebox.showwarning("Warning", "No column selected.")
    else:
        messagebox.showinfo("Error", "Please load a CSV file first.")

# Print all data on console window
def all_data():
    if 'pddata' in globals():
        console.insert('end', pddata.to_string())
        console.insert('end', "\n")
    else:
        messagebox.showinfo("Error", "Please load a CSV file first.")

# Clear the console window
def clear_console():
    console.delete(1.0, 'end')

# Rename the selected column
def rename_column():
    global pddata, anything_modified
    if pddata is not None:
        try:
            selection_index = datacolumns.current()
            if selection_index != -1:
                old_name = pddata.columns[selection_index]
                root.withdraw()
                new_name = tkinter.simpledialog.askstring("Rename Column", f"Rename '{old_name}' to:")
                root.deiconify()
                if new_name:
                    pddata = pddata.rename(columns={old_name: new_name})
                    anything_modified = True
                    update_display()
            else:
                messagebox.showwarning("Warning", "No column selected.")
        except Exception as e:
            messagebox.showerror("Error", f"Error renaming column: {e}")
    else:
        messagebox.showinfo("Error", "Please load a CSV file first.")

# Remove the selected column
def drop_column():
    global pddata, column_labels, data_labels, col_names, anything_modified
    if pddata is not None:
        try:
            selection_index = datacolumns.current()
            if selection_index != -1:
                column_name = pddata.columns[selection_index]
                pddata = pddata.drop([column_name], axis=1)

                col_names = list(pddata.columns)
                datacolumns['values'] = col_names

                column_labels[selection_index].grid_forget()
                del column_labels[selection_index]

                for row_labels in data_labels:
                    row_labels[selection_index].grid_forget()
                    del row_labels[selection_index]

                datacolumns.current(0)
                anything_modified = True
                update_display()

            else:
                messagebox.showwarning("Warning", "No column selected.")
        except Exception as e:
            messagebox.showerror("Error", f"Error dropping column: {e}")
    else:
        messagebox.showinfo("Error", "Please load a CSV file first.")

# Describe the selected column on console window
def print_column():
    if 'pddata' in globals():
        selection_index = datacolumns.current()
        if selection_index != -1:
            try:
                column_name = col_names[selection_index]
                data_to_print = pddata[column_name]
                console.insert('end', data_to_print.to_string())
                console.insert('end', "\n")
            except KeyError:
                console.insert('end', "Column not found.\n")
        else:
            messagebox.showwarning("Warning", "No column selected.")
    else:
        messagebox.showinfo("Error", "Please load a CSV file first.")

# Remove the selected row
def remove_row():
    global pddata, anything_modified, column_labels, data_labels
    if pddata is not None:
        try:
            row_index_str = toBeChanged.get()
            if row_index_str:
                row_index = int(row_index_str)

                if 0 <= row_index < len(pddata):
                    pddata = pddata.drop(row_index)
                    pddata = pddata.reset_index(drop=True)

                    for label in data_labels[row_index]:
                        label.grid_forget()
                    del data_labels[row_index]

                    anything_modified = True
                    update_display()
                    console.insert('end', f"Row {row_index} removed.\n")
                else:
                    messagebox.showerror("Error", "Invalid row number.")
            else:
                messagebox.showerror("Error", "Row number is empty.")

        except ValueError:
            messagebox.showerror("Error", "Invalid row number. Must be an integer.")
        except IndexError:
            messagebox.showerror("Error", "Invalid row number.")
        except Exception as e:
            messagebox.showerror("Error", f"Error removing row: {e}")
    else:
        messagebox.showinfo("Error", "Please load a CSV file first.")

# Check the data for duplicates
def check_duplicates():
    global pddata
    if 'pddata' in globals():
        duplicates_in_any_column = (pddata.duplicated().sum() > 0)
        if duplicates_in_any_column:
            duplicates = pddata[pddata.duplicated(keep=False)]
            console.insert('end', "Duplicates found:\n")
            for index, row in duplicates.iterrows():
                console.insert('end', f"Row {index}: {row.to_string()}\n")
            console.insert('end', "\n")
        else:
            messagebox.showinfo("", "No duplicates found.")
    else:
        messagebox.showinfo("Error", "Please load a CSV file first.")

# Drop the duplicate rows
def remove_duplicates():
    global pddata, anything_modified
    if 'pddata' in globals():
        duplicates = pddata[pddata.duplicated(keep='first')]
        if not duplicates.empty:
            pddata = pddata.drop_duplicates(keep='first')
            anything_modified = True
            update_display()
            console.insert('end', "Duplicates removed.\n")
        else:
            messagebox.showinfo("", "No duplicates")
    else:
        messagebox.showinfo("Error", "Please load a CSV file first.")

# Check the data for NaN values
def check_nanvalues():
    global pddata
    if 'pddata' in globals():
        nan_columns = []

        for column in pddata.columns:
            if pddata[column].isnull().any():
                nan_columns.append(column)

        if nan_columns:
            console.insert('end', "NaN-values found from: \n")
            for column in nan_columns:
                console.insert('end', (f"- {column}\n"))
        else:
            messagebox.showinfo("", "No NaN-values found")
    else:
        messagebox.showinfo("Error", "Please load a CSV file first.")

# Replace the NaN values with the user input
def replace():
    global pddata, anything_modified
    if pddata is not None:
        try:
            column_index = datacolumns.current()
            if column_index != -1:
                column_name = col_names[column_index]
                replacement_value = converted.get()
                if replacement_value == "":
                    replacement_value = "0"
                pddata[column_name] = pddata[column_name].fillna(replacement_value)
                anything_modified = True
                update_display()
                console.insert('end', f"NaN values in '{column_name}' replaced with '{replacement_value}'.\n")
            else:
                messagebox.showwarning("Warning", "No column selected.")
        except Exception as e:
            messagebox.showerror("Error", f"Error replacing NaN values: {e}")
    else:
        messagebox.showinfo("Error", "Please load a CSV file first.")

# Drop the rows including NaN values for the selected column
def dropnans():
    global pddata, anything_modified
    if pddata is not None:
        try:
            column_index = datacolumns.current()
            if column_index != -1:
                column_name = col_names[column_index]
                original_rows = len(pddata)
                pddata = pddata.dropna(subset=[column_name])
                dropped_rows = original_rows - len(pddata)
                anything_modified = True
                update_display()
                console.insert('end', f"{dropped_rows} rows with NaN values in '{column_name}' dropped.\n")
            else:
                messagebox.showwarning("Warning", "No column selected.")
        except Exception as e:
            messagebox.showerror("Error", f"Error dropping NaN rows: {e}")
    else:
        messagebox.showinfo("Error", "Please load a CSV file first.")

# Replace the NaN values with the column mean
def nanstomean():
    global pddata, anything_modified
    if pddata is not None:
        try:
            column_index = datacolumns.current()
            if column_index != -1:
                column_name = col_names[column_index]
                if pddata[column_name].dtype in ['int64', 'float64']:
                    mean_value = pddata[column_name].mean()
                    pddata[column_name] = pddata[column_name].fillna(mean_value)
                    anything_modified = True
                    update_display()
                    console.insert('end', f"NaN values in '{column_name}' replaced with mean ({mean_value}).\n")
                else:
                    messagebox.showerror("Error", "Selected column is not numeric.")
            else:
                messagebox.showwarning("Warning", "No column selected.")
        except Exception as e:
            messagebox.showerror("Error", f"Error replacing NaN values with mean: {e}")
    else:
        messagebox.showinfo("Error", "Please load a CSV file first.")

# Change the datatype of selected column
def change_dtype():
    global pddata, anything_modified
    try:
        column_index = datacolumns.current()
        if column_index != -1:
            column_name = col_names[column_index]
            if datatypes.current() == 0:
                pddata[column_name] = pddata[column_name].astype('int64')
            elif datatypes.current() == 1:
                pddata[column_name] = pddata[column_name].astype('float64')
            elif datatypes.current() == 2:
                pddata[column_name] = pddata[column_name].astype('object')
            elif datatypes.current() == 3:
                 pddata[column_name] = pd.to_datetime(pddata[column_name], errors='coerce')
            elif datatypes.current() == 4:
                 pddata[column_name] = pddata[column_name].astype('boolean')
            anything_modified = True
            update_display()
            console.insert('end', f"Data type of '{column_name}' changed.\n")
        else:
            messagebox.showwarning("Warning", "No column selected.")

    except (KeyError, TypeError, ValueError) as e:
        messagebox.showerror("Error", f"Error: {e}")

# Change the selected value of given row with user input
def update_row():
    global pddata, anything_modified
    try:
        column_index = datacolumns.current()
        if column_index != -1:
            column_name = col_names[column_index]
            try:
                x = int(toBeChanged.get())
                y = toChange.get()
                if x in pddata.index:
                    pddata.loc[x, column_name] = y
                    update_display()
                    anything_modified = True
                    console.insert('end', f"Value on row {x} and column '{column_name}' is updated.\n")
                else:
                    messagebox.showerror("Error", "Invalid row number.")
            except ValueError:
                messagebox.showerror("Error", "Invalid row number. Must be integer.")
        else:
            messagebox.showwarning("Warning", "No column selected.")

    except (KeyError, IndexError) as e:
        messagebox.showerror("Error", f"Error updating row: {e}")

# Ensure quitting if changes were made
def on_closing():
    if anything_modified:
        if messagebox.askyesno(title="Quit?", message="You have unsaved project.\nReally quit without saving?"):
            root.destroy()
    else:
        root.destroy()

# Window settings
root = tk.Tk()
root.title("Data Cleaner")
root.geometry("1150x700")
root.iconbitmap(default=ICON_PATH)
root.resizable(False, False)
root.protocol("WM_DELETE_WINDOW", on_closing)

# Menubar settings
menubar = tk.Menu(root)
root.config(menu = menubar)
filemenu = tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="Open", command=load_file)
filemenu.add_command(label="Open and generate headers", command=load_file_with_row)
filemenu.add_command(label="Save", command=save_file)
filemenu.add_command(label="Save as", command=save_as_file)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=on_closing)

# Widget settings
clearbtn = tk.Button(text="Clear console", command=clear_console)
describebtn = tk.Button(text="Describe data", command=describe_data)
dupbtn = tk.Button(text="Duplicates", command=check_duplicates)
removedupbtn = tk.Button(text="Remove duplicates", command=remove_duplicates)
nanbtn = tk.Button(text="NaN values", command=check_nanvalues)
printColumnbtn = tk.Button(text="Print column data", command=print_column)
dtypebtn = tk.Button(text="Change column datatype", command=change_dtype)
alldatabtn = tk.Button(text="Print all data", command=all_data)
describe_columnbtn = tk.Button(text="Describe", command=describe_column)
console = tk.Text()
label_datacolumns = tk.Label(text="Columns")
datacolumns = ttk.Combobox(state="readonly")
datatypes = ttk.Combobox(state="readonly", width=5, values=["int", "float", "string", "datetime", "Boolean"])
datatypes.current(0)
renamecolumn = tk.Button(text="Rename", command=rename_column)
dropcolumn = tk.Button(text="Remove", command=drop_column)
changeLabel = tk.Label(text="Change row")
toBeChanged = tk.Entry(width=3)
toLabel1 = tk.Label(text="to")
toLabel2 = tk.Label(text="to")
nanconversion = tk.Button(text="Replace NaN values", command=replace)
withLabel = tk.Label(text="with")
converted = tk.Entry(width=3)
converted.insert(0, "0")
nandrop = tk.Button(text="Drop rows with NaN values", command=dropnans)
nantomean = tk.Button(text="Replace NaN values with column mean", command=nanstomean)
toChange = tk.Entry()
updateRowbtn = tk.Button(text="Update row", command=update_row)
removeRowbtn = tk.Button(text="Delete row", command=remove_row)

# Widget placements
changeLabel.place(x=680, y=370)
toBeChanged.place(x=755, y=370)
toLabel1.place(x=785, y=370)
toChange.place(x=810, y=370)
updateRowbtn.place(x=945, y=365)
removeRowbtn.place(x=1025, y=365)
describebtn.place(x=680, y=450)
alldatabtn.place(x=770, y=450)
clearbtn.place(x=680, y=660)
dupbtn.place(x=680, y=490)
removedupbtn.place(x=755, y=490)
dtypebtn.place(x=680, y=410)
toLabel2.place(x=835, y=411)
datatypes.place(x=860, y=413)
nanbtn.place(x=680, y=530)
nanconversion.place(x=760, y=530)
withLabel.place(x=885, y=533)
converted.place(x=920, y=534)
nandrop.place(x=680, y=570)
nantomean.place(x=680, y=610)
label_datacolumns.place(x=680, y=300)
datacolumns.place(x=680, y=325)
renamecolumn.place(x=830, y=322)
dropcolumn.place(x=890, y=322)
printColumnbtn.place(x=950, y=322)
describe_columnbtn.place(x=1060, y=322)
console.place(x=20, y=300)

if __name__ == '__main__':
    root.mainloop()