#!/usr/bin/env python
# coding: utf-8

# In[1]:


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

