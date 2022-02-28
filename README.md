# Pitch Model

# Data Dictionary

|Feature           |Description                                |Dataset        |Type    |
|---               |--                                         |---            |---     |
|pitch_type        |Type of pitch from Statcast                |model-pitches  |object  |
|velo              |out-of-hand pitch velocity                 |model-pitches  |float64 |
|spin_rate         |Spin rate of pitch tracked by Statcast     |model-pitches  |float64 |
|spin_axis         |The Spin Axis in the 2D X-Z plane in degrees from 0 to 360, such that 180 represents a pure backspin fastball and 0 degrees represents a pure topspin (12-6) curveball |model-pitches | float64
|pfx_-x            |Horizontal movement in feet from the pitchers's perspective | model-pitches |float64
|pfx_z             |Vertical movement in feet from the catcher's perpsective    |model-pitches |float64
|bauer_units       |spin rate / velocity           |model-pitches |float64
|effective_speed   |Derived speed based on the the extension of the pitcher's release  |model-pitches |int64
|release_pos_x  |Horizontal Release Position of the ball measured in feet from the catcher's perspective|model-pitches |float64 |
|release_pos_z  |Vertical Release Position of the ball measured in feet from the catcher's perspective |model-pitches  |float64 |
|release_extension      |Release extension of pitch in feet as tracked by Statcast   |model-pitches  |float64 |
|release_pos_y     |Release position of pitch measured in feet from the catcher's perspective  |model-pitches  |float64 |
|swing_miss          |If the result of the pitch is a swing and miss 1 if not 0 | model-pitches |float64
|delta_run_exp         |The change in Run Expectancy before the Pitch and after the Pitch |model-pitches |float64
|hit_distance_sc       |Projected hit distance of the batted ball    |model-pitches |float64
|exit_velo   |Exit velocity of the batted ball as tracked by Statcast  |model-pitches |int64
|launch_angle     |Launch angle of the batted ball as tracked by Statcast |model-pitches |float64
|launch_speed_angle |Launch speed/angle 1: Weak 2: Topped 3: Under 4: Flare/Burner 5: Solid Contact 6: Barrel |model-pitches  |float64 |
|xba   |Estimated Batting Avg based on launch angle and exit velocity |model-pitches  |float64 |
|xwoba |Estimated wOBA based on launch angle and exit velocity |model-pitches  |float64 |
|woba_value            |wOBA value based on result of play | model-pitches |float64
|woba_denom             |wOBA denominator based on result of play    |model-pitches |float64
|babip_value       |BABIP value based on result of play   |model-pitches |float64
|iso_value   |ISO value based on result of play |model-pitches |float64