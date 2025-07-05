import json
import sys


def convert(path: str) -> None:
    """Normalize connection formats to the nested lists n8n expects."""
    with open(path) as f:
        data = json.load(f)

    conns = data.get("connections")

    # Format 1: list of [src, dst] pairs
    if isinstance(conns, list):
        new_conns: dict[str, dict] = {}
        for pair in conns:
            if not isinstance(pair, list) or len(pair) != 2:
                continue
            src, dst = pair
            entry = new_conns.setdefault(src, {"main": [[]]})
            entry["main"][0].append({"node": dst, "type": "main", "index": 0})
        data["connections"] = new_conns

    # Format 2+: dictionary based
    elif isinstance(conns, dict):
        changed = False
        new_conns = {}
        for src, value in conns.items():
            entry = {"main": [[]]}

            if isinstance(value, dict):
                # Possible n8n or single object
                if "main" in value:
                    main = value["main"]
                else:
                    # treat as single connection object
                    main = value

                if isinstance(main, list):
                    if main and isinstance(main[0], list):
                        entry = {"main": main}
                        if entry != value:
                            changed = True
                    else:
                        entry["main"][0] = main
                        changed = True
                elif isinstance(main, dict):
                    entry["main"][0].append(main)
                    changed = True
                else:
                    # leave entry empty if unknown structure
                    entry = value
            elif isinstance(value, list):
                # List of connection objects
                entry["main"][0] = value
                changed = True
            else:
                entry = value

            new_conns[src] = entry

        if changed or new_conns != conns:
            data["connections"] = new_conns

    if data.get("connections") != conns:
        with open(path, "w") as f:
            json.dump(data, f, indent=2)
            f.write("\n")


if __name__ == "__main__":
    for arg in sys.argv[1:]:
        convert(arg)
