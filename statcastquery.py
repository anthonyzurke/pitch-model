from pybaseball import statcast

data = statcast(start_dt = '2021-04-01', end_dt = '2021-10-04')

data.to_csv('../data/mlb-pitches.csv')
data = pd.read_csv('../data/mlb-pitches.csv')

data.drop(columns = ['spin_dir', 'spin_rate_deprecated', 'break_angle_deprecated', 
                     'break_length_deprecated', 'tfs_deprecated', 'tfs_zulu_deprecated', 
                     'umpire', 'sv_id', 'game_type','pitcher.1', 'fielder_2.1', 
                     'fielder_3', 'fielder_4', 'fielder_5', 'fielder_6', 'fielder_7', 
                     'fielder_8', 'fielder_9', 'bat_score', 'fld_score', 'post_bat_score', 
                     'post_fld_score'], inplace = True)

# Add bauer_units column
data['bauer_units'] = data['release_spin_rate'] / data['release_speed']

# Drop pitch types Fasball, knuckleball, eephus, and screwball
pitch_values = ['SC', 'EP', 'KN', 'FA', 'CS']
data = data[data.pitch_type.isin(pitch_values) == False]

# Create is_strike column
data['is_strike'] = [1 if x != 'B' else 0 for x in data['type']]
# Create pitch_count column
data['pitch_count'] = data[['balls', 'strikes']].astype(str).agg('-'.join, axis = 1)

data['description'].replace(['blocked_ball', 'foul_tip', 'missed_bunt' 'swinging_strike_blocked', 'foul_bunt', 
                             'bunt_foul_tip', 'foul_pitchout'], 
                            ['ball', 'foul', 'swinging_strike', 'swinging_strike','foul', 'foul'], inplace = True)
# Make all events that aren't hits, outs
data['events'].replace(['grounded_into_double_play', 'sac_fly', 'force_out', 'hit_by_pitch', 
                        'fielders_choice', 'fielders_choice_out'], 'field_out', inplace = True)
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

data.to_csv('../data/mlb-pitches.csv')

# Clean data for modeling

pitch = pd.read_csv('../data/mlb-pitches.csv', index_col = [0])
pitch = pitch[['player_name', 'p_throws', 'pitch_type','release_speed', 'release_spin_rate', 'spin_axis', 
               'pfx_-x', 'pfx_z', 'bauer_units', 'effective_speed', 'release_pos_x', 'release_pos_z', 
               'release_extension', 'release_pos_y', 'plate_-x', 'plate_x', 'plate_z', 'type', 'balls','strikes', 
               'pitch_count', 'stand', 'description', 'events', 'hit_distance_sc', 'launch_speed','launch_angle', 
               'launch_speed_angle', 'estimated_ba_using_speedangle', 'estimated_woba_using_speedangle', 
               'woba_value', 'woba_denom', 'babip_value', 'iso_value','at_bat_number', 'pitch_number', 
               'inning', 'inning_topbot', 'home_score', 'away_score', 'post_home_score', 'post_away_score', 
               'on_1b', 'on_2b', 'on_3b', 'outs_when_up', 'delta_run_exp']].copy()

#Rename some columns
col_dict = {
    'release_speed': 'velo',
    'release_spin_rate': 'spin_rate',
    'launch_speed': 'exit_velo',
    'estimated_ba_using_speedangle': 'xba',
    'estimated_woba_using_speedangle': 'xwobacon'
}
pitch.rename(columns = col_dict, inplace = True)
pitch.to_csv('../data/model-pitches.csv')

# Run Expectany Table

# 2010-2015 Run Expectancy
# matrix = [[0, 0, 0, 0, 0.481], [1, 0, 0, 0, 0.859], [0, 1, 0, 0, 1.100], [1, 1, 0, 0, 1.437], 
#           [0, 0, 1, 0, 1.350], [1, 0, 1, 0, 1.784], [0, 1, 1, 0, 1.964], [1, 1, 1, 0, 2.292], 
#           [0, 0, 0, 1, 0.254], [1, 0, 0, 1, 0.509], [0, 1, 0, 1, 0.664], [1, 1, 0, 1, 0.884], 
#           [0, 0, 1, 1, 0.950], [1, 0, 1, 1, 1.130], [0, 1, 1, 1, 1.376], [1, 1, 1, 1, 1.541],
#           [0, 0, 0, 2, 0.098], [1, 0, 0, 2, 0.224], [0, 1, 0, 2, 0.319], [1, 1, 0, 2, 0.429], 
#           [0, 0, 1, 2, 0.353], [1, 0, 1, 2, 0.478], [0, 1, 1, 2, 0.580], [1, 1, 1, 2, 0.752]]

# 2019 Run Expectancy
matrix = [[0, 0, 0, 0, 0.544], [1, 0, 0, 0, 0.935], [0, 1, 0, 0, 1.147], [1, 1, 0, 0, 1.537], 
          [0, 0, 1, 0, 1.369], [1, 0, 1, 0, 1.759], [0, 1, 1, 0, 1.971], [1, 1, 1, 0, 2.362],
          [0, 0, 0, 1, 0.298], [1, 0, 0, 1, 0.564], [0, 1, 0, 1, 0.713], [1, 1, 0, 1, 0.979], 
          [0, 0, 1, 1, 0.953], [1, 0, 1, 1, 1.219], [0, 1, 1, 1, 1.368], [1, 1, 1, 1, 1.634],
          [0, 0, 0, 2, 0.115], [1, 0, 0, 2, 0.242], [0, 1, 0, 2, 0.339], [1, 1, 0, 2, 0.467], 
          [0, 0, 1, 2, 0.391], [1, 0, 1, 2, 0.518], [0, 1, 1, 2, 0.615], [1, 1, 1, 2, 0.743]]

re = pd.DataFrame(matrix, columns = ['on_1b', 'on_2b', 'on_3b', 'outs_when_up', 're'])
re.to_csv('../data/run_expectancy_table.csv')

# wOBA by Count

count_woba = [['0-0', 0.331], ['0-1', 0.281], ['0-2', 0.207], ['1-0', 0.374], ['1-1', 0.313], ['1-2', 0.233], 
              ['2-0', 0.444], ['2-1', 0.372], ['2-2', 0.282], ['3-0', 0.588], ['3-1', 0.488], ['3-2', 0.387]]

woba_value = pd.DataFrame(count_woba, columns = ['pitch_count', 'count_woba_value'])
woba_value.to_csv('../data/count_woba_value.csv')