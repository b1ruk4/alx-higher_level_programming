#!/usr/bin/python3

if __name__ == "__main__":

    import hidden_4

    names_def = dir(hidden_4)
    for name in names_def:
        if name[:2] != "__":
            print(name)
