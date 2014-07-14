"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

TESTS = {
    "Basics": [
        {
            "input": [["scout", "super"]],
            "answer": [["scout", "super"]],
            "show": '({"scout", "super"})'
        },
        {
            "input": [['scout', 'hater'], ['planer', 'hater']],
            "answer": [['scout', 'hater'], ['planer', 'hater']],
            "show": "({'hater', 'scout'}, {'planer', 'hater'})",
            "state": {'hater': 'planer', 'planer': 'scout', 'scout': 'hater'}
        },
        {
            "input": [['digger', 'melter'], ['melter', 'planer'], ['digger', 'planer']],
            "answer": [['digger', 'melter'], ['melter', 'planer'], ['digger', 'planer']],
            "show": "({'melter', 'digger'}, {'melter', 'planer'}, {'digger', 'planer'})",
            "state": {'melter': 'planer', 'digger': 'digger', 'planer': 'melter'}
        },
    ],
    "Extra": [
        {
            "input": [['scout', 'driller'], ['scout', 'lister'], ['digger', 'hater'], ['planer', 'lister'],
                      ['super', 'melter']],
            "answer": [['scout', 'driller'], ['scout', 'lister'], ['digger', 'hater'], ['planer', 'lister'],
                       ['super', 'melter']],
            "show": "({'scout', 'driller'}, {'scout', 'lister'}, {'hater', 'digger'}, {'planer', 'lister'},"
                    " {'super', 'melter'})",
            "state": {'planer': 'driller', 'hater': 'digger', 'driller': 'scout', 'digger': 'hater', 'super': 'melter',
                      'melter': 'super', 'scout': 'lister', 'lister': 'planer'}
        },
        {
            "input": [['melter', 'drawer'], ['hammer', 'hater'], ['melter', 'hater'], ['scout', 'planer'],
                      ['driller', 'lister'], ['digger', 'drawer']],
            "answer": [['melter', 'drawer'], ['hammer', 'hater'], ['melter', 'hater'], ['scout', 'planer'],
                       ['driller', 'lister'], ['digger', 'drawer']],
            "show": "({'drawer', 'melter'}, {'hater', 'hammer'}, {'hater', 'melter'}, {'planer', 'scout'},"
                    " {'driller', 'lister'}, {'drawer', 'digger'})",
            "state": {'planer': 'scout', 'hater': 'drawer', 'digger': 'melter', 'driller': 'lister', 'hammer': 'hater',
                      'drawer': 'digger', 'lister': 'driller', 'scout': 'planer', 'melter': 'hammer'}
        },
        {
            "input": [['digger', 'melter'], ['drawer', 'hater'], ['digger', 'hammer'], ['super', 'melter'],
                      ['super', 'lister'], ['super', 'driller'], ['melter', 'hater'], ['driller', 'hater'],
                      ['digger', 'lister'], ['melter', 'drawer'], ['digger', 'drawer'], ['lister', 'hater'],
                      ['planer', 'drawer'], ['scout', 'driller']],
            "answer": [['digger', 'melter'], ['drawer', 'hater'], ['digger', 'hammer'], ['super', 'melter'],
                       ['super', 'lister'], ['super', 'driller'], ['melter', 'hater'], ['driller', 'hater'],
                       ['digger', 'lister'], ['melter', 'drawer'], ['digger', 'drawer'], ['lister', 'hater'],
                       ['planer', 'drawer'], ['scout', 'driller']],
            "show": "({'melter', 'digger'}, {'drawer', 'hater'}, {'hammer', 'digger'}, {'super', 'melter'},"
                    " {'super', 'lister'}, {'super', 'driller'}, {'melter', 'hater'}, {'driller', 'hater'},"
                    " {'lister', 'digger'}, {'melter', 'drawer'}, {'drawer', 'digger'}, {'lister', 'hater'},"
                    " {'planer', 'drawer'}, {'driller', 'scout'})",
            "state": {'melter': 'hater', 'driller': 'scout', 'planer': 'digger', 'digger': 'drawer', 'super': 'driller',
                      'scout': 'super', 'hammer': 'melter', 'drawer': 'planer', 'lister': 'lister', 'hater': 'hammer'}
        },
        {
            "input": [['driller', 'hammer'], ['digger', 'lister'], ['super', 'driller'], ['planer', 'hater'],
                      ['scout', 'melter'], ['digger', 'drawer'], ['melter', 'hammer'], ['digger', 'melter'],
                      ['scout', 'super'], ['planer', 'hammer'], ['melter', 'drawer'], ['scout', 'drawer'],
                      ['scout', 'hater'], ['hammer', 'hater'], ['digger', 'hammer'], ['super', 'melter']],
            "answer": [['driller', 'hammer'], ['digger', 'lister'], ['super', 'driller'], ['planer', 'hater'],
                       ['scout', 'melter'], ['digger', 'drawer'], ['melter', 'hammer'], ['digger', 'melter'],
                       ['scout', 'super'], ['planer', 'hammer'], ['melter', 'drawer'], ['scout', 'drawer'],
                       ['scout', 'hater'], ['hammer', 'hater'], ['digger', 'hammer'], ['super', 'melter']],
            "show": "({'driller', 'hammer'}, {'lister', 'digger'}, {'super', 'driller'}, {'planer', 'hater'},"
                    " {'melter', 'scout'}, {'drawer', 'digger'}, {'melter', 'hammer'}, {'melter', 'digger'},"
                    " {'super', 'scout'}, {'planer', 'hammer'}, {'melter', 'drawer'}, {'drawer', 'scout'},"
                    " {'hater', 'scout'}, {'hammer', 'hater'}, {'hammer', 'digger'}, {'super', 'melter'})",
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
            "answer": [['super', 'melter'], ['digger', 'lister'], ['melter', 'planer'], ['scout', 'digger'],
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
            "show": "({'super', 'melter'}, {'digger', 'lister'}, {'planer', 'melter'}, {'scout', 'digger'},"
                    " {'drawer', 'scout'}, {'hater', 'driller'}, {'lister', 'melter'}, {'super', 'digger'},"
                    " {'planer', 'drawer'}, {'planer', 'lister'}, {'planer', 'super'}, {'super', 'lister'},"
                    " {'scout', 'lister'}, {'super', 'driller'}, {'drawer', 'lister'}, {'drawer', 'hammer'},"
                    " {'hater', 'lister'}, {'super', 'scout'}, {'scout', 'hammer'}, {'hater', 'digger'},"
                    " {'planer', 'hater'}, {'planer', 'digger'}, {'hater', 'hammer'}, {'scout', 'melter'},"
                    " {'planer', 'scout'}, {'driller', 'melter'}, {'hater', 'scout'}, {'hammer', 'melter'},"
                    " {'drawer', 'hater'}, {'lister', 'hammer'}, {'super', 'hater'}, {'digger', 'hammer'},"
                    " {'digger', 'melter'}, {'driller', 'hammer'}, {'drawer', 'melter'}, {'drawer', 'driller'},"
                    " {'digger', 'driller'}, {'planer', 'hammer'}, {'super', 'hammer'}, {'hater', 'melter'},"
                    " {'scout', 'driller'}, {'drawer', 'super'}, {'driller', 'lister'}, {'drawer', 'digger'},"
                    " {'planer', 'driller'})",
            "state": {'planer': 'lister', 'super': 'melter', 'driller': 'drawer', 'digger': 'digger',
                      'hammer': 'hammer', 'hater': 'super', 'drawer': 'driller', 'melter': 'planer', 'scout': 'scout',
                      'lister': 'hater'}
        },
    ]
}
