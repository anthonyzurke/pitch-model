from pybaseball import statcast

data = statcast(start_dt = '2021-04-01', end_dt = '2021-10-04')

data.to_csv('./data/mlb-pitches.csv')
data = pd.read_csv('./data/mlb-pitches.csv')

data.drop(columns = ['Unnamed: 0', 'spin_dir', 'spin_rate_deprecated', 
                     'break_angle_deprecated', 'break_length_deprecated', 
                     'tfs_deprecated', 'tfs_zulu_deprecated', 'umpire', 'sv_id'], inplace = True)

# Drop pitch types Fasball, knuckleball, eephus, and screwball
pitch_values = ['SC', 'EP', 'KN', 'FA', 'CS']
data = data[data.pitch_type.isin(pitch_values) == False]

# Create is_strike column
data['is_strike'] = [1 if x != 'B' else 0 for x in data['type']]
# Create pitch_count column
data['pitch_count'] = data[['balls', 'strikes']].astype(str).agg('-'.join, axis = 1)

data['description'].replace(['blocked_ball', 'foul_tip', 'swinging_strike_blocked', 'foul_bunt'], 
                            ['ball', 'foul', 'swinging_strike', 'foul'], inplace = True)
# Make all events that aren't hits, outs
data['events'].replace(['field_out', 'grounded_into_double_play', 'sac_fly', 'force_out', 'hit_by_pitch', 
                        'field_error', 'fielders_choice', 'fielders_choice_out'], 'out', inplace = True)
# make swing_miss column
data['swing_miss'] = [1 if x == 'swinging_strike' else 0 for x in data['description']]

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