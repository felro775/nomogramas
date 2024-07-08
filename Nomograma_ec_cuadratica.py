from pynomo.nomographer import *
Q_params={
'u_min':-50.0,
'u_max':50.0,
'f':lambda u:u/(u**2+1),
'g':lambda u:1/(u**2+1),
'h':lambda u:1,
'title':r'\huge $q$',
'title_x_shift':7.2,
'title_y_shift':-0.3,
'scale_type':'linear smart',
'tick_levels':0,
'tick_text_levels':0,
'turn_relative':True,
'grid_length_0':0.5,
'text_distance_0':0.55,
'grid_length_1':0.3,
'text_distance_1':0.35,
'grid_length_2':0.25,
'text_distance_2':0.30,
'grid_length_3':0.15,
'text_distance_3':0.20,
'grid_length_4':0.15,
'text_distance_4':0.20,
'extra_params':
    [
    {
        'u_min':-50.0,
        'u_max':50.0,
        'base_start':-50.0,
        'base_stop':50.0,
        'tick_levels':5,
        'tick_text_levels':5,
        'scale_type':'log smart',
        'text_format':r"$%3.3g$ ",
    }
    ],
}
A_params={
'u_min':1.0,
'u_max':50.0,
'f':lambda u:1/u,
'g':lambda u:0,
'h':lambda u:1,
'title':r'\huge $a$',
'title_x_shift':-7.0,
'title_y_shift':0.8,
'scale_type':'log smart',
'tick_levels':5,
'tick_text_levels':5,
'grid_length_0':0.5,
'text_distance_0':0.55,
'grid_length_1':0.3,
'text_distance_1':0.35,
'grid_length_2':0.25,
'text_distance_2':0.30,
'grid_length_3':0.15,
'text_distance_3':0.20,
'grid_length_4':0.15,
'text_distance_4':0.20,
'extra_params':
    [
    {
        'u_min':-50.0,
        'u_max':-1.0,
            'tick_levels':5,
        'tick_text_levels':5,
        'scale_type':'log smart',
    }
    ]
}
B_params={
'u_min':-10.0,
'u_max':-0.1,
'f':lambda u:0,
'g':lambda u:-1/(u-1),
'h':lambda u:1,
'title':r'\huge $b$',
'title_x_shift':-1.0,
'title_y_shift':-2.5,
'scale_type':'log smart',
'tick_levels':5,
'tick_text_levels':5,
'grid_length_0':0.5,
'text_distance_0':0.55,
'grid_length_1':0.3,
'text_distance_1':0.35,
'grid_length_2':0.25,
'text_distance_2':0.30,
'grid_length_3':0.15,
'text_distance_3':0.20,
'grid_length_4':0.15,
'text_distance_4':0.20,
'extra_params':
    [{
        'u_min':0.01,
        'u_max':0.25,
        'tick_levels':5,
        'tick_text_levels':5,
        'scale_type':'log smart',
    },
    {
        'u_min':4.0,
        'u_max':15.0,
        'tick_levels':5,
        'tick_text_levels':5,
        'scale_type':'log smart',
    }]
}
block_params={
'block_type':'type_9',
'f1_params':Q_params,
'f2_params':A_params,
'f3_params':B_params,
'transform_ini':False,
}
main_params={
'filename':'Type9-Circular.pdf',
'paper_height':25.4,
'paper_width':30.4,
'block_params':[block_params],
'transformations':[('rotate',0.01),('scale paper',)],
'title_x':7.5,
'title_y': 21.0,
'title_box_width': 6,
'title_str':r'\Huge $q^2-aq+b=0$',
'make_grid':False,
}
Nomographer(main_params)
