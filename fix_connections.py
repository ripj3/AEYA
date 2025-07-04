import json, sys
for path in sys.argv[1:]:
    with open(path) as f:
        data = json.load(f)
    conns = data.get("connections")
    if isinstance(conns, list):
        new_conns = {}
        for pair in conns:
            if not isinstance(pair, list) or len(pair) != 2:
                continue
            src, dst = pair
            src_entry = new_conns.setdefault(src, {"main": [[]]})
            src_entry["main"][0].append({"node": dst, "type": "main", "index": 0})
        data["connections"] = new_conns
        with open(path, 'w') as f:
            json.dump(data, f, indent=2)
            f.write("\n")
