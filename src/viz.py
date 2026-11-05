
# Stapeldiagram 
def bar(ax, x, y, title, xlabel, ylabel):
    ax.bar(x, y)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(True, axis="y")
    return ax

# Linjediagram
def line(ax, x, y, title, xlabel, ylabel):
    ax.plot(x, y, marker="o")
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(True)
    return ax

