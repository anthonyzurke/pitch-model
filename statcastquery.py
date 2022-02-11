from pybaseball import statcast, statcast_pitcher_spin

data = statcast(start_dt = '2021-04-01', end_dt = '2021-10-04')

data.to_csv('./data/mlb-pitches.csv')
data = pd.read_csv('./data/mlb-pitches.csv')

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

# Clean Dataset
pd.set_option('max_columns', None)
arsenal = pd.read_csv('./data/pitch-arsenal-stats.csv')
arsenal = arsenal.sort_values(by = ['last_name'], ascending = True)
#print(arsenal.shape)

spin = pd.read_csv('./data/spin-direction-pitches.csv')
spin.drop(columns = ['year', 'hawkeye_measured_clock_minutes', 'movement_inferred_clock_minutes'], inplace = True)
spin = spin.sort_values(by = ['last_name'], ascending = True)
spin.rename(columns={'api_pitch_type': 'pitch_type', 'api_pitch_name': 'pitch_name'}, inplace=True)
#print(spin.shape)

df = pd.merge(arsenal, spin, how = 'inner', on = ['player_id', 'pitch_type', 'pitch_type'])
df.drop_duplicates(subset = ['player_id', 'pitch_type'], inplace = True)
df = df[['last_name_x', 'last_name_y', ' first_name_x', 'player_id', 'pitch_hand',
         'pitch_type', 'pitch_name_x', 'pitch_name_y', 'pitches', 'n_pitches', 'pitch_usage',
         'release_speed', 'spin_rate', 'movement_inches', 'active_spin_formatted', 'alan_active_spin_pct', 
         'active_spin', 'hawkeye_measured', 'movement_inferred', 'diff_measured_inferred', 'diff2', 
         'run_value_per_100', 'run_value', 'pa', 'ba', 'slg', 'woba', 'whiff_percent', 'k_percent', 
         'put_away', 'est_ba', 'est_slg', 'est_woba', 'hard_hit_percent', 'diff_measured_inferred_minutes', 
         'hawkeye_measured_clock_hh', 'hawkeye_measured_clock_mm', 'movement_inferred_clock_hh', 
         'movement_inferred_clock_mm', 'diff_clock_hh', 'diff_clock_mm', 'hawkeye_measured_clock_label', 
         'movement_inferred_clock_label', 'diff_clock_label', 'team_name_alt']]
#print(df.shape)

col_dict = {
    'active_spin_formatted': 'spin_eff%', 
}

df.rename(columns = col_dict, inplace = True)
df.to_csv('./data/arsenal-spin.csv')