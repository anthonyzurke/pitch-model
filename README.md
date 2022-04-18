# Pitch Model

# Data Dictionary

|Feature           |Description                                |Dataset        |Type    |
|---               |--                                         |---            |---     |
|player_name       |Player's name                              |model-pitches-rv  |object  |
|p_throws          |Hand pitcher throws with                   |model-pitches-rv  |object  |
|pitch_type        |Type of pitch from Statcast                |model-pitches-rv  |object  |
|velo              |Out-of-hand pitch velocity                 |model-pitches-rv  |float64 |
|spin_rate         |Spin rate of pitch tracked by Statcast     |model-pitches-rv  |float64 |
|pfx_x (HB)        |Horizontal movement in feet from the pitchers's perspective | model-pitches-rv |float64
|pfx_z (VB)        |Vertical movement in feet from the catcher's perpsective    |model-pitches-rv |float64
|release_pos_x |Horizontal Release Position of the ball measured in ft from the catcher's perspective|model-pitches-rv |float64 |
|release_pos_z |Vertical Release Position of the ball measured in ft. from the catcher's perspective |model-pitches-rv |float64 |
|release_extension      |Release extension of pitch in feet as tracked by Statcast   |model-pitches-rv  |float64 |
|description          |If the result of the pitch is a swing and miss 1 if not 0 | model-pitches-rv |float64
|events         |If the result of the pitch is a swing and miss 1 if not 0 | model-pitches-rv |float64
|on_1b          |Pre-pitch 1 if player is on 1st, 0 if not | model-pitches-rv |float64
|on_2b          |Pre-pitch 1 if player is on 2nd, 0 if not | model-pitches-rv |float64
|on_3b          |Pre-pitch 1 if player is on 3rd, 0 if not | model-pitches-rv |float64
|outs_when_up          |Pre-pitch number of outs | model-pitches-rv |float64
|is_strike          |1 if strike was thrown 0 if ball was thrown | model-pitches-rv |int64
|is_ball          |1 if ball was thrown 0 if strike was thrown | model-pitches-rv |int64
|final_pitch_ab          |If the last pitch in the at bat was thrown | model-pitches-rv |int64
|out_to_end_inning          |If result of the at bat ends the half inning | model-pitches-rv |int64
|home_runs          |If result of the pitch leads to a run | model-pitches-rv |float64
|away_runs          |If result of the pitch leads to a run | model-pitches-rv |float64
|runs        |If result of the pitch leads to a run  | model-pitches-rv |float64
|re          |Run Expectancy Matrix value based on base-out-state | model-pitches |float64
|re_change   |Change in Run Expectancy based on current base-out-state and the next base-out-state |model-pitches-rv |float64
|re_end_state    |Run Expectancy Matrix value based on the next base-out-state | model-pitches-rv |float64
|re24          |Run Expectancy change based on the outcome of the play | model-pitches-rv |float64
|lin_weight_above_avg  |Avg RE24 of all events | model-pitches-rv |float64
|lin_weight_above_outs  |Avg RE24 of all events with outs = 0 | model-pitches-rv |float64
|woba_scale   |Season total wOBA divided by wOBA denominator | model-pitches-rv |float64
|final_lin_weights  |Linear weight above outs multiplied by wOBA scale| model-pitches-rv |float64
|count_woba_value   |wOBA value based count | model-pitches-rv |float64
|wraa_change   |Change in weighted runs above average based on change in count | model-pitches-rv |float64
|rv   |The run impact of an event based on the runners on base, outs, and the ball and strike count | model-pitches-rv |float64