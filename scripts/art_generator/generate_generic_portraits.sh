#!/bin/bash

#REQUIREMENTS:
#	python
#	pip
# pypng
# imagegmagick

#USAGE: ./generate_generic_portraits.sh <source_character_name>
#EX:		./generate_generic_portraits.sh guan_yinping

#type=$1
hero=$1

#3k Mod character folder:
#E:\Games\Steam\SteamApps\common\Total War THREE KINGDOMS\data\UI\characters
character_dir="/mnt/e/Games/Steam/SteamApps/common/Total War THREE KINGDOMS/data/UI/characters"

#workspace folder:
#C:\Users\zades\Pictures\tt3k_workspace\dw9\generals
workspace_dir='/mnt/c/Users/zades/Pictures/tt3k_workspace/dw9/generals'
pic_x=-25
pic_y=-75

#set variables
case ${hero} in
	bian_huilan)
	pic_x=-23
	pic_y=2
	element="earth"
	type="generic"
	mod_folder_name="3k_main_hero_special_${element}_lady_bian_huilan"
	;;
	bao_sanniang)
	element="wood"
	type="unique"
	mod_folder_name="3k_main_hero_special_${element}_lady_bao_sanniang"
	;;
	cai_wenji)
	element="water"
	type="generic"
	mod_folder_name="3k_main_hero_special_${element}_lady_cai_yan"
	;;
	cao_cao)
	element="earth"
	type="unique"
	mod_folder_name="3k_main_hero_special_${element}_cao_cao"
	;;
	cao_pi)
	element="earth"
	type="generic"
	mod_folder_name="3k_main_hero_special_${element}_cao_pi"
	;;
	cao_ren)
	element="earth"
	type="generic"
	mod_folder_name="3k_main_hero_special_${element}_cao_ren"
	;;
	cao_xiu)
	element="fire"
	type="generic"
	mod_folder_name="3k_main_hero_special_${element}_cao_xiu"
	;;
	chen_gong)
	element="water"
	type="generic"
	mod_folder_name="3k_main_hero_special_${element}_chen_gong"
	;;
	cheng_pu)
	element="metal"
	type="generic"
	mod_folder_name="3k_main_hero_special_${element}_cheng_pu"
	;;
	da_qiao)
	element="earth"
	type="generic"
	mod_folder_name="3k_main_hero_special_${element}_lady_da_qiao"
	;;
	deng_ai)
	element="metal"
	type="generic"
	mod_folder_name="3k_main_hero_special_${element}_deng_ai"
	;;
	dian_wei)
	element="wood"
	type="unique"
	mod_folder_name="3k_main_hero_special_${element}_dian_wei"
	;;
	diao_chan)
	element="water"
	type="generic"
	mod_folder_name="3k_main_hero_special_${element}_lady_diao_chan"
	;;
	ding_feng)
	element="metal"
	type="generic"
	mod_folder_name="3k_main_hero_special_${element}_ding_feng"
	;;
	dong_bai)
	element="metal"
	type="generic"
	mod_folder_name="3k_main_hero_special_${element}_lady_dong_bai"
	;;
	dong_bai_alt)
	element="metal"
	type="generic"
	mod_folder_name="3k_main_hero_special_${element}_lady_dong_bai"
	;;
	dong_zhuo)
	element="fire"
	type="unique"
	mod_folder_name="3k_main_hero_special_${element}_dong_zhuo"
	;;
	fa_zheng)
	element="water"
	type="generic"
	mod_folder_name="3k_main_hero_special_${element}_fa_zheng"
	;;
	gan_ning)
	element="fire"
	type="unique"
	mod_folder_name="3k_main_hero_special_${element}_gan_ning"
	;;
	guan_ping)
	element="fire"
	type="generic"
	mod_folder_name="3k_main_hero_special_${element}_guan_ping"
	;;
	guan_suo)
	element="earth"
	type="generic"
	mod_folder_name="3k_main_hero_special_${element}_guan_suo"
	;;
	guan_xing)
	element="wood"
	type="generic"
	mod_folder_name="3k_main_hero_special_${element}_guan_xing"
	;;
	guan_yinping)
	element="wood"
	type="unique"
	mod_folder_name="3k_main_hero_special_${element}_lady_guan_yinping"
	;;
	guan_yu)
	element="wood"
	type="unique"
	mod_folder_name="3k_main_hero_special_${element}_guan_yu"
	;;
	guo_huai)
	element="earth"
	type="generic"
	mod_folder_name="3k_main_hero_special_${element}_guo_huai"
	;;
	guo_jia)
	element="water"
	type="generic"
	mod_folder_name="3k_main_hero_special_${element}_guo_jia"
	;;
	han_dang)
	element="wood"
	type="generic"
	mod_folder_name="3k_main_hero_special_${element}_han_dang"
	;;
	hua_xiong)
	element="fire"
	type="generic"
	mod_folder_name="3k_main_hero_special_${element}_hua_xiong"
	;;
	huang_gai)
	element="wood"
	type="generic"
	mod_folder_name="3k_main_hero_special_${element}_huang_gai"
	;;
	huang_zhong)
	element="metal"
	type="unique"
	mod_folder_name="3k_main_hero_special_${element}_huang_zhong"
	;;
	huang_zhong_water)
	hero="huang_zhong"
	element="water"
	type="unique"
	mod_folder_name="3k_main_hero_special_${element}_huang_zhong"
	;;
	iskandar)
	element="fire"
	type="generic"
	mod_folder_name="3k_main_hero_special_${element}_iskandar"
	;;
	jia_chong)
	element="water"
	type="generic"
	mod_folder_name="3k_main_hero_special_${element}_jia_chong"
	;;
	jia_xu)
	element="water"
	type="generic"
	mod_folder_name="3k_main_hero_special_${element}_jia_xu"
	;;
	jiang_wei)
	element="fire"
	type="generic"
	mod_folder_name="3k_main_hero_special_${element}_jiang_wei"
	;;
	li_dian)
	element="metal"
	type="generic"
	mod_folder_name="3k_main_hero_special_${element}_li_dian"
	;;
	lian_shi)
	element="wood"
	type="unique"
	mod_folder_name="3k_main_hero_special_${element}_lady_bu_lianshi"
	;;
	ling_tong)
	element="wood"
	type="generic"
	mod_folder_name="3k_main_hero_special_${element}_ling_tong"
	;;
	liu_bei)
	element="earth"
	type="unique"
	mod_folder_name="3k_main_hero_special_${element}_liu_bei"
	;;
	liu_bei_historical)
	hero=liu_bei
	element="earth"
	type="unique"
	mod_folder_name="3k_main_hero_special_${element}_liu_bei_historical"
	;;
	liu_shan)
	element="earth"
	type="generic"
	mod_folder_name="3k_main_hero_special_${element}_liu_shan"
	;;
	lu_bu)
	element="fire"
	type="unique"
	mod_folder_name="3k_main_hero_special_${element}_lu_bu"
	;;
	lu_bu_historical)
	hero="lu_bu"
	element="fire"
	type="unique"
	mod_folder_name="3k_main_hero_special_${element}_lu_bu_historical"
	;;
	lu_lingqi)
	element="fire"
	type="unique"
	mod_folder_name="3k_main_hero_special_${element}_lady_lu_lingqi"
	;;
	lu_meng)
	element="metal"
	type="generic"
	mod_folder_name="3k_main_hero_special_${element}_lu_meng"
	;;
	lu_su)
	element="water"
	type="generic"
	mod_folder_name="3k_main_hero_special_${element}_lu_su"
	;;
	lu_xun)
	element="water"
	type="generic"
	mod_folder_name="3k_main_hero_special_${element}_lu_xun"
	;;
	ma_chao)
	element="fire"
	type="unique"
	mod_folder_name="3k_main_hero_special_${element}_ma_chao"
	;;
	ma_dai)
	element="fire"
	type="generic"
	mod_folder_name="3k_main_hero_special_${element}_ma_dai"
	;;
	man_chong)
	element="fire"
	type="generic"
	mod_folder_name="3k_main_hero_special_${element}_man_chong"
	;;
	meng_huo)
	element="wood"
	type="generic"
	mod_folder_name="3k_main_hero_special_${element}_meng_huo"
	;;
	pang_de)
	element="wood"
	type="unique"
	mod_folder_name="3k_main_hero_special_${element}_pang_de"
	;;
	pang_tong)
	element="water"
	type="generic"
	mod_folder_name="3k_main_hero_special_${element}_pang_tong"
	;;
	sima_shi)
	element="earth"
	type="generic"
	mod_folder_name="3k_main_hero_special_${element}_sima_shi"
	;;
	sima_yi)
	element="water"
	type="unique"
	mod_folder_name="3k_main_hero_special_${element}_sima_yi"
	;;
	sima_zhao)
	element="earth"
	type="generic"
	mod_folder_name="3k_main_hero_special_${element}_sima_zhao"
	;;
	sun_ce)
	element="fire"
	type="unique"
	mod_folder_name="3k_main_hero_special_${element}_sun_ce"
	;;
	sun_jian)
	element="metal"
	type="unique"
	mod_folder_name="3k_main_hero_special_${element}_sun_jian"
	;;
	sun_quan)
	element="earth"
	type="unique"
	mod_folder_name="3k_main_hero_special_${element}_sun_quan"
	;;
	sun_shangxiang)
	element="fire"
	type="unique"
	mod_folder_name="3k_main_hero_special_${element}_lady_sun"
	;;
	taishi_ci)
	element="metal"
	type="unique"
	mod_folder_name="3k_main_hero_special_${element}_taishi_ci"
	;;
	tohsaka_rin)
	element="fire"
	type="unique"
	mod_folder_name="3k_main_hero_special_${element}_lady_tohsaka_rin"
	;;
	wang_yi)
	element="fire"
	type="unique"
	mod_folder_name="3k_main_hero_special_${element}_lady_wang_yi"
	;;
	wang_yuanji)
	element="earth"
	type="generic"
	mod_folder_name="3k_main_hero_special_${element}_lady_wang_yuanji"
	;;
	wei_yan)
	element="fire"
	type="generic"
	mod_folder_name="3k_main_hero_special_${element}_wei_yan"
	;;
	wei_yan_2)
	pic_x=30
	pic_y=25
	element="fire"
	type="generic"
	mod_folder_name="3k_main_hero_special_${element}_wei_yan"
	;;
	wen_yang)
	element="wood"
	type="generic"
	mod_folder_name="3k_main_hero_special_${element}_wen_yang"
	;;
	xiahou_ba)
	element="wood"
	type="generic"
	mod_folder_name="3k_main_hero_special_${element}_xiahou_ba"
	;;
	xiahou_ba_alt)
	element="wood"
	type="generic"
	mod_folder_name="3k_main_hero_special_${element}_xiahou_ba"
	;;
	xiahou_dun)
	element="wood"
	type="unique"
	mod_folder_name="3k_main_hero_special_${element}_xiahou_dun"
	;;
	xiahou_ji)
	element="water"
	type="generic"
	mod_folder_name="3k_main_hero_special_${element}_lady_xiahou_ji"
	;;
	xiahou_yuan)
	element="fire"
	type="unique"
	mod_folder_name="3k_main_hero_special_${element}_xiahou_yuan"
	;;
	xiao_qiao)
	element="metal"
	type="generic"
	mod_folder_name="3k_main_hero_special_${element}_lady_xiao_qiao"
	;;
	xin_xianying)
	element="water"
	type="generic"
	mod_folder_name="3k_main_hero_special_${element}_lady_xin_xianying"
	;;
	xing_cai)
	element="metal"
	type="generic"
	mod_folder_name="3k_main_hero_special_${element}_lady_zhang_xingcai"
	;;
	xu_huang)
	element="metal"
	type="unique"
	mod_folder_name="3k_main_hero_special_${element}_xu_huang"
	;;
	xu_sheng)
	element="fire"
	type="generic"
	mod_folder_name="3k_main_hero_special_${element}_xu_sheng"
	;;
	xu_shu)
	element="water"
	type="generic"
	mod_folder_name="3k_main_hero_special_${element}_xu_shu"
	;;
	xu_zhu)
	element="wood"
	type="unique"
	mod_folder_name="3k_main_hero_special_${element}_xu_chu"
	;;
	xun_you)
	element="earth"
	type="generic"
	mod_folder_name="3k_main_hero_special_${element}_xun_you"
	;;
	xun_yu)
	element="water"
	type="generic"
	mod_folder_name="3k_main_hero_special_${element}_xun_yu"
	;;
	yuan_shao)
	element="earth"
	type="unique"
	mod_folder_name="3k_main_hero_special_${element}_yuan_shao"
	;;
	yuan_shu)
	element="earth"
	type="unique"
	mod_folder_name="3k_main_hero_special_${element}_yuan_shu"
	;;
	yu_jin)
	element="metal"
	type="generic"
	mod_folder_name="3k_main_hero_special_${element}_yu_jin"
	;;
	yue_jin)
	element="metal"
	type="unique"
	mod_folder_name="3k_main_hero_special_${element}_yue_jin"
	;;
	yue_ying)
	element="wood"
	type="unique"
	mod_folder_name="3k_main_hero_special_${element}_lady_huang_yueying"
	;;
	zhang_bao)
	element="metal"
	type="generic"
	mod_folder_name="3k_main_hero_special_${element}_zhang_bao"
	;;
	zhang_chunhua)
	element="metal"
	type="generic"
	mod_folder_name="3k_main_hero_special_${element}_lady_zhang_chunhua"
	;;
	zhang_fei)
	element="fire"
	type="unique"
	mod_folder_name="3k_main_hero_special_${element}_zhang_fei"
	;;
	zhang_he)
	element="fire"
	type="generic"
	mod_folder_name="3k_main_hero_special_${element}_zhang_he"
	;;
	zhang_liao)
	element="metal"
	type="unique"
	mod_folder_name="3k_main_hero_special_${element}_zhang_liao"
	;;
	zhang_jiao)
	element="healer"
	type="generic"
	mod_folder_name="3k_ytr_hero_special_${element}_zhang_jiao"
	;;
	zhao_yun)
	element="metal"
	type="unique"
	mod_folder_name="3k_main_hero_special_${element}_zhao_yun"
	;;
	zhong_hui)
	element="earth"
	type="generic"
	mod_folder_name="3k_main_hero_special_${element}_zhong_hui"
	;;
	zhong_hui_alt)
	element="earth"
	type="generic"
	mod_folder_name="3k_main_hero_special_${element}_zhong_hui"
	;;
	zhou_cang)
	element="fire"
	type="generic"
	mod_folder_name="3k_main_hero_special_${element}_zhou_cang"
	;;
	zhou_cang_alt)
	element="fire"
	type="generic"
	mod_folder_name="3k_main_hero_special_${element}_zhou_cang"
	;;
	zhen_ji)
	element="earth"
	type="generic"
	mod_folder_name="3k_main_hero_special_${element}_lady_zhen_ji"
	;;
	zhou_tai)
	element="fire"
	type="generic"
	mod_folder_name="3k_main_hero_special_${element}_zhou_tai"
	;;
	zhou_yu)
	element="water"
	type="unique"
	mod_folder_name="3k_main_hero_special_${element}_zhou_yu"
	;;
	zhou_yu_historical)
	hero=zhou_yu
	element="water"
	type="unique"
	mod_folder_name="3k_main_hero_special_${element}_zhou_yu_historical"
	;;
	zhu_ran)
	element="fire"
	type="generic"
	mod_folder_name="3k_main_hero_special_${element}_zhu_ran"
	;;
	zhu_rong)
	element="fire"
	type="unique"
	mod_folder_name="3k_main_hero_special_${element}_lady_zhu_rong"
	;;
	zhuge_dan)
	element="fire"
	type="generic"
	mod_folder_name="3k_main_hero_special_${element}_zhuge_dan"
	;;
	zhuge_liang)
	element="water"
	type="unique"
	mod_folder_name="3k_main_hero_special_${element}_zhuge_liang"
	;;
	zuo_ci)
	element="water"
	type="generic"
	mod_folder_name="3k_main_hero_special_${element}_zuo_ci"
	;;
esac

#gender='male'
#if [[ ${mod_folder_name} == *"lady"* ]]; then
#	gender='female'
#fi
#hero="generic_${element}_${gender}"

echo "x: ${pic_x}"
echo "y: ${pic_y}"

convert ${workspace_dir}/${hero}/halfbody_large_large.png -resize 312x250 -background transparent -gravity center -extent 312x250 ${workspace_dir}/${hero}/halfbody_large.png
convert ${workspace_dir}/${hero}/halfbody_large_large.png -resize 176x134 -background transparent -gravity center -extent 176x134 ${workspace_dir}/${hero}/halfbody_small_large.png
convert ${workspace_dir}/${hero}/halfbody_large_large.png -resize 176x134 -background transparent -gravity center -extent 110x84 ${workspace_dir}/${hero}/halfbody_small.png
convert ${workspace_dir}/${hero}/bobbleheads_large.png -resize 84x138 -background transparent -gravity center -extent 84x138 ${workspace_dir}/${hero}/bobbleheads.png
convert ${workspace_dir}/${hero}/mini_large.png -resize 30x30 -background transparent -gravity center -extent 30x30 ${workspace_dir}/${hero}/mini.png
convert ${workspace_dir}/${hero}/unitcard_large.png -resize 82x272 -background transparent -gravity center -extent 82x272 ${workspace_dir}/${hero}/unitcard.png


if [[ ${type} == "unique" ]]; then
	mkdir -p "${character_dir}"/${mod_folder_name}/composites/large_panel/angry
	mkdir -p "${character_dir}"/${mod_folder_name}/composites/large_panel/happy
	mkdir -p "${character_dir}"/${mod_folder_name}/composites/large_panel/norm

	mkdir -p "${character_dir}"/${mod_folder_name}/stills/bobbleheads/large
	mkdir -p "${character_dir}"/${mod_folder_name}/stills/halfbody_large/large
	mkdir -p "${character_dir}"/${mod_folder_name}/stills/halfbody_small/large
	mkdir -p "${character_dir}"/${mod_folder_name}/stills/mini/large
	mkdir -p "${character_dir}"/${mod_folder_name}/stills/unitcards/large

	cp ${workspace_dir}/${hero}/head.png "${character_dir}"/${mod_folder_name}/composites/large_panel/angry/head.png
	cp ${workspace_dir}/${hero}/head.png "${character_dir}"/${mod_folder_name}/composites/large_panel/happy/head.png
	cp ${workspace_dir}/${hero}/head.png "${character_dir}"/${mod_folder_name}/composites/large_panel/norm/head.png

	python /mnt/c/Users/zades/Pictures/tt3k_workspace/10_gold_flowers/source/add_comment.py "${character_dir}"/${mod_folder_name}/composites/large_panel/angry/head.png "[type:angry;x:${pic_x};y:${pic_y};z-order:0;pivot_x:0.5000;pivot_y:0.5000;]"
	python /mnt/c/Users/zades/Pictures/tt3k_workspace/10_gold_flowers/source/add_comment.py "${character_dir}"/${mod_folder_name}/composites/large_panel/happy/head.png "[type:happy;x:${pic_x};y:${pic_y};z-order:0;pivot_x:0.5000;pivot_y:0.5000;]"
	python /mnt/c/Users/zades/Pictures/tt3k_workspace/10_gold_flowers/source/add_comment.py "${character_dir}"/${mod_folder_name}/composites/large_panel/norm/head.png "[type:norm;x:${pic_x};y:${pic_y};z-order:0;pivot_x:0.5000;pivot_y:0.5000;]"

	cp ${workspace_dir}/${hero}/bobbleheads.png "${character_dir}"/${mod_folder_name}/stills/bobbleheads/${mod_folder_name}.png
	cp ${workspace_dir}/${hero}/bobbleheads_large.png "${character_dir}"/${mod_folder_name}/stills/bobbleheads/large/${mod_folder_name}.png
	cp ${workspace_dir}/${hero}/halfbody_large.png "${character_dir}"/${mod_folder_name}/stills/halfbody_large/${mod_folder_name}.png
	cp ${workspace_dir}/${hero}/halfbody_large_large.png "${character_dir}"/${mod_folder_name}/stills/halfbody_large/large/${mod_folder_name}.png
	cp ${workspace_dir}/${hero}/halfbody_small.png "${character_dir}"/${mod_folder_name}/stills/halfbody_small/${mod_folder_name}.png
	cp ${workspace_dir}/${hero}/halfbody_small_large.png "${character_dir}"/${mod_folder_name}/stills/halfbody_small/large/${mod_folder_name}.png
	cp ${workspace_dir}/${hero}/mini.png "${character_dir}"/${mod_folder_name}/stills/mini/${mod_folder_name}.png
	cp ${workspace_dir}/${hero}/mini_large.png "${character_dir}"/${mod_folder_name}/stills/mini/large/${mod_folder_name}.png
	cp ${workspace_dir}/${hero}/unitcard.png "${character_dir}"/${mod_folder_name}/stills/unitcards/${mod_folder_name}.png
	cp ${workspace_dir}/${hero}/unitcard_large.png "${character_dir}"/${mod_folder_name}/stills/unitcards/large/${mod_folder_name}.png
elif [[ ${type} == "generic" ]]; then
	mkdir -p "${character_dir}"/${mod_folder_name}/composites/faces/${mod_folder_name}/large_panel/angry
	mkdir -p "${character_dir}"/${mod_folder_name}/composites/faces/${mod_folder_name}/large_panel/happy
	mkdir -p "${character_dir}"/${mod_folder_name}/composites/faces/${mod_folder_name}/large_panel/norm

	mkdir -p "${character_dir}"/${mod_folder_name}/composites/faces/${mod_folder_name}/small_panel/angry
	mkdir -p "${character_dir}"/${mod_folder_name}/composites/faces/${mod_folder_name}/small_panel/happy
	mkdir -p "${character_dir}"/${mod_folder_name}/composites/faces/${mod_folder_name}/small_panel/norm

	mkdir -p "${character_dir}"/${mod_folder_name}/stills/bobbleheads/faces/large
	mkdir -p "${character_dir}"/${mod_folder_name}/stills/bobbleheads/large
	mkdir -p "${character_dir}"/${mod_folder_name}/stills/halfbody_large/faces/large
	mkdir -p "${character_dir}"/${mod_folder_name}/stills/halfbody_large/large
	mkdir -p "${character_dir}"/${mod_folder_name}/stills/halfbody_small/faces/large
	mkdir -p "${character_dir}"/${mod_folder_name}/stills/halfbody_small/large
	mkdir -p "${character_dir}"/${mod_folder_name}/stills/mini/faces/large
	mkdir -p "${character_dir}"/${mod_folder_name}/stills/mini/large
	mkdir -p "${character_dir}"/${mod_folder_name}/stills/unitcards/faces/large
	mkdir -p "${character_dir}"/${mod_folder_name}/stills/unitcards/large

	cp ${workspace_dir}/${hero}/head.png "${character_dir}"/${mod_folder_name}/composites/faces/${mod_folder_name}/large_panel/angry/face.png
	cp ${workspace_dir}/${hero}/head.png "${character_dir}"/${mod_folder_name}/composites/faces/${mod_folder_name}/large_panel/happy/face.png
	cp ${workspace_dir}/${hero}/head.png "${character_dir}"/${mod_folder_name}/composites/faces/${mod_folder_name}/large_panel/norm/face.png

	cp ${workspace_dir}/${hero}/head.png "${character_dir}"/${mod_folder_name}/composites/faces/${mod_folder_name}/small_panel/angry/face.png
	cp ${workspace_dir}/${hero}/head.png "${character_dir}"/${mod_folder_name}/composites/faces/${mod_folder_name}/small_panel/happy/face.png
	cp ${workspace_dir}/${hero}/head.png "${character_dir}"/${mod_folder_name}/composites/faces/${mod_folder_name}/small_panel/norm/face.png

	python /mnt/c/Users/zades/Pictures/tt3k_workspace/10_gold_flowers/source/add_comment.py "${character_dir}"/${mod_folder_name}/composites/faces/${mod_folder_name}/large_panel/angry/face.png "[type:angry;x:${pic_x};y:${pic_y};z-order:0;pivot_x:0.5000;pivot_y:0.5000;]"
	python /mnt/c/Users/zades/Pictures/tt3k_workspace/10_gold_flowers/source/add_comment.py "${character_dir}"/${mod_folder_name}/composites/faces/${mod_folder_name}/large_panel/happy/face.png "[type:happy;x:${pic_x};y:${pic_y};z-order:0;pivot_x:0.5000;pivot_y:0.5000;]"
	python /mnt/c/Users/zades/Pictures/tt3k_workspace/10_gold_flowers/source/add_comment.py "${character_dir}"/${mod_folder_name}/composites/faces/${mod_folder_name}/large_panel/norm/face.png "[type:norm;x:${pic_x};y:${pic_y};z-order:0;pivot_x:0.5000;pivot_y:0.5000;]"

	python /mnt/c/Users/zades/Pictures/tt3k_workspace/10_gold_flowers/source/add_comment.py "${character_dir}"/${mod_folder_name}/composites/faces/${mod_folder_name}/small_panel/angry/face.png "[type:angry;x:${pic_x};y:${pic_y};z-order:0;pivot_x:0.5000;pivot_y:0.5000;]"
	python /mnt/c/Users/zades/Pictures/tt3k_workspace/10_gold_flowers/source/add_comment.py "${character_dir}"/${mod_folder_name}/composites/faces/${mod_folder_name}/small_panel/happy/face.png "[type:happy;x:${pic_x};y:${pic_y};z-order:0;pivot_x:0.5000;pivot_y:0.5000;]"
	python /mnt/c/Users/zades/Pictures/tt3k_workspace/10_gold_flowers/source/add_comment.py "${character_dir}"/${mod_folder_name}/composites/faces/${mod_folder_name}/small_panel/norm/face.png "[type:norm;x:${pic_x};y:${pic_y};z-order:0;pivot_x:0.5000;pivot_y:0.5000;]"

	cp ${workspace_dir}/${hero}/bobbleheads.png "${character_dir}"/${mod_folder_name}/stills/bobbleheads/faces/${mod_folder_name}.png
	cp ${workspace_dir}/${hero}/bobbleheads_large.png "${character_dir}"/${mod_folder_name}/stills/bobbleheads/faces/large/${mod_folder_name}.png
	cp ${workspace_dir}/${hero}/halfbody_large.png "${character_dir}"/${mod_folder_name}/stills/halfbody_large/faces/${mod_folder_name}.png
	cp ${workspace_dir}/${hero}/halfbody_large_large.png "${character_dir}"/${mod_folder_name}/stills/halfbody_large/faces/large/${mod_folder_name}.png
	cp ${workspace_dir}/${hero}/halfbody_small.png "${character_dir}"/${mod_folder_name}/stills/halfbody_small/faces/${mod_folder_name}.png
	cp ${workspace_dir}/${hero}/halfbody_small_large.png "${character_dir}"/${mod_folder_name}/stills/halfbody_small/faces/large/${mod_folder_name}.png
	cp ${workspace_dir}/${hero}/mini.png "${character_dir}"/${mod_folder_name}/stills/mini/faces/${mod_folder_name}.png
	cp ${workspace_dir}/${hero}/mini_large.png "${character_dir}"/${mod_folder_name}/stills/mini/faces/large/${mod_folder_name}.png
	cp ${workspace_dir}/${hero}/unitcard.png "${character_dir}"/${mod_folder_name}/stills/unitcards/faces/${mod_folder_name}.png
	cp ${workspace_dir}/${hero}/unitcard_large.png "${character_dir}"/${mod_folder_name}/stills/unitcards/faces/large/${mod_folder_name}.png

	gender='male'
	if [[ ${mod_folder_name} == *"lady"* ]]; then
		gender='female'
	fi
	#create blank ancillary files

	for dir in "${character_dir}"/${mod_folder_name}/stills/*; do
		dir_short=${dir##*/}
		case ${dir_short} in
			bobbleheads)
			size="84x138"
			size_large="134x220"
			;;
			halfbody_large)
			size="312x250"
			size_large="499x400"
			;;
			halfbody_small)
			size="100x84"
			size_large="176x134"
			;;
			mini)
			size="30x30"
			size_large="48x48"
			;;
			unitcards)
			size="82x272"
			size_large="131x435"
			;;
		esac

		if [[ ${element} == "water" ]]; then
			convert -size ${size} xc:transparent png32:"${character_dir}"/${mod_folder_name}/stills/${dir_short}/3k_main_ancillary_armour_light_tunic_common_water_${gender}.png
			convert -size ${size} xc:transparent png32:"${character_dir}"/${mod_folder_name}/stills/${dir_short}/3k_main_ancillary_armour_light_tunic_exceptional_water_${gender}.png
			convert -size ${size} xc:transparent png32:"${character_dir}"/${mod_folder_name}/stills/${dir_short}/3k_main_ancillary_armour_light_tunic_refined_water_${gender}.png
			convert -size ${size} xc:transparent png32:"${character_dir}"/${mod_folder_name}/stills/${dir_short}/3k_main_ancillary_armour_light_tunic_unique_water_${gender}.png

			convert -size ${size_large} xc:transparent png32:"${character_dir}"/${mod_folder_name}/stills/${dir_short}/large/3k_main_ancillary_armour_light_tunic_common_water_${gender}.png
			convert -size ${size_large} xc:transparent png32:"${character_dir}"/${mod_folder_name}/stills/${dir_short}/large/3k_main_ancillary_armour_light_tunic_exceptional_water_${gender}.png
			convert -size ${size_large} xc:transparent png32:"${character_dir}"/${mod_folder_name}/stills/${dir_short}/large/3k_main_ancillary_armour_light_tunic_refined_water_${gender}.png
			convert -size ${size_large} xc:transparent png32:"${character_dir}"/${mod_folder_name}/stills/${dir_short}/large/3k_main_ancillary_armour_light_tunic_unique_water_${gender}.png
		elif [[ ${element} == "fire" ]]; then
			convert -size ${size} xc:transparent png32:"${character_dir}"/${mod_folder_name}/stills/${dir_short}/3k_main_ancillary_armour_heavy_iron_common_shared_${gender}.png
			convert -size ${size} xc:transparent png32:"${character_dir}"/${mod_folder_name}/stills/${dir_short}/3k_main_ancillary_armour_heavy_iron_exceptional_fire_${gender}.png
			convert -size ${size} xc:transparent png32:"${character_dir}"/${mod_folder_name}/stills/${dir_short}/3k_main_ancillary_armour_heavy_iron_refined_shared_${gender}.png
			convert -size ${size} xc:transparent png32:"${character_dir}"/${mod_folder_name}/stills/${dir_short}/3k_main_ancillary_armour_heavy_iron_unique_fire_${gender}.png
			convert -size ${size} xc:transparent png32:"${character_dir}"/${mod_folder_name}/stills/${dir_short}/3k_main_ancillary_armour_medium_iron_partial_common_shared_${gender}.png
			convert -size ${size} xc:transparent png32:"${character_dir}"/${mod_folder_name}/stills/${dir_short}/3k_main_ancillary_armour_medium_iron_partial_exceptional_fire_${gender}.png
			convert -size ${size} xc:transparent png32:"${character_dir}"/${mod_folder_name}/stills/${dir_short}/3k_main_ancillary_armour_medium_iron_partial_refined_shared_${gender}.png
			convert -size ${size} xc:transparent png32:"${character_dir}"/${mod_folder_name}/stills/${dir_short}/3k_main_ancillary_armour_medium_iron_partial_unique_fire_${gender}.png

			convert -size ${size_large} xc:transparent png32:"${character_dir}"/${mod_folder_name}/stills/${dir_short}/large/3k_main_ancillary_armour_heavy_iron_common_shared_${gender}.png
			convert -size ${size_large} xc:transparent png32:"${character_dir}"/${mod_folder_name}/stills/${dir_short}/large/3k_main_ancillary_armour_heavy_iron_exceptional_fire_${gender}.png
			convert -size ${size_large} xc:transparent png32:"${character_dir}"/${mod_folder_name}/stills/${dir_short}/large/3k_main_ancillary_armour_heavy_iron_refined_shared_${gender}.png
			convert -size ${size_large} xc:transparent png32:"${character_dir}"/${mod_folder_name}/stills/${dir_short}/large/3k_main_ancillary_armour_heavy_iron_unique_fire_${gender}.png
			convert -size ${size_large} xc:transparent png32:"${character_dir}"/${mod_folder_name}/stills/${dir_short}/large/3k_main_ancillary_armour_medium_iron_partial_common_shared_${gender}.png
			convert -size ${size_large} xc:transparent png32:"${character_dir}"/${mod_folder_name}/stills/${dir_short}/large/3k_main_ancillary_armour_medium_iron_partial_exceptional_fire_${gender}.png
			convert -size ${size_large} xc:transparent png32:"${character_dir}"/${mod_folder_name}/stills/${dir_short}/large/3k_main_ancillary_armour_medium_iron_partial_refined_shared_${gender}.png
			convert -size ${size_large} xc:transparent png32:"${character_dir}"/${mod_folder_name}/stills/${dir_short}/large/3k_main_ancillary_armour_medium_iron_partial_unique_fire_${gender}.png
		elif [[ ${element} == "earth" ]]; then
			convert -size ${size} xc:transparent png32:"${character_dir}"/${mod_folder_name}/stills/${dir_short}/3k_main_ancillary_armour_light_armour_earth_metal_and_water_common.png
			convert -size ${size} xc:transparent png32:"${character_dir}"/${mod_folder_name}/stills/${dir_short}/3k_main_ancillary_armour_light_leather_partial_common_shared_${gender}.png
			convert -size ${size} xc:transparent png32:"${character_dir}"/${mod_folder_name}/stills/${dir_short}/3k_main_ancillary_armour_light_leather_partial_exceptional_earth_${gender}.png
			convert -size ${size} xc:transparent png32:"${character_dir}"/${mod_folder_name}/stills/${dir_short}/3k_main_ancillary_armour_light_leather_partial_refined_shared_${gender}.png
			convert -size ${size} xc:transparent png32:"${character_dir}"/${mod_folder_name}/stills/${dir_short}/3k_main_ancillary_armour_light_leather_partial_unique_earth_${gender}.png
			convert -size ${size} xc:transparent png32:"${character_dir}"/${mod_folder_name}/stills/${dir_short}/3k_main_ancillary_armour_medium_leather_common_shared_${gender}.png
			convert -size ${size} xc:transparent png32:"${character_dir}"/${mod_folder_name}/stills/${dir_short}/3k_main_ancillary_armour_medium_leather_exceptional_earth_${gender}.png
			convert -size ${size} xc:transparent png32:"${character_dir}"/${mod_folder_name}/stills/${dir_short}/3k_main_ancillary_armour_medium_leather_refined_shared_${gender}.png
			convert -size ${size} xc:transparent png32:"${character_dir}"/${mod_folder_name}/stills/${dir_short}/3k_main_ancillary_armour_medium_leather_unique_earth_${gender}.png

			convert -size ${size_large} xc:transparent png32:"${character_dir}"/${mod_folder_name}/stills/${dir_short}/large/3k_main_ancillary_armour_light_armour_earth_metal_and_water_common.png
			convert -size ${size_large} xc:transparent png32:"${character_dir}"/${mod_folder_name}/stills/${dir_short}/large/3k_main_ancillary_armour_light_leather_partial_common_shared_${gender}.png
			convert -size ${size_large} xc:transparent png32:"${character_dir}"/${mod_folder_name}/stills/${dir_short}/large/3k_main_ancillary_armour_light_leather_partial_exceptional_earth_${gender}.png
			convert -size ${size_large} xc:transparent png32:"${character_dir}"/${mod_folder_name}/stills/${dir_short}/large/3k_main_ancillary_armour_light_leather_partial_refined_shared_${gender}.png
			convert -size ${size_large} xc:transparent png32:"${character_dir}"/${mod_folder_name}/stills/${dir_short}/large/3k_main_ancillary_armour_light_leather_partial_unique_earth_${gender}.png
			convert -size ${size_large} xc:transparent png32:"${character_dir}"/${mod_folder_name}/stills/${dir_short}/large/3k_main_ancillary_armour_medium_leather_common_shared_${gender}.png
			convert -size ${size_large} xc:transparent png32:"${character_dir}"/${mod_folder_name}/stills/${dir_short}/large/3k_main_ancillary_armour_medium_leather_exceptional_earth_${gender}.png
			convert -size ${size_large} xc:transparent png32:"${character_dir}"/${mod_folder_name}/stills/${dir_short}/large/3k_main_ancillary_armour_medium_leather_refined_shared_${gender}.png
			convert -size ${size_large} xc:transparent png32:"${character_dir}"/${mod_folder_name}/stills/${dir_short}/large/3k_main_ancillary_armour_medium_leather_unique_earth_${gender}.png
		elif [[ ${element} == "metal" ]]; then
			convert -size ${size} xc:transparent png32:"${character_dir}"/${mod_folder_name}/stills/${dir_short}/3k_main_ancillary_armour_light_leather_partial_common_shared_${gender}.png
			convert -size ${size} xc:transparent png32:"${character_dir}"/${mod_folder_name}/stills/${dir_short}/3k_main_ancillary_armour_light_leather_partial_exceptional_metal_${gender}.png
			convert -size ${size} xc:transparent png32:"${character_dir}"/${mod_folder_name}/stills/${dir_short}/3k_main_ancillary_armour_light_leather_partial_refined_shared_${gender}.png
			convert -size ${size} xc:transparent png32:"${character_dir}"/${mod_folder_name}/stills/${dir_short}/3k_main_ancillary_armour_light_leather_partial_unique_metal_${gender}.png
			convert -size ${size} xc:transparent png32:"${character_dir}"/${mod_folder_name}/stills/${dir_short}/3k_main_ancillary_armour_medium_leather_common_shared_${gender}.png
			convert -size ${size} xc:transparent png32:"${character_dir}"/${mod_folder_name}/stills/${dir_short}/3k_main_ancillary_armour_medium_leather_exceptional_metal_${gender}.png
			convert -size ${size} xc:transparent png32:"${character_dir}"/${mod_folder_name}/stills/${dir_short}/3k_main_ancillary_armour_medium_leather_refined_shared_${gender}.png
			convert -size ${size} xc:transparent png32:"${character_dir}"/${mod_folder_name}/stills/${dir_short}/3k_main_ancillary_armour_medium_leather_unique_metal_${gender}.png

			convert -size ${size_large} xc:transparent png32:"${character_dir}"/${mod_folder_name}/stills/${dir_short}/large/3k_main_ancillary_armour_light_leather_partial_common_shared_${gender}.png
			convert -size ${size_large} xc:transparent png32:"${character_dir}"/${mod_folder_name}/stills/${dir_short}/large/3k_main_ancillary_armour_light_leather_partial_exceptional_metal_${gender}.png
			convert -size ${size_large} xc:transparent png32:"${character_dir}"/${mod_folder_name}/stills/${dir_short}/large/3k_main_ancillary_armour_light_leather_partial_refined_shared_${gender}.png
			convert -size ${size_large} xc:transparent png32:"${character_dir}"/${mod_folder_name}/stills/${dir_short}/large/3k_main_ancillary_armour_light_leather_partial_unique_metal_${gender}.png
			convert -size ${size_large} xc:transparent png32:"${character_dir}"/${mod_folder_name}/stills/${dir_short}/large/3k_main_ancillary_armour_medium_leather_common_shared_${gender}.png
			convert -size ${size_large} xc:transparent png32:"${character_dir}"/${mod_folder_name}/stills/${dir_short}/large/3k_main_ancillary_armour_medium_leather_exceptional_metal_${gender}.png
			convert -size ${size_large} xc:transparent png32:"${character_dir}"/${mod_folder_name}/stills/${dir_short}/large/3k_main_ancillary_armour_medium_leather_refined_shared_${gender}.png
			convert -size ${size_large} xc:transparent png32:"${character_dir}"/${mod_folder_name}/stills/${dir_short}/large/3k_main_ancillary_armour_medium_leather_unique_metal_${gender}.png
		elif [[ ${element} == "wood" ]]; then
			convert -size ${size} xc:transparent png32:"${character_dir}"/${mod_folder_name}/stills/${dir_short}/3k_main_ancillary_armour_heavy_iron_common_shared_${gender}.png
			convert -size ${size} xc:transparent png32:"${character_dir}"/${mod_folder_name}/stills/${dir_short}/3k_main_ancillary_armour_heavy_iron_exceptional_wood_${gender}.png
			convert -size ${size} xc:transparent png32:"${character_dir}"/${mod_folder_name}/stills/${dir_short}/3k_main_ancillary_armour_heavy_iron_refined_shared_${gender}.png
			convert -size ${size} xc:transparent png32:"${character_dir}"/${mod_folder_name}/stills/${dir_short}/3k_main_ancillary_armour_heavy_iron_unique_wood_${gender}.png
			convert -size ${size} xc:transparent png32:"${character_dir}"/${mod_folder_name}/stills/${dir_short}/3k_main_ancillary_armour_medium_iron_partial_common_shared_${gender}.png
			convert -size ${size} xc:transparent png32:"${character_dir}"/${mod_folder_name}/stills/${dir_short}/3k_main_ancillary_armour_medium_iron_partial_exceptional_wood_${gender}.png
			convert -size ${size} xc:transparent png32:"${character_dir}"/${mod_folder_name}/stills/${dir_short}/3k_main_ancillary_armour_medium_iron_partial_refined_shared_${gender}.png
			convert -size ${size} xc:transparent png32:"${character_dir}"/${mod_folder_name}/stills/${dir_short}/3k_main_ancillary_armour_medium_iron_partial_unique_wood_${gender}.png

			convert -size ${size_large} xc:transparent png32:"${character_dir}"/${mod_folder_name}/stills/${dir_short}/large/3k_main_ancillary_armour_heavy_iron_common_shared_${gender}.png
			convert -size ${size_large} xc:transparent png32:"${character_dir}"/${mod_folder_name}/stills/${dir_short}/large/3k_main_ancillary_armour_heavy_iron_exceptional_wood_${gender}.png
			convert -size ${size_large} xc:transparent png32:"${character_dir}"/${mod_folder_name}/stills/${dir_short}/large/3k_main_ancillary_armour_heavy_iron_refined_shared_${gender}.png
			convert -size ${size_large} xc:transparent png32:"${character_dir}"/${mod_folder_name}/stills/${dir_short}/large/3k_main_ancillary_armour_heavy_iron_unique_wood_${gender}.png
			convert -size ${size_large} xc:transparent png32:"${character_dir}"/${mod_folder_name}/stills/${dir_short}/large/3k_main_ancillary_armour_medium_iron_partial_common_shared_${gender}.png
			convert -size ${size_large} xc:transparent png32:"${character_dir}"/${mod_folder_name}/stills/${dir_short}/large/3k_main_ancillary_armour_medium_iron_partial_exceptional_wood_${gender}.png
			convert -size ${size_large} xc:transparent png32:"${character_dir}"/${mod_folder_name}/stills/${dir_short}/large/3k_main_ancillary_armour_medium_iron_partial_refined_shared_${gender}.png
			convert -size ${size_large} xc:transparent png32:"${character_dir}"/${mod_folder_name}/stills/${dir_short}/large/3k_main_ancillary_armour_medium_iron_partial_unique_wood_${gender}.png
		fi
	done
else
	echo "Invalid type of general, type must be generic or unique"
	exit 1
fi
