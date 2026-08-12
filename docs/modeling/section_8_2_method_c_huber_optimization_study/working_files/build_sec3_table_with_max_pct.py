import sys

headers = [
    'Huber Threshold (`delta`)', 'eta_low', 'C0_single (h^-1)', 'C0_dual (h^-1)', '`k`', '`p`',
    '`Mean_dT` (mins)', '`MAE_T` (mins)', '`RMSE_T` (mins)', 'Max Error (mins)', 'Max Error (%)', 'Boundary Status'
]
alignments = [':---:'] * len(headers)

rows = [
    ['**`0.0` (Pure MAE)**',   '`0.9673`', '`0.4029`', '`4.7127`', '`1.0371`', '`0.2261`', '`-3.37`', '**`8.79`**', '`13.36`', '`37.07`', '`+52.6%`', 'OK (Interior)'],
    ['**`0.5`**',               '`0.9673`', '`0.4034`', '`4.6212`', '`1.0333`', '`0.2221`', '`-3.52`', '**`8.77`**', '`13.43`', '`37.30`', '`+51.3%`', 'OK (Interior)'],
    ['**`1.0`**',               '`0.9674`', '`0.4032`', '`4.6944`', '`1.0387`', '`0.2245`', '`-3.34`', '**`8.78`**', '`13.35`', '`37.05`', '`+52.3%`', 'OK (Interior)'],
    ['**`2.5`**',               '`0.9676`', '`0.4026`', '`4.8238`', '`1.0482`', '`0.2299`', '`-3.01`', '**`8.81`**', '`13.22`', '`36.57`', '`+54.5%`', 'OK (Interior)'],
    ['**`5.0`**',               '`0.9679`', '`0.4021`', '`4.9126`', '`1.0576`', '`0.2347`', '`-2.69`', '**`8.84`**', '`13.10`', '`36.12`', '`+56.5%`', 'OK (Interior)'],
    ['**`7.5`**',               '`0.9681`', '`0.4012`', '`4.9815`', '`1.0686`', '`0.2429`', '`-2.28`', '**`8.89`**', '`12.96`', '`35.52`', '`+59.6%`', 'OK (Interior)'],
    ['**`10.0`**',              '`0.9682`', '`0.3997`', '`4.9985`', '`1.0778`', '`0.2531`', '`-1.87`', '**`8.96`**', '`12.84`', '`34.95`', '`+63.2%`', 'OK (Interior)'],
    ['**`15.0`**',              '`0.9683`', '`0.3965`', '`5.0235`', '`1.0943`', '`0.2735`', '`-1.10`', '**`9.18`**', '`12.68`', '`33.87`', '`+70.5%`', 'OK (Interior)'],
    ['**`20.0` (Primary)**',    '`0.9687`', '`0.3943`', '`5.0649`', '`1.1188`', '`0.2893`', '`-0.13`', '**`9.41`**', '`12.55`', '`32.55`', '`+77.6%`', 'OK (Interior)'],
    ['**`30.0`**',              '`0.9692`', '`0.3933`', '`5.1037`', '`1.1437`', '`0.2993`', '`+0.78`', '**`9.65`**', '`12.49`', '`31.33`', '`+83.4%`', 'OK (Interior)'],
    ['**`50.0`**',              '`0.9692`', '`0.3933`', '`5.1049`', '`1.1444`', '`0.2996`', '`+0.81`', '**`9.66`**', '`12.49`', '`31.29`', '`+83.6%`', 'OK (Interior)'],
    ['**`100.0` (MSE-like)**',  '`0.9692`', '`0.3933`', '`5.1048`', '`1.1444`', '`0.2996`', '`+0.81`', '**`9.66`**', '`12.49`', '`31.29`', '`+83.6%`', 'OK (Interior)']
]

col_widths = [len(h) for h in headers]
for r in rows:
    for i, val in enumerate(r):
        col_widths[i] = max(col_widths[i], len(val))

header_str = '| ' + ' | '.join(headers[i].ljust(col_widths[i]) for i in range(len(headers))) + ' |'
align_cells = [':' + '-' * (col_widths[i] - 2) + ':' for i in range(len(headers))]
align_str = '| ' + ' | '.join(align_cells) + ' |'

lines_out = [header_str, align_str]
for r in rows:
    lines_out.append('| ' + ' | '.join(r[i].ljust(col_widths[i]) for i in range(len(r))) + ' |')

res_text = '\n'.join(lines_out)
with open(r"c:\Users\Ion\.gemini\antigravity\scratch\smartphone_db\docs\modeling\section_8_2_method_c_huber_optimization_study\working_files\sec3_table_audited.md", "w", encoding="utf-8") as f:
    f.write(res_text)

print("Built audited Section 3 table successfully.")
