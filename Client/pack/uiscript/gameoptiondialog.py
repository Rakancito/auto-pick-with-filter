# You probably have things added, just change "height" to fit the image, in my case is:

window = {
	"name" : "GameOptionDialog",
	"style" : ["movable", "float",],

	"x" : 0,
	"y" : 0,

	"width" : 300,
	"height" : 25*11+8+105, # Change for you.
  
	"children" :
	[
		{
			"name" : "board",
			"type" : "board",

			"x" : 0,
			"y" : 0,

			"width" : 300,
			"height" : 25*11+8+105,  # Change for you.

# Search

				{
					"name" : "salestext_off_button",
					"type" : "radio_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH,
					"y" : 240,

					"text" : uiScriptLocale.OPTION_SALESTEXT_VIEW_OFF,

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},
        
        
# Add after

				#PickUpFilter
					{
						"name" : "PickUpFilter",
						"type" : "text",
						
						"multi_line" : 1,
						
						"x" : LINE_LABEL_X,
						"y" : 300+2,

						"text" : uiScriptLocale.OPTION_PICKUP_TITLE,
					},
					{
						"name" : "Pick_Up_FilterWeapon",
						"type" : "toggle_button",

						"x" : LINE_DATA_X,
						"y" : 300,

						"text" : uiScriptLocale.OPTION_PICKUP_WEAPONS,

						"default_image" : ROOT_PATH + "middle_button_01.sub",
						"over_image" : ROOT_PATH + "middle_button_02.sub",
						"down_image" : ROOT_PATH + "middle_button_03.sub",
					},
					{
						"name" : "Pick_Up_FilterArmor",
						"type" : "toggle_button",

						"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH,
						"y" : 300,

						"text" : uiScriptLocale.OPTION_PICKUP_ARMORS,

						"default_image" : ROOT_PATH + "middle_button_01.sub",
						"over_image" : ROOT_PATH + "middle_button_02.sub",
						"down_image" : ROOT_PATH + "middle_button_03.sub",
					},
					{
						"name" : "Pick_Up_FilterEar",
						"type" : "toggle_button",

						"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH*2,
						"y" : 300,

						"text" : uiScriptLocale.OPTION_PICKUP_EARS,

						"default_image" : ROOT_PATH + "middle_button_01.sub",
						"over_image" : ROOT_PATH + "middle_button_02.sub",
						"down_image" : ROOT_PATH + "middle_button_03.sub",
					},
					{
						"name" : "Pick_Up_FilterNeck",
						"type" : "toggle_button",

						"x" : LINE_DATA_X,
						"y" : 325,

						"text" : uiScriptLocale.OPTION_PICKUP_NECK,

						"default_image" : ROOT_PATH + "middle_button_01.sub",
						"over_image" : ROOT_PATH + "middle_button_02.sub",
						"down_image" : ROOT_PATH + "middle_button_03.sub",
					},
					{
						"name" : "Pick_Up_FilterFoots",
						"type" : "toggle_button",

						"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH,
						"y" : 325,

						"text" : uiScriptLocale.OPTION_PICKUP_SHOES,

						"default_image" : ROOT_PATH + "middle_button_01.sub",
						"over_image" : ROOT_PATH + "middle_button_02.sub",
						"down_image" : ROOT_PATH + "middle_button_03.sub",
					},
					{
						"name" : "Pick_Up_FilterShield",
						"type" : "toggle_button",

						"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH*2,
						"y" : 325,

						"text" : uiScriptLocale.OPTION_PICKUP_SHIELDS,

						"default_image" : ROOT_PATH + "middle_button_01.sub",
						"over_image" : ROOT_PATH + "middle_button_02.sub",
						"down_image" : ROOT_PATH + "middle_button_03.sub",
					},
					{
						"name" : "Pick_Up_FilterBook",
						"type" : "toggle_button",

						"x" : LINE_DATA_X,
						"y" : 350,

						"text" : uiScriptLocale.OPTION_PICKUP_BOOKS,

						"default_image" : ROOT_PATH + "middle_button_01.sub",
						"over_image" : ROOT_PATH + "middle_button_02.sub",
						"down_image" : ROOT_PATH + "middle_button_03.sub",
					},
					{
						"name" : "Pick_Up_FilterStone",
						"type" : "toggle_button",

						"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH,
						"y" : 350,

						"text" : uiScriptLocale.OPTION_PICKUP_STONES,

						"default_image" : ROOT_PATH + "middle_button_01.sub",
						"over_image" : ROOT_PATH + "middle_button_02.sub",
						"down_image" : ROOT_PATH + "middle_button_03.sub",
					},
					{
						"name" : "Pick_Up_FilterEtc",
						"type" : "toggle_button",

						"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH*2,
						"y" : 350,

						"text" : uiScriptLocale.OPTION_PICKUP_OTHER,

						"default_image" : ROOT_PATH + "middle_button_01.sub",
						"over_image" : ROOT_PATH + "middle_button_02.sub",
						"down_image" : ROOT_PATH + "middle_button_03.sub",
					},
          
