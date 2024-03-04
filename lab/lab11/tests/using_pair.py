test = {
  'name': 'using-pair',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'answer': '5e9484882252923f12097bb0e47f89bb',
          'choices': [
            "Pair('+', Pair('-', Pair(2, Pair(4, Pair(6, Pair(8, nil))))))",
            "Pair('+', Pair(Pair('-', Pair(2, Pair(4))), Pair(6, Pair(8))))",
            'Pair(+, Pair(Pair(-, Pair(2, Pair(4, nil))), Pair(6, Pair(8, nil))))',
            "Pair('+', Pair(Pair('-', Pair(2, Pair(4, nil))), Pair(6, Pair(8, nil))))",
            'None of these'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'Write out the Python expression that returns a `Pair` representing the given expression: (+ (- 2 4) 6 8)'
        },
        {
          'answer': '4481655b9a856f48d68225e9a06ec7f8',
          'choices': [
            '-',
            '+',
            '(',
            '2',
            '6',
            'None of these'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'What is the operator of the call expression?'
        },
        {
          'answer': '2140336f31cbfbc5b302a1b1925091f1',
          'choices': [
            'p',
            'p.first',
            'p.rest',
            'p.rest.first',
            'p.first.rest'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': r"""
          If the `Pair` you constructed in the previous part was bound to the name `p`,
          how would you retrieve the operator?
          """
        },
        {
          'answer': '9d19d47bff432a668c438a672b700ac3',
          'choices': [
            'p',
            'p.first',
            'p.rest',
            'p.rest.first',
            'p.first.rest'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': r"""
          If the `Pair` you constructed was bound to the name `p`, 
          how would you retrieve a list containing all of the operands?
          """
        },
        {
          'answer': 'c328983ff898e7607079d82dc6718233',
          'choices': [
            'p',
            'p.first',
            'p.rest',
            'p.rest.first',
            'p.first.rest'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'How would you retrieve only the first operand?'
        },
        {
          'answer': '3778b12d84d9bfbbfb84155a3e14598e',
          'choices': [
            "'-'",
            "'+'",
            '2',
            '4',
            '-2',
            "Pair('-', Pair(2, Pair(4, nil)))",
            'Pair(2, Pair(4, nil))'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'What is the first operand of the call expression (prior to evaluation)?'
        }
      ],
      'scored': False,
      'type': 'concept'
    }
  ]
}
