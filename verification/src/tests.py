TESTS = {
    "Rank_01": [
        {
            "input": [["scout", "super"]],
            "state": {'scout': 'super', 'super': 'scout'}
        },
        {
            "input": [['scout', 'hater'], ['planer', 'hater']],
            "state": {'hater': 'planer', 'planer': 'scout', 'scout': 'hater'}
        },
        {
            "input": [['digger', 'melter'], ['melter', 'planer'], ['digger', 'planer']],
            "state": {'melter': 'planer', 'digger': 'digger', 'planer': 'melter'}
        },
        {
            "input": [['scout', 'driller'], ['scout', 'lister'], ['digger', 'hater'], ['planer', 'lister'],
                      ['super', 'melter']],
            "state": {'planer': 'driller', 'hater': 'digger', 'driller': 'scout', 'digger': 'hater', 'super': 'melter',
                      'melter': 'super', 'scout': 'lister', 'lister': 'planer'}
        },
        {
            "input": [['melter', 'drawer'], ['hammer', 'hater'], ['melter', 'hater'], ['scout', 'planer'],
                      ['driller', 'lister'], ['digger', 'drawer']],
            "state": {'planer': 'scout', 'hater': 'drawer', 'digger': 'melter', 'driller': 'lister', 'hammer': 'hater',
                      'drawer': 'digger', 'lister': 'driller', 'scout': 'planer', 'melter': 'hammer'}
        },
        {
            "input": [['digger', 'melter'], ['drawer', 'hater'], ['digger', 'hammer'], ['super', 'melter'],
                      ['super', 'lister'], ['super', 'driller'], ['melter', 'hater'], ['driller', 'hater'],
                      ['digger', 'lister'], ['melter', 'drawer'], ['digger', 'drawer'], ['lister', 'hater'],
                      ['planer', 'drawer'], ['scout', 'driller']],
            "state": {'melter': 'hater', 'driller': 'scout', 'planer': 'digger', 'digger': 'drawer', 'super': 'driller',
                      'scout': 'super', 'hammer': 'melter', 'drawer': 'planer', 'lister': 'lister', 'hater': 'hammer'}
        },
        {
            "input": [['driller', 'hammer'], ['digger', 'lister'], ['super', 'driller'], ['planer', 'hater'],
                      ['scout', 'melter'], ['digger', 'drawer'], ['melter', 'hammer'], ['digger', 'melter'],
                      ['scout', 'super'], ['planer', 'hammer'], ['melter', 'drawer'], ['scout', 'drawer'],
                      ['scout', 'hater'], ['hammer', 'hater'], ['digger', 'hammer'], ['super', 'melter']],
            "state": {'drawer': 'hammer', 'super': 'lister', 'melter': 'melter', 'driller': 'super', 'digger': 'drawer',
                      'planer': 'scout', 'scout': 'planer', 'hammer': 'driller', 'lister': 'digger', 'hater': 'hater'}
        },
        {
            "input": [['super', 'melter'], ['digger', 'lister'], ['melter', 'planer'], ['scout', 'digger'],
                      ['scout', 'drawer'], ['driller', 'hater'], ['melter', 'lister'], ['super', 'digger'],
                      ['planer', 'drawer'], ['planer', 'lister'], ['super', 'planer'], ['super', 'lister'],
                      ['scout', 'lister'], ['super', 'driller'], ['lister', 'drawer'], ['hammer', 'drawer'],
                      ['lister', 'hater'], ['scout', 'super'], ['scout', 'hammer'], ['digger', 'hater'],
                      ['planer', 'hater'], ['digger', 'planer'], ['hammer', 'hater'], ['scout', 'melter'],
                      ['scout', 'planer'], ['melter', 'driller'], ['scout', 'hater'], ['melter', 'hammer'],
                      ['drawer', 'hater'], ['hammer', 'lister'], ['super', 'hater'], ['digger', 'hammer'],
                      ['digger', 'melter'], ['driller', 'hammer'], ['melter', 'drawer'], ['driller', 'drawer'],
                      ['digger', 'driller'], ['planer', 'hammer'], ['super', 'hammer'], ['melter', 'hater'],
                      ['scout', 'driller'], ['super', 'drawer'], ['driller', 'lister'], ['digger', 'drawer'],
                      ['planer', 'driller']],
            "state": {'planer': 'lister', 'super': 'melter', 'driller': 'drawer', 'digger': 'digger',
                      'hammer': 'hammer', 'hater': 'super', 'drawer': 'driller', 'melter': 'planer', 'scout': 'scout',
                      'lister': 'hater'}
        },
    ]
}
