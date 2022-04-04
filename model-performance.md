### model-pitch-quality-lr
**Independent Variables:** Velocity, Spin Rate, HB, VB, Horizontal Release Position, Vertical Release, Release Extension, Horizontal Plate Coords, Vertical Plate Coords 

**Dependent Variable:** Run Value

Model: Linear Regression

Test Data
|Pitch Type           |R2 Score  |MSE       |RMSE       |MAE       |  
|--                   |---       |--        |---        |---       |
|4-Seam - RHP         |0.012     |0.093     |0.304      |0.157     |
|4-Seam - LHP         |0.010     |0.090     |0.301      |0.156     |
|Cutter - RHP         |0.005     |0.092     |0.304      |0.152     |
|Cutter - LHP         |0.004     |0.101     |0.318      |0.162     |
|Sinker - RHP         |0.003     |0.099     |0.315      |0.174     |
|Sinker - LHP         |0.002     |0.093     |0.305      |0.165     |
|Slider - RHP         |0.015     |0.084     |0.290      |0.139     |
|Slider - LHP         |0.015     |0.081     |0.285      |0.139     |
|Curveball - RHP      |0.016     |0.073     |0.270      |0.124     |
|Curveball - LHP      |0.016     |0.067     |0.260      |0.124     |
|Changeup - RHP       |0.017     |0.086     |0.293      |0.150     |
|Changeup - LHP       |0.021     |0.094     |0.306      |0.158     |
|Fastball - RHP       |0.007     |0.096     |0.310      |0.161     |
|Fastball - LHP       |0.004     |0.096     |0.310      |0.162     |
|Breaking Ball - RHP  |0.015     |0.077     |0.277      |0.132     |
|Breaking Ball - LHP  |0.014     |0.076     |0.276      |0.133     |
|Off Speed - RHP      |0.019     |0.082     |0.287      |0.147     |
|Off Speed - LHP      |0.022     |0.095     |0.308      |0.156     |

Original Data
|Pitch Type           |R2 Score  |MSE       |RMSE       |MAE       |  
|--                   |---       |--        |---        |---       |
|4-Seam - RHP         |0.012     |0.095     |0.309      |0.159     |
|4-Seam - LHP         |0.010     |0.094     |0.307      |0.159     |
|Cutter - RHP         |0.004     |0.090     |0.300      |0.150     |
|Cutter - LHP         |0.003     |0.097     |0.312      |0.160     |
|Sinker - RHP         |0.003     |0.096     |0.311      |0.172     |
|Sinker - LHP         |0.002     |0.094     |0.307      |0.168     |
|Slider - RHP         |0.015     |0.081     |0.285      |0.138     |
|Slider - LHP         |0.014     |0.081     |0.284      |0.138     |
|Curveball - RHP      |0.014     |0.068     |0.262      |0.120     |
|Curveball - LHP      |0.016     |0.070     |0.265      |0.126     |
|Changeup - RHP       |0.017     |0.088     |0.296      |0.149     |
|Changeup - LHP       |0.021     |0.090     |0.301      |0.155     |
|Fastball - RHP       |0.007     |0.095     |0.309      |0.161     |
|Fastball - LHP       |0.005     |0.095     |0.308      |0.160     |
|Breaking Ball - RHP  |0.015     |0.077     |0.277      |0.132     |
|Breaking Ball - LHP  |0.014     |0.076     |0.277      |0.132     |
|Off Speed - RHP      |0.019     |0.085     |0.292      |0.148     |
|Off Speed - LHP      |0.021     |0.090     |0.301      |0.155     |


### model-pitch-quality-rf
**Independent Variables:** Velocity, Spin Rate, HB, VB, Horizontal Release Position, Vertical Release, Release Extension, Horizontal Plate Coords, Vertical Plate Coords 

**Dependent Variable:** Run Value

**Model:** Random Forest Regression

Test Data
|Pitch Type           |R2 Score  |MSE       |RMSE     |MAE       |  
|--                   |---       |--        |---      |---       |
|4-Seam - RHP         |-0.024    |0.096     |0.310    |0.177     |
|4-Seam - LHP         |-0.027    |0.094     |0.306    |0.176     |
|Cutter - RHP         |-0.033    |0.095     |0.309    |0.172     |
|Cutter - LHP         |-0.019    |0.103     |0.321    |0.180     |
|Sinker - RHP         |-0.014    |0.101     |0.317    |0.189     |
|Sinker - LHP         |-0.030    |0.096     |0.310    |0.182     |
|Slider - RHP         |-0.007    |0.086     |0.294    |0.161     |
|Slider - LHP         |-0.008    |0.083     |0.288    |0.161     |
|Curveball - RHP      |-0.019    |0.075     |0.274    |0.145     |
|Curveball - LHP      |-0.021    |0.070     |0.264    |0.145     |
|Changeup - RHP       |-0.014    |0.089     |0.298    |0.170     |
|Changeup - LHP       |-0.012    |0.097     |0.311    |0.178     |
|Fastball - RHP       |-0.012    |0.098     |0.313    |0.180     |
|Fastball - LHP       |-0.018    |0.098     |0.313    |0.180     |
|Breaking Ball - RHP  |-0.005    |0.078     |0.280    |0.154     |
|Breaking Ball - LHP  |0.008     |0.077     |0.277    |0.154     |
|Off Speed - RHP      |-0.021    |0.086     |0.293    |0.168     |
|Off Speed - LHP      |-0.017    |0.098     |0.313    |0.179     |

Original Data
|Pitch Type           |R2 Score  |MSE       |RMSE       |MAE     |  
|--                   |---       |--        |---        |---     |
|4-Seam - RHP         |0.644     |0.034     |0.185      |0.095   |
|4-Seam - LHP         |0.644     |0.034     |0.184      |0.095   |
|Cutter - RHP         |0.629     |0.034     |0.183      |0.091   |
|Cutter - LHP         |0.629     |0.036     |0.190      |0.096   |
|Sinker - RHP         |0.633     |0.036     |0.188      |0.099   |
|Sinker - LHP         |0.636     |0.034     |0.186      |0.098   |
|Slider - RHP         |0.634     |0.030     |0.174      |0.085   |
|Slider - LHP         |0.639     |0.030     |0.172      |0.085   |
|Curveball - RHP      |0.624     |0.026     |0.162      |0.076   |
|Curveball - LHP      |0.646     |0.025     |0.159      |0.078   |
|Changeup - RHP       |0.644     |0.032     |0.178      |0.091   |
|Changeup - LHP       |0.632     |0.034     |0.185      |0.094   |
|Fastball - RHP       |0.639     |0.035     |0.186      |0.095   |
|Fastball - LHP       |0.636     |0.035     |0.187      |0.095   |
|Breaking Ball - RHP  |0.644     |0.028     |0.167      |0.082   |
|Breaking Ball - LHP  |0.647     |0.027     |0.165      |0.082   |
|Off Speed - RHP      |0.645     |0.031     |0.176      |0.090   |
|Off Speed - LHP      |0.629     |0.034     |0.185      |0.094   |