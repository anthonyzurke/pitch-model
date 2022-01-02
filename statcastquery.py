from pybaseball import statcast

data = statcast(start_dt = '2021-04-01', end_dt = '2021-10-04')

data.to_csv('./data/mlb-pitches.csv')
data = pd.read_csv('./data/mlb-pitches.csv')

data.drop(columns = ['Unnamed: 0', 'spin_dir', 'spin_rate_deprecated', 
                     'break_angle_deprecated', 'break_length_deprecated', 
                     'tfs_deprecated', 'tfs_zulu_deprecated', 'umpire', 'sv_id'], inplace = True)

# pitch_count: combine balls and strikes (as string)
data['count'] = data[['balls', 'strikes']].astype(str).agg('-'.join, axis = 1)

# Switch from catcher's perspective to pitcher's perspective
# Catcher's POV: (plate_x, plate_z)
# Pitcher's POV: (plate_-x, plate_z)
data['plate_-x'] = -data['plate_x']
# Switch HB to perspective of pitcher
# Catcher's POV: (pfx_x, pfx_z)
# Pitcher's POV: (pfx_-x, pfx_z)
data['pfx_-x'] = -data['pfx_x']

# HB and VB in feet should be in inches (*12)
data['pfx_x'] = 12 * data['pfx_x']
data['pfx_-x'] = 12 * data['pfx_-x']
data['pfx_z'] = 12 * data['pfx_z']


data.to_csv('./data/mlb-pitches.csv')