import os

BASE_DIR = os.path.dirname(__file__)

csv_dir = {
    'calendar': ['boundary', 'equivalence-weak-general', 'equivalence-strong-general', 'equivalence-weak-robust',
                 'equivalent-strong-robust'],
    'triangle': ['boundary', 'equivalence'],
    'commission': ['boundary-input', 'boundary-output'],
    'charge': ['boundary', 'equivalence', 'decision'],
    'sales': ['statement', 'judge', 'condition', 'judge-condition', 'condition-combination'],
}

triangle = {
    'boundary': BASE_DIR + '/q1/triangle-boundary.csv',
    'equivalence': BASE_DIR + '/q1/triangle-equivalent.csv'
}

commission = {
    'boundary-input': BASE_DIR + '/q3/commission-boundary.csv',
    'boundary-output': BASE_DIR + '/q3/commission-boundary-output.csv'
}

charge = {
    'boundary': BASE_DIR + '/q6/charge-boundary.csv',
    'equivalence': BASE_DIR + '/q6/charge-equivalence.csv',
    'decision': BASE_DIR + '/q6/charge-decision.csv',
    'final': BASE_DIR + '/q6/charge.csv'
}

sales = {
    'statement': BASE_DIR + '/q8/sales-statement-cov.csv',
    'judge': BASE_DIR + '/q8/sales-judge-cov.csv',
    'condition': BASE_DIR + '/q8/sales-condition-cov.csv',
    'judge-condition': BASE_DIR + '/q8/sales-judge-condition-cov.csv',
    'condition-combination': BASE_DIR + '/q8/sales-condition-combination-cov.csv'
}

calendar = {
    'boundary': BASE_DIR + '/q1/calendar-boundary.csv',
    'equivalence-weak-general': BASE_DIR + '/q1/calendar-equivalent-weak-general.csv',
    'equivalence-strong-general': BASE_DIR + '/q1/calendar-equivalent-strong-general.csv',
    'equivalence-weak-robust': BASE_DIR + '/q1/calendar-equivalent-weak-robust.csv',
    'equivalence-strong-robust': BASE_DIR + '/q1/calendar-equivalent-strong-robust.csv'
}

csv_dir2 = {
    'triangle': triangle,
    'commission': commission,
    'charge': charge,
    'sales': sales,
}
