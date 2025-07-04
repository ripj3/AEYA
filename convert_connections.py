import json, sys
for path in sys.argv[1:]:
    with open(path) as f:
        data = json.load(f)
    conns = data.get("connections")
    if isinstance(conns, dict):
        changed = False
        new_conns = {}
        for src, value in conns.items():
            if isinstance(value, dict) and 'main' in value and isinstance(value['main'], list):
                main = value['main']
                if main and isinstance(main[0], list):
                    new_conns[src] = main[0]
                    changed = True
                else:
                    new_conns[src] = value
            else:
                new_conns[src] = value
        if changed:
            data['connections'] = new_conns
            with open(path, 'w') as f:
                json.dump(data, f, indent=2)
                f.write('\n')
