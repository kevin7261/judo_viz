SHEET_URL_VIZ = 'https://docs.google.com/spreadsheets/d/1A8wULZkw8SYx4_jkv2xbcUhaQuUEy1k-J_L8MpSkf-U/edit?usp=sharing'

olympic_countries = [
    {"id": 1, "english_name": "Afghanistan", "chinese_name": "阿富汗", "code": "AFG", "latitude": 33.93911, "longitude": 67.709953, "continent": "Asia"},
    {"id": 2, "english_name": "Albania", "chinese_name": "阿爾巴尼亞", "code": "ALB", "latitude": 41.153332, "longitude": 20.168331, "continent": "Europe"},
    {"id": 3, "english_name": "Algeria", "chinese_name": "阿爾及利亞", "code": "ALG", "latitude": 28.033886, "longitude": 1.659626, "continent": "Africa"},
    {"id": 4, "english_name": "Andorra", "chinese_name": "安道爾", "code": "AND", "latitude": 42.507789, "longitude": 1.52109, "continent": "Europe"},
    {"id": 5, "english_name": "Angola", "chinese_name": "安哥拉", "code": "ANG", "latitude": -11.202692, "longitude": 17.873887, "continent": "Africa"},
    {"id": 6, "english_name": "Antigua and Barbuda", "chinese_name": "安地卡及巴布達", "code": "ANT", "latitude": 17.060816, "longitude": -61.796428, "continent": "North America"},
    {"id": 7, "english_name": "Argentina", "chinese_name": "阿根廷", "code": "ARG", "latitude": -38.416097, "longitude": -63.616672, "continent": "South America"},
    {"id": 8, "english_name": "Armenia", "chinese_name": "亞美尼亞", "code": "ARM", "latitude": 40.069099, "longitude": 45.038189, "continent": "Asia"},
    {"id": 9, "english_name": "Australia", "chinese_name": "澳大利亞", "code": "AUS", "latitude": -25.274398, "longitude": 133.775136, "continent": "Oceania"},
    {"id": 10, "english_name": "Austria", "chinese_name": "奧地利", "code": "AUT", "latitude": 47.516231, "longitude": 14.550072, "continent": "Europe"},
    {"id": 11, "english_name": "Azerbaijan", "chinese_name": "亞塞拜然", "code": "AZE", "latitude": 40.143105, "longitude": 47.576927, "continent": "Asia"},
    {"id": 12, "english_name": "Bahamas", "chinese_name": "巴哈馬", "code": "BAH", "latitude": 25.03428, "longitude": -77.39628, "continent": "North America"},
    {"id": 13, "english_name": "Bahrain", "chinese_name": "巴林", "code": "BRN", "latitude": 26.0667, "longitude": 50.5577, "continent": "Asia"},
    {"id": 14, "english_name": "Bangladesh", "chinese_name": "孟加拉國", "code": "BAN", "latitude": 23.684994, "longitude": 90.356331, "continent": "Asia"},
    {"id": 15, "english_name": "Barbados", "chinese_name": "巴貝多", "code": "BAR", "latitude": 13.193887, "longitude": -59.543198, "continent": "North America"},
    {"id": 16, "english_name": "Belarus", "chinese_name": "白俄羅斯", "code": "BLR", "latitude": 53.900602, "longitude": 27.559, "continent": "Europe"},
    {"id": 17, "english_name": "Belgium", "chinese_name": "比利時", "code": "BEL", "latitude": 50.850346, "longitude": 4.351721, "continent": "Europe"},
    {"id": 18, "english_name": "Belize", "chinese_name": "貝里斯", "code": "BIZ", "latitude": 17.189877, "longitude": -88.49765, "continent": "North America"},
    {"id": 19, "english_name": "Benin", "chinese_name": "貝寧", "code": "BEN", "latitude": 9.30769, "longitude": 2.315834, "continent": "Africa"},
    {"id": 20, "english_name": "Bhutan", "chinese_name": "不丹", "code": "BHU", "latitude": 27.514162, "longitude": 90.433601, "continent": "Asia"},
    {"id": 21, "english_name": "Bolivia", "chinese_name": "玻利維亞", "code": "BOL", "latitude": -16.290154, "longitude": -63.588653, "continent": "South America"},
    {"id": 22, "english_name": "Bosnia and Herzegovina", "chinese_name": "波斯尼亞和赫塞哥維那", "code": "BIH", "latitude": 43.915886, "longitude": 17.679076, "continent": "Europe"},
    {"id": 23, "english_name": "Botswana", "chinese_name": "波札那", "code": "BOT", "latitude": -22.328474, "longitude": 24.684866, "continent": "Africa"},
    {"id": 24, "english_name": "Brazil", "chinese_name": "巴西", "code": "BRA", "latitude": -14.235004, "longitude": -51.92528, "continent": "South America"},
    {"id": 25, "english_name": "Brunei", "chinese_name": "汶萊", "code": "BRU", "latitude": 4.535277, "longitude": 114.727669, "continent": "Asia"},
    {"id": 26, "english_name": "Bulgaria", "chinese_name": "保加利亞", "code": "BUL", "latitude": 42.733883, "longitude": 25.48583, "continent": "Europe"},
    {"id": 27, "english_name": "Burkina Faso", "chinese_name": "布吉納法索", "code": "BUR", "latitude": 12.238333, "longitude": -1.561593, "continent": "Africa"},
    {"id": 28, "english_name": "Burundi", "chinese_name": "蒲隆地", "code": "BDI", "latitude": -3.373056, "longitude": 29.918886, "continent": "Africa"},
    {"id": 29, "english_name": "Cabo Verde", "chinese_name": "維德角", "code": "CPV", "latitude": 16.5388, "longitude": -23.0418, "continent": "Africa"},
    {"id": 30, "english_name": "Cambodia", "chinese_name": "柬埔寨", "code": "CAM", "latitude": 12.565679, "longitude": 104.990963, "continent": "Asia"},
    {"id": 31, "english_name": "Cameroon", "chinese_name": "喀麥隆", "code": "CMR", "latitude": 7.369722, "longitude": 12.354722, "continent": "Africa"},
    {"id": 32, "english_name": "Canada", "chinese_name": "加拿大", "code": "CAN", "latitude": 56.130366, "longitude": -106.346771, "continent": "North America"},
    {"id": 33, "english_name": "Central African Republic", "chinese_name": "中非共和國", "code": "CAF", "latitude": 6.611111, "longitude": 20.939444, "continent": "Africa"},
    {"id": 34, "english_name": "Chad", "chinese_name": "查德", "code": "CHA", "latitude": 15.454166, "longitude": 18.732207, "continent": "Africa"},
    {"id": 35, "english_name": "Chile", "chinese_name": "智利", "code": "CHI", "latitude": -35.675147, "longitude": -71.542969, "continent": "South America"},
    {"id": 36, "english_name": "China", "chinese_name": "中國", "code": "CHN", "latitude": 35.86166, "longitude": 104.195397, "continent": "Asia"},
    {"id": 37, "english_name": "Colombia", "chinese_name": "哥倫比亞", "code": "COL", "latitude": 4.570868, "longitude": -74.297333, "continent": "North America"},
    {"id": 38, "english_name": "Comoros", "chinese_name": "科摩羅", "code": "COM", "latitude": -11.6455, "longitude": 43.3333, "continent": "Asia"},
    {"id": 39, "english_name": "Congo", "chinese_name": "剛果", "code": "CGO", "latitude": -0.228021, "longitude": 15.827659, "continent": "Africa"},
    {"id": 40, "english_name": "Costa Rica", "chinese_name": "哥斯達黎加", "code": "CRC", "latitude": 9.6302, "longitude": -84.2542, "continent": "North America"},
    {"id": 41, "english_name": "Croatia", "chinese_name": "克羅埃西亞", "code": "CRO", "latitude": 45.1667, "longitude": 15.5000, "continent": "Europe"},
    {"id": 42, "english_name": "Cuba", "chinese_name": "古巴", "code": "CUB", "latitude": 21.5000, "longitude": -80.0000, "continent": "North America"},
    {"id": 44, "english_name": "Czech Republic", "chinese_name": "捷克", "code": "CZE", "latitude": 49.7419, "longitude": 15.3350, "continent": "Europe"},
    {"id": 45, "english_name": "Democratic Republic of the Congo", "chinese_name": "剛果民主共和國", "code": "COD", "latitude": -2.9814, "longitude": 23.8223, "continent": "Africa"},
    {"id": 46, "english_name": "Denmark", "chinese_name": "丹麥", "code": "DEN", "latitude": 56.0000, "longitude": 10.0000, "continent": "Europe"},
    {"id": 47, "english_name": "Djibouti", "chinese_name": "吉布地", "code": "DJI", "latitude": 11.7556, "longitude": 42.6043, "continent": "Asia"},
    {"id": 49, "english_name": "Dominican Republic", "chinese_name": "多明尼加", "code": "DOM", "latitude": 19.0000, "longitude": -70.6667, "continent": "North America"},
    {"id": 50, "english_name": "Ecuador", "chinese_name": "厄瓜多", "code": "ECU", "latitude": -1.4000, "longitude": -78.5000, "continent": "South America"},
    {"id": 53, "english_name": "Equatorial Guinea", "chinese_name": "赤道幾內亞", "code": "GEQ", "latitude": 1.5000, "longitude": 10.0000, "continent": "Africa"},
    {"id": 54, "english_name": "Eritrea", "chinese_name": "厄立垂亞", "code": "ERI", "latitude": 15.3333, "longitude": 39.0000, "continent": "Asia"},
    {"id": 56, "english_name": "Eswatini", "chinese_name": "史瓦帝尼", "code": "SWZ", "latitude": -26.5667, "longitude": 31.5000, "continent": "Asia"},
    {"id": 57, "english_name": "Ethiopia", "chinese_name": "衣索比亞", "code": "ETH", "latitude": 9.1450, "longitude": 40.4897, "continent": "Asia"},
    {"id": 59, "english_name": "Finland", "chinese_name": "芬蘭", "code": "FIN", "latitude": 62.0000, "longitude": 26.0000, "continent": "Europe"},
    {"id": 60, "english_name": "France", "chinese_name": "法國", "code": "FRA", "latitude": 46.6034, "longitude": 1.8883, "continent": "Europe"},
    {"id": 61, "english_name": "Gabon", "chinese_name": "加彭", "code": "GAB", "latitude": -0.8000, "longitude": 11.6094, "continent": "Africa"},
    {"id": 62, "english_name": "Gambia", "chinese_name": "甘比亞", "code": "GAM", "latitude": 13.4667, "longitude": -15.5000, "continent": "Africa"},
    {"id": 63, "english_name": "Georgia", "chinese_name": "喬治亞", "code": "GEO", "latitude": 42.0000, "longitude": 43.5000, "continent": "Asia"},
    {"id": 65, "english_name": "Ghana", "chinese_name": "迦納", "code": "GHA", "latitude": 7.9465, "longitude": -1.0232, "continent": "Africa"},
    {"id": 66, "english_name": "Greece", "chinese_name": "希臘", "code": "GRE", "latitude": 39.0000, "longitude": 22.0000, "continent": "Europe"},
    {"id": 68, "english_name": "Guatemala", "chinese_name": "瓜地馬拉", "code": "GUA", "latitude": 15.5000, "longitude": -90.0000, "continent": "North America"},
    {"id": 69, "english_name": "Guinea", "chinese_name": "幾內亞", "code": "GUI", "latitude": 10.8333, "longitude": -10.6667, "continent": "Africa"},
    {"id": 70, "english_name": "Guinea-Bissau", "chinese_name": "幾內亞比索", "code": "GBS", "latitude": 12.0000, "longitude": -15.2000, "continent": "Africa"},
    {"id": 71, "english_name": "Guyana", "chinese_name": "圭亞那", "code": "GUY", "latitude": 5.0000, "longitude": -59.0000, "continent": "North America"},
    {"id": 73, "english_name": "Honduras", "chinese_name": "宏都拉斯", "code": "HON", "latitude": 14.8000, "longitude": -86.3000, "continent": "North America"},
    {"id": 74, "english_name": "Hungary", "chinese_name": "匈牙利", "code": "HUN", "latitude": 47.1625, "longitude": 19.5033, "continent": "Europe"},
    {"id": 76, "english_name": "India", "chinese_name": "印度", "code": "IND", "latitude": 21.0000, "longitude": 78.0000, "continent": "Asia"},
    {"id": 77, "english_name": "Indonesia", "chinese_name": "印尼", "code": "INA", "latitude": -2.5000, "longitude": 118.0000, "continent": "Asia"},
    {"id": 78, "english_name": "Iran", "chinese_name": "伊朗", "code": "IRI", "latitude": 32.0000, "longitude": 53.0000, "continent": "Asia"},
    {"id": 79, "english_name": "Iraq", "chinese_name": "伊拉克", "code": "IRQ", "latitude": 33.0000, "longitude": 44.0000, "continent": "Asia"},
    {"id": 80, "english_name": "Ireland", "chinese_name": "愛爾蘭", "code": "IRL", "latitude": 53.4495, "longitude": -7.5029, "continent": "Europe"},
    {"id": 81, "english_name": "Israel", "chinese_name": "以色列", "code": "ISR", "latitude": 31.0461, "longitude": 34.8516, "continent": "Asia"},
    {"id": 82, "english_name": "Italy", "chinese_name": "義大利", "code": "ITA", "latitude": 42.6384, "longitude": 12.6743, "continent": "Europe"},
    {"id": 83, "english_name": "Jamaica", "chinese_name": "牙買加", "code": "JAM", "latitude": 18.1096, "longitude": -77.2975, "continent": "North America"},
    {"id": 84, "english_name": "Japan", "chinese_name": "日本", "code": "JPN", "latitude": 36.2048, "longitude": 138.2529, "continent": "Asia"},
    {"id": 85, "english_name": "Jordan", "chinese_name": "約旦", "code": "JOR", "latitude": 31.2400, "longitude": 36.3200, "continent": "Asia"},
    {"id": 86, "english_name": "Kazakhstan", "chinese_name": "哈薩克", "code": "KAZ", "latitude": 48.0196, "longitude": 66.9237, "continent": "Asia"},
    {"id": 87, "english_name": "Kenya", "chinese_name": "肯亞", "code": "KEN", "latitude": 0.8000, "longitude": 37.0000, "continent": "Asia"},
    {"id": 88, "english_name": "Kiribati", "chinese_name": "吉里巴斯", "code": "KIR", "latitude": 1.8709, "longitude": 157.4983, "continent": "Oceania"},
    {"id": 89, "english_name": "Kuwait", "chinese_name": "科威特", "code": "KUW", "latitude": 29.3117, "longitude": 47.4818, "continent": "Asia"},
    {"id": 90, "english_name": "Kyrgyzstan", "chinese_name": "吉爾吉斯", "code": "KGZ", "latitude": 41.2044, "longitude": 74.7661, "continent": "Asia"},
    {"id": 91, "english_name": "Laos", "chinese_name": "寮國", "code": "LAO", "latitude": 19.8563, "longitude": 102.4955, "continent": "Asia"},
    {"id": 92, "english_name": "Latvia", "chinese_name": "拉脫維亞", "code": "LAT", "latitude": 56.8796, "longitude": 24.6032, "continent": "Europe"},
    {"id": 93, "english_name": "Lebanon", "chinese_name": "黎巴嫩", "code": "LBN", "latitude": 33.8547, "longitude": 35.8623, "continent": "Asia"},
    {"id": 94, "english_name": "Lesotho", "chinese_name": "賴索托", "code": "LES", "latitude": -29.6099, "longitude": 28.2336, "continent": "Africa"},
    {"id": 95, "english_name": "Liberia", "chinese_name": "賴比瑞亞", "code": "LBR", "latitude": 6.4281, "longitude": -9.4295, "continent": "Africa"},
    {"id": 96, "english_name": "Libya", "chinese_name": "利比亞", "code": "LBA", "latitude": 26.3351, "longitude": 17.2283, "continent": "Africa"},
    {"id": 97, "english_name": "Liechtenstein", "chinese_name": "列支敦士登", "code": "LIE", "latitude": 47.1660, "longitude": 9.5554, "continent": "Europe"},
    {"id": 98, "english_name": "Lithuania", "chinese_name": "立陶宛", "code": "LTU", "latitude": 55.1694, "longitude": 23.8813, "continent": "Europe"},
    {"id": 99, "english_name": "Luxembourg", "chinese_name": "盧森堡", "code": "LUX", "latitude": 49.8153, "longitude": 6.1296, "continent": "Europe"},
    {"id": 100, "english_name": "Madagascar", "chinese_name": "馬達加斯加", "code": "MAD", "latitude": -18.7669, "longitude": 46.8691, "continent": "Asia"},
    {"id": 101, "english_name": "Malawi", "chinese_name": "馬拉威", "code": "MAW", "latitude": -13.2543, "longitude": 34.3015, "continent": "Asia"},
    {"id": 102, "english_name": "Malaysia", "chinese_name": "馬來西亞", "code": "MAS", "latitude": 4.2105, "longitude": 101.9758, "continent": "Asia"},
    {"id": 103, "english_name": "Maldives", "chinese_name": "馬爾地夫", "code": "MDV", "latitude": 3.2028, "longitude": 73.2207, "continent": "Asia"},
    {"id": 104, "english_name": "Mali", "chinese_name": "馬利", "code": "MLI", "latitude": 17.5707, "longitude": -3.9962, "continent": "Africa"},
    {"id": 105, "english_name": "Malta", "chinese_name": "馬爾他", "code": "MLT", "latitude": 35.9375, "longitude": 14.3754, "continent": "Africa"},
    {"id": 106, "english_name": "Marshall Islands", "chinese_name": "馬紹爾群島", "code": "MHL", "latitude": 7.1315, "longitude": 171.1845, "continent": "Oceania"},
    {"id": 107, "english_name": "Mauritania", "chinese_name": "茅利塔尼亞", "code": "MTN", "latitude": 21.0079, "longitude": -10.9408, "continent": "Africa"},
    {"id": 108, "english_name": "Mauritius", "chinese_name": "模里西斯", "code": "MRI", "latitude": -20.3484, "longitude": 57.5522, "continent": "Asia"},
    {"id": 109, "english_name": "Mexico", "chinese_name": "墨西哥", "code": "MEX", "latitude": 23.6345, "longitude": -102.5528, "continent": "North America"},
    {"id": 110, "english_name": "Micronesia", "chinese_name": "密克羅尼西亞", "code": "FSM", "latitude": 7.4256, "longitude": 150.5508, "continent": "Oceania"},
    {"id": 111, "english_name": "Moldova", "chinese_name": "摩爾多瓦", "code": "MDA", "latitude": 47.4116, "longitude": 28.3699, "continent": "Europe"},
    {"id": 112, "english_name": "Monaco", "chinese_name": "摩納哥", "code": "MON", "latitude": 43.7333, "longitude": 7.4167, "continent": "Europe"},
    {"id": 113, "english_name": "Mongolia", "chinese_name": "蒙古", "code": "MGL", "latitude": 46.8625, "longitude": 103.8467, "continent": "Asia"},
    {"id": 114, "english_name": "Montenegro", "chinese_name": "蒙特內哥羅", "code": "MNE", "latitude": 42.7087, "longitude": 19.3744, "continent": "Europe"},
    {"id": 115, "english_name": "Morocco", "chinese_name": "摩洛哥", "code": "MAR", "latitude": 31.7917, "longitude": -7.0926, "continent": "Africa"},
    {"id": 116, "english_name": "Mozambique", "chinese_name": "莫三比克", "code": "MOZ", "latitude": -18.6657, "longitude": 35.5296, "continent": "Asia"},
    {"id": 117, "english_name": "Myanmar", "chinese_name": "緬甸", "code": "MYA", "latitude": 21.9162, "longitude": 95.9560, "continent": "Asia"},
    {"id": 118, "english_name": "Namibia", "chinese_name": "那米比亞", "code": "NAM", "latitude": -22.9576, "longitude": 18.4904, "continent": "Africa"},
    {"id": 119, "english_name": "Nauru", "chinese_name": "諾魯", "code": "NRU", "latitude": -0.5228, "longitude": 166.9315, "continent": "Oceania"},
    {"id": 120, "english_name": "Nepal", "chinese_name": "尼泊爾", "code": "NEP", "latitude": 28.3949, "longitude": 84.1240, "continent": "Asia"},
    {"id": 121, "english_name": "Netherlands", "chinese_name": "荷蘭", "code": "NED", "latitude": 52.1326, "longitude": 5.2913, "continent": "Europe"},
    {"id": 122, "english_name": "New Zealand", "chinese_name": "紐西蘭", "code": "NZL", "latitude": -41.0151, "longitude": 172.7700, "continent": "Oceania"},
    {"id": 123, "english_name": "Nicaragua", "chinese_name": "尼加拉瓜", "code": "NCA", "latitude": 12.8654, "longitude": -85.2072, "continent": "North America"},
    {"id": 124, "english_name": "Niger", "chinese_name": "尼日", "code": "NIG", "latitude": 17.6078, "longitude": 8.0817, "continent": "Africa"},
    {"id": 125, "english_name": "Nigeria", "chinese_name": "奈及利亞", "code": "NGR", "latitude": 9.0820, "longitude": 8.6753, "continent": "Africa"},
    {"id": 126, "english_name": "North Macedonia", "chinese_name": "北馬其頓", "code": "MKD", "latitude": 41.6086, "longitude": 21.7453, "continent": "Europe"},
    {"id": 127, "english_name": "Norway", "chinese_name": "挪威", "code": "NOR", "latitude": 60.4720, "longitude": 8.4689, "continent": "Europe"},
    {"id": 128, "english_name": "Oman", "chinese_name": "阿曼", "code": "OMA", "latitude": 21.5126, "longitude": 55.9233, "continent": "Asia"},
    {"id": 129, "english_name": "Pakistan", "chinese_name": "巴基斯坦", "code": "PAK", "latitude": 30.3753, "longitude": 69.3451, "continent": "Asia"},
    {"id": 130, "english_name": "Palau", "chinese_name": "帛琉", "code": "PLW", "latitude": 7.5150, "longitude": 134.5825, "continent": "Oceania"},
    {"id": 131, "english_name": "Palestine", "chinese_name": "巴勒斯坦", "code": "PLE", "latitude": 31.9522, "longitude": 35.2332, "continent": "Asia"},
    {"id": 132, "english_name": "Panama", "chinese_name": "巴拿馬", "code": "PAN", "latitude": 8.5380, "longitude": -80.7821, "continent": "North America"},
    {"id": 133, "english_name": "Papua New Guinea", "chinese_name": "巴布亞紐幾內亞", "code": "PNG", "latitude": -6.3149, "longitude": 143.9555, "continent": "Oceania"},
    {"id": 134, "english_name": "Paraguay", "chinese_name": "巴拉圭", "code": "PAR", "latitude": -23.4425, "longitude": -58.4438, "continent": "South America"},
    {"id": 135, "english_name": "Peru", "chinese_name": "秘魯", "code": "PER", "latitude": -9.1900, "longitude": -75.0152, "continent": "South America"},
    {"id": 136, "english_name": "Philippines", "chinese_name": "菲律賓", "code": "PHI", "latitude": 12.8797, "longitude": 121.7740, "continent": "Asia"},
    {"id": 137, "english_name": "Poland", "chinese_name": "波蘭", "code": "POL", "latitude": 51.9194, "longitude": 19.1451, "continent": "Europe"},
    {"id": 138, "english_name": "Portugal", "chinese_name": "葡萄牙", "code": "POR", "latitude": 39.3999, "longitude": -8.2245, "continent": "Europe"},
    {"id": 139, "english_name": "Qatar", "chinese_name": "卡達", "code": "QAT", "latitude": 25.3548, "longitude": 51.1839, "continent": "Asia"},
    {"id": 140, "english_name": "Romania", "chinese_name": "羅馬尼亞", "code": "ROU", "latitude": 45.9432, "longitude": 24.9668, "continent": "Europe"},
    {"id": 141, "english_name": "Russian Federation", "chinese_name": "俄羅斯", "code": "RUS", "latitude": 61.5240, "longitude": 105.3188, "continent": "Asia"},
    {"id": 142, "english_name": "Rwanda", "chinese_name": "盧安達", "code": "RWA", "latitude": -1.9403, "longitude": 29.8739, "continent": "Africa"},
    {"id": 143, "english_name": "Saint Kitts and Nevis", "chinese_name": "聖克里斯多福及尼維斯", "code": "SKN", "latitude": 17.3578, "longitude": -62.7829, "continent": "North America"},
    {"id": 144, "english_name": "Saint Lucia", "chinese_name": "聖露西亞", "code": "LCA", "latitude": 13.9094, "longitude": -60.9789, "continent": "North America"},
    {"id": 145, "english_name": "Saint Vincent and the Grenadines", "chinese_name": "聖文森及格瑞那丁", "code": "VIN", "latitude": 12.9843, "longitude": -61.2872, "continent": "North America"},
    {"id": 146, "english_name": "Samoa", "chinese_name": "薩摩亞", "code": "SAM", "latitude": -13.7590, "longitude": -172.1046, "continent": "Oceania"},
    {"id": 147, "english_name": "San Marino", "chinese_name": "聖馬利諾", "code": "SMR", "latitude": 43.9333, "longitude": 12.4501, "continent": "Europe"},
    {"id": 148, "english_name": "Sao Tome and Principe", "chinese_name": "聖多美普林西比", "code": "STP", "latitude": 0.1864, "longitude": 6.6131, "continent": "Africa"},
    {"id": 149, "english_name": "Saudi Arabia", "chinese_name": "沙烏地阿拉伯", "code": "KSA", "latitude": 23.8859, "longitude": 45.0792, "continent": "Asia"},
    {"id": 150, "english_name": "Senegal", "chinese_name": "塞內加爾", "code": "SEN", "latitude": 14.4974, "longitude": -14.4524, "continent": "Africa"},
    {"id": 151, "english_name": "Serbia", "chinese_name": "塞爾維亞", "code": "SRB", "latitude": 44.0165, "longitude": 21.0059, "continent": "Europe"},
    {"id": 152, "english_name": "Seychelles", "chinese_name": "塞席爾", "code": "SEY", "latitude": -4.6796, "longitude": 55.4920, "continent": "Asia"},
    {"id": 153, "english_name": "Sierra Leone", "chinese_name": "獅子山", "code": "SLE", "latitude": 8.4606, "longitude": -11.7799, "continent": "Africa"},
    {"id": 154, "english_name": "Singapore", "chinese_name": "新加坡", "code": "SGP", "latitude": 1.3521, "longitude": 103.8198, "continent": "Asia"},
    {"id": 155, "english_name": "Slovakia", "chinese_name": "斯洛伐克", "code": "SVK", "latitude": 48.6690, "longitude": 19.6990, "continent": "Europe"},
    {"id": 156, "english_name": "Slovenia", "chinese_name": "斯洛維尼亞", "code": "SLO", "latitude": 46.1512, "longitude": 14.9955, "continent": "Europe"},
    {"id": 157, "english_name": "Solomon Islands", "chinese_name": "索羅門群島", "code": "SOL", "latitude": -9.6457, "longitude": 160.1562, "continent": "Oceania"},
    {"id": 158, "english_name": "Somalia", "chinese_name": "索馬利亞", "code": "SOM", "latitude": 5.1521, "longitude": 46.1996, "continent": "Asia"},
    {"id": 159, "english_name": "South Africa", "chinese_name": "南非", "code": "RSA", "latitude": -30.5595, "longitude": 22.9375, "continent": "Africa"},
    {"id": 160, "english_name": "South Korea", "chinese_name": "南韓", "code": "KOR", "latitude": 35.9078, "longitude": 127.7669, "continent": "Asia"},
    {"id": 161, "english_name": "South Sudan", "chinese_name": "南蘇丹", "code": "SSD", "latitude": 6.877, "longitude": 31.307, "continent": "Africa"},
    {"id": 162, "english_name": "Spain", "chinese_name": "西班牙", "code": "ESP", "latitude": 40.4637, "longitude": -3.7492, "continent": "Europe"},
    {"id": 163, "english_name": "Sri Lanka", "chinese_name": "斯里蘭卡", "code": "SRI", "latitude": 7.8731, "longitude": 80.7718, "continent": "Asia"},
    {"id": 164, "english_name": "Sudan", "chinese_name": "蘇丹", "code": "SUD", "latitude": 12.8628, "longitude": 30.2176, "continent": "Africa"},
    {"id": 165, "english_name": "Suriname", "chinese_name": "蘇利南", "code": "SUR", "latitude": 3.9193, "longitude": -56.0278, "continent": "South America"},
    {"id": 166, "english_name": "Sweden", "chinese_name": "瑞典", "code": "SWE", "latitude": 60.1282, "longitude": 18.6435, "continent": "Europe"},
    {"id": 167, "english_name": "Switzerland", "chinese_name": "瑞士", "code": "SUI", "latitude": 46.8182, "longitude": 8.2275, "continent": "Europe"},
    {"id": 168, "english_name": "Syria", "chinese_name": "敘利亞", "code": "SYR", "latitude": 34.8021, "longitude": 38.9968, "continent": "Asia"},
    {"id": 169, "english_name": "Tajikistan", "chinese_name": "塔吉克", "code": "TJK", "latitude": 38.861, "longitude": 71.2761, "continent": "Asia"},
    {"id": 170, "english_name": "Tanzania", "chinese_name": "坦尚尼亞", "code": "TAN", "latitude": -6.369, "longitude": 34.8888, "continent": "Africa"},
    {"id": 171, "english_name": "Thailand", "chinese_name": "泰國", "code": "THA", "latitude": 15.87, "longitude": 100.9925, "continent": "Asia"},
    {"id": 172, "english_name": "Timor-Leste", "chinese_name": "東帝汶", "code": "TLS", "latitude": -8.8742, "longitude": 125.7275, "continent": "Asia"},
    {"id": 173, "english_name": "Togo", "chinese_name": "多哥", "code": "TOG", "latitude": 8.6195, "longitude": 0.8248, "continent": "Africa"},
    {"id": 174, "english_name": "Tonga", "chinese_name": "東加", "code": "TGA", "latitude": -21.1789, "longitude": -175.1982, "continent": "Oceania"},
    {"id": 175, "english_name": "Trinidad and Tobago", "chinese_name": "千里達及多巴哥", "code": "TTO", "latitude": 10.6918, "longitude": -61.2225, "continent": "North America"},
    {"id": 176, "english_name": "Tunisia", "chinese_name": "突尼西亞", "code": "TUN", "latitude": 33.8869, "longitude": 9.5375, "continent": "Africa"},
    {"id": 177, "english_name": "Turkey", "chinese_name": "土耳其", "code": "TUR", "latitude": 38.9637, "longitude": 35.2433, "continent": "Asia"},
    {"id": 178, "english_name": "Turkmenistan", "chinese_name": "土庫曼", "code": "TKM", "latitude": 38.9697, "longitude": 59.5563, "continent": "Asia"},
    {"id": 179, "english_name": "Tuvalu", "chinese_name": "吐瓦魯", "code": "TUV", "latitude": -7.1095, "longitude": 177.6493, "continent": "Oceania"},
    {"id": 180, "english_name": "Uganda", "chinese_name": "烏干達", "code": "UGA", "latitude": 1.3733, "longitude": 32.2903, "continent": "Africa"},
    {"id": 181, "english_name": "Ukraine", "chinese_name": "烏克蘭", "code": "UKR", "latitude": 48.3794, "longitude": 31.1656, "continent": "Europe"},
    {"id": 182, "english_name": "United Arab Emirates", "chinese_name": "阿拉伯聯合大公國", "code": "UAE", "latitude": 23.4241, "longitude": 53.8478, "continent": "Asia"},
    {"id": 183, "english_name": "United Kingdom", "chinese_name": "英國", "code": "GBR", "latitude": 55.3781, "longitude": -3.436, "continent": "Europe"},
    {"id": 184, "english_name": "United States", "chinese_name": "美國", "code": "USA", "latitude": 37.0902, "longitude": -95.7129, "continent": "North America"},
    {"id": 185, "english_name": "Uruguay", "chinese_name": "烏拉圭", "code": "URU", "latitude": -32.5228, "longitude": -55.7658, "continent": "South America"},
    {"id": 186, "english_name": "Uzbekistan", "chinese_name": "烏茲別克", "code": "UZB", "latitude": 41.3775, "longitude": 64.5853, "continent": "Asia"},
    {"id": 187, "english_name": "Vanuatu", "chinese_name": "萬那杜", "code": "VAN", "latitude": -15.3767, "longitude": 166.9592, "continent": "Oceania"},
    {"id": 188, "english_name": "Vatican City", "chinese_name": "梵蒂岡", "code": "VAT", "latitude": 41.9029, "longitude": 12.4534, "continent": "Europe"},
    {"id": 189, "english_name": "Venezuela", "chinese_name": "委內瑞拉", "code": "VEN", "latitude": 6.4238, "longitude": -66.5897, "continent": "North America"},
    {"id": 190, "english_name": "Vietnam", "chinese_name": "越南", "code": "VIE", "latitude": 14.0583, "longitude": 108.2772, "continent": "Asia"},
    {"id": 191, "english_name": "Yemen", "chinese_name": "葉門", "code": "YEM", "latitude": 15.5527, "longitude": 48.5164, "continent": "Asia"},
    {"id": 192, "english_name": "Zambia", "chinese_name": "尚比亞", "code": "ZAM", "latitude": -13.1339, "longitude": 27.8493, "continent": "Africa"},
    {"id": 193, "english_name": "Zimbabwe", "chinese_name": "辛巴威", "code": "ZIM", "latitude": -19.0154, "longitude": 29.1549, "continent": "Africa"},
    {"id": 194, "english_name": "American Samoa", "chinese_name": "美屬薩摩亞", "code": "ASA", "latitude": -14.271, "longitude": -170.1322, "continent": "Oceania"},
    {"id": 195, "english_name": "Guam", "chinese_name": "關島", "code": "GUM", "latitude": 13.4443, "longitude": 144.7937, "continent": "Oceania"},
    {"id": 196, "english_name": "Puerto Rico", "chinese_name": "波多黎各", "code": "PUR", "latitude": 18.2208, "longitude": -66.5901, "continent": "North America"},
    {"id": 197, "english_name": "Hong Kong", "chinese_name": "香港", "code": "HKG", "latitude": 22.3193, "longitude": 114.1694, "continent": "Asia"},
    {"id": 198, "english_name": "Macau", "chinese_name": "澳門", "code": "MAC", "latitude": 22.1987, "longitude": 113.5439, "continent": "Asia"},
    {"id": 199, "english_name": "Palestine", "chinese_name": "巴勒斯坦", "code": "PLE", "latitude": 31.9522, "longitude": 35.2332, "continent": "Asia"},
    {"id": 200, "english_name": "Cook Islands", "chinese_name": "庫克群島", "code": "COK", "latitude": -21.2367, "longitude": -159.777, "continent": "Oceania"},
    {"id": 201, "english_name": "Aruba", "chinese_name": "阿魯巴", "code": "ARU", "latitude": 12.5211, "longitude": -69.9683, "continent": "North America"},
    {"id": 202, "english_name": "Bermuda", "chinese_name": "百慕達", "code": "BER", "latitude": 32.3078, "longitude": -64.7505, "continent": "North America"},
    {"id": 203, "english_name": "Cayman Islands", "chinese_name": "開曼群島", "code": "CAY", "latitude": 19.3133, "longitude": -81.2546, "continent": "North America"},
    {"id": 204, "english_name": "British Virgin Islands", "chinese_name": "英屬維京群島", "code": "IVB", "latitude": 18.4207, "longitude": -64.6399, "continent": "North America"},
    {"id": 205, "english_name": "Turks and Caicos Islands", "chinese_name": "特克斯與凱科斯群島", "code": "TCA", "latitude": 21.694, "longitude": -71.7979, "continent": "North America"},
    {"id": 206, "english_name": "Montserrat", "chinese_name": "蒙特塞拉特", "code": "MNT", "latitude": 16.7425, "longitude": -62.1874, "continent": "North America"},
    {"id": 207, "english_name": "Falkland Islands", "chinese_name": "福克蘭群島", "code": "FLK", "latitude": -51.7963, "longitude": -59.5236, "continent": "South America"},
    {"id": 208, "english_name": "Ivory Coast", "chinese_name": "象牙海岸", "code": "CIV", "latitude": 7.54, "longitude": -5.55, "continent": "Africa"},
    {"id": 999, "english_name": "Chinese Taipei", "chinese_name": "中華台北", "code": "TPE", "latitude": 23.6978, "longitude": 120.9605, "continent": "Asia"}
]

import pandas as pd

# 將資料轉為 DataFrame
df_olympic_countries = pd.DataFrame(olympic_countries)

# ===== 模擬資料結構（請替換為你實際的）=====
DROPDOWN_OPTIONS = {
    "勝者國家": [
        ("勝者國家>Ippon技術分類地圖", "勝者國家>Ippon技術分類地圖"),
        ("勝者國家>Ippon技術地圖", "勝者國家>Ippon技術地圖"),
    ],
}

SECONDARY_DROPDOWN_MAP = {
    "勝者國家>Ippon技術分類地圖": ["全部Ippon比賽",
                            "男子有Ippon比賽",
                            "女子有Ippon比賽"],
    "勝者國家>Ippon技術地圖": ["全部Ippon比賽",
                            "男子有Ippon比賽",
                            "女子有Ippon比賽"],
}

YEARS_DATA = [
    {"year": "24", "game": "olympics", "label": "24奧運", "source_sheet_id": "18qRVPHn9o-3I0ewCaGFxpHYfL1duN7Pq66NLuchkSm0"},
    {"year": "20", "game": "olympics", "label": "20奧運", "source_sheet_id": "1kk2sI_grQKPUo3ibBsXIk7NOXSC3IyGSc9xzM5MoLmg"},
    {"year": "16", "game": "olympics", "label": "16奧運", "source_sheet_id": "1TeCEposDKZHLeXabM06dJkksB9F8qsYjy3ZJfP04c_A"},
    {"year": "24", "game": "championships", "label": "24世錦", "source_sheet_id": "1dF_VlluGM-dTn8oJ_v3vk7NDYYr6kz0b9fDc9LMq4dE"},
    {"year": "23", "game": "championships", "label": "23世錦", "source_sheet_id": "1VwCnLXG0cHznP7i9wjOlfhToauPIt1VKpIj0hZ4Yxvw"},
    {"year": "22", "game": "championships", "label": "22世錦", "source_sheet_id": "1CWj7xY9N7fM6HghhNHrFgP7N4mturbGgOP5axIaG2QU"},
    {"year": "21", "game": "championships", "label": "21世錦", "source_sheet_id": "1Nf4QBY901h8BE7V2cKYhiae5rzQyJErXv6opmBfK2lI"},
    {"year": "19", "game": "championships", "label": "19世錦", "source_sheet_id": "1XJS1FKOQLztddPh54z32nuhyIxidr20Y7uw_u3UmpNQ"},
    {"year": "18", "game": "championships", "label": "18世錦", "source_sheet_id": "1pQsSvrtBL_AXfrDhrOhcuq9S_gv_Ipur3QfcxiSpJ3g"},
    {"year": "17", "game": "championships", "label": "17世錦", "source_sheet_id": "1BEzcYM8phoaimrzGcVEAN69ZPg8UxWpyPVAv9kSQaAM"},
]

JUDO_TECHNIQUE = {
  "AGR": {"en": "Ashi-garami", "zh": "足緘", "jp": "足緘", "group": "固技:関節技"},
  "AGU": {"en": "Ashi-guruma", "zh": "足車", "jp": "足車", "group": "投技:立技:足技"},
  "ASG": {"en": "Ashi-gatame", "zh": "足固", "jp": "足固め", "group": "固技:抑技"},
  "DAB": {"en": "De-ashi-barai", "zh": "出足払", "jp": "出足払い", "group": "投技:立技:足技"},
  "DAH": {"en": "De-ashi-harai", "zh": "出足払", "jp": "出足払い", "group": "投技:立技:足技"},
  "DKW": {"en": "Daki-wakare", "zh": "抱分", "jp": "抱分かれ", "group": "投技:捨身技:前捨身技"},
  "FUS": {"en": "Fusen-gachi", "zh": "不戰勝", "jp": "不戦勝ち", "group": "未分群"},
  "GJJ": {"en": "Gyaku-juji-jime", "zh": "逆十字絞", "jp": "逆十字絞め", "group": "固技:絞技"},
  "HAD": {"en": "Hadaka-jime", "zh": "裸絞", "jp": "裸絞め", "group": "固技:絞技"},
  "HGT": {"en": "Hara-gatame", "zh": "腹固", "jp": "腹固め", "group": "固技:抑技"},
  "HGG": {"en": "Harai-goshi-gaeshi", "zh": "払腰返", "jp": "払腰返し", "group": "投技:捨身技:前捨身技"},
  "HIG": {"en": "Ude-hishigi-hiza-gatame", "zh": "腕挫膝固", "jp": "腕挫膝固め", "group": "固技:関節技"},
  "HKG": {"en": "Hikikomi-gaeshi", "zh": "引込返", "jp": "引込返し", "group": "投技:捨身技:前捨身技"},
  "HRG": {"en": "Harai-goshi", "zh": "払腰", "jp": "払い腰", "group": "投技:立技:腰技"},
  "HRM": {"en": "Harai-makikomi", "zh": "払巻込", "jp": "払い巻き込み", "group": "投技:捨身技:橫捨身技"},
  "HMK": {"en": "Hane-makikomi", "zh": "跳卷込", "jp": "跳ね巻き込み", "group": "投技:捨身技:橫捨身技"},
  "HTA": {"en": "Harai-tsurikomi-ashi", "zh": "払釣込足", "jp": "払釣り込み足", "group": "投技:立技:足技"},
  "HZG": {"en": "Hiza-guruma", "zh": "膝車", "jp": "膝車", "group": "投技:立技:足技"},
  "HZT": {"en": "Hiza-gatame", "zh": "膝固", "jp": "膝固め", "group": "固技:抑技"},
  "ISN": {"en": "Ippon-seoi-nage", "zh": "一本背負投", "jp": "一本背負い投げ", "group": "投技:立技:手技"},
  "JG": {"en": "Ude-hishigi-juji-gatame", "zh": "腕挫十字固", "jp": "腕挫十字固め", "group": "固技:関節技"},
  "JGA": {"en": "Juji-gatame", "zh": "十字固", "jp": "十字固め", "group": "固技:抑技"},
  "JGT": {"en": "Ude-hishigi-juji-gatame", "zh": "腕挫十字固", "jp": "腕挫十字固め", "group": "固技:関節技"},
  "KAG": {"en": "Kata-gatame", "zh": "肩固", "jp": "肩固め", "group": "固技:抑技"},
  "KCG": {"en": "Ko-uchi-gaeshi", "zh": "小內返", "jp": "小内返し", "group": "投技:立技:不分群"},
  "KEG": {"en": "Kesa-gatame", "zh": "袈裟固", "jp": "袈裟固め", "group": "固技:抑技"},
  "KGU": {"en": "Kata-guruma", "zh": "肩車", "jp": "肩車", "group": "投技:立技:不分群"},
  "KHJ": {"en": "Kataha-jime", "zh": "片羽絞", "jp": "片羽絞め", "group": "固技:絞技"},
  "KIK": {"en": "Kiken-gachi", "zh": "棄權勝", "jp": "棄権勝ち", "group": "未分群"},
  "KJJ": {"en": "Kata-juji-jime", "zh": "片十字絞", "jp": "片十字絞め", "group": "固技:絞技"},
  "KKE": {"en": "Kuzure-kesa-gatame", "zh": "崩袈裟固", "jp": "崩れ袈裟固め", "group": "固技:抑技"},
  "KKS": {"en": "Kuzure-kami-shiho-gatame", "zh": "崩上四方固", "jp": "崩れ上四方固め", "group": "固技:抑技"},
  "KOG": {"en": "Koshi-guruma", "zh": "腰車", "jp": "腰車", "group": "投技:立技:腰技"},
  "KSG": {"en": "Ko-soto-gari", "zh": "小外刈", "jp": "小外刈り", "group": "投技:立技:足技"},
  "KSH": {"en": "Kami-shiho-gatame", "zh": "上四方固", "jp": "上四方固め", "group": "固技:抑技"},
  "KSK": {"en": "Ko-soto-gake", "zh": "小外掛", "jp": "小外掛け", "group": "投技:立技:足技"},
  "KTJ": {"en": "Katate-jime", "zh": "片手絞", "jp": "片手絞め", "group": "固技:絞技"},
  "KUG": {"en": "Ko-uchi-gari", "zh": "小內刈", "jp": "小内刈り", "group": "投技:立技:足技"},
  "KUM": {"en": "Ko-uchi-makikomi", "zh": "小內巻込", "jp": "小内巻き込み", "group": "投技:捨身技:橫捨身技"},
  "OAH": {"en": "Okuri-ashi-harai", "zh": "送足払", "jp": "送り足払い", "group": "投技:立技:足技"},
  "OEJ": {"en": "Okuri-eri-jime", "zh": "送襟絞", "jp": "送り襟絞め", "group": "固技:絞技"},
  "OGA": {"en": "O-soto-gaeshi", "zh": "大外返", "jp": "大外返し", "group": "投技:立技:足技"},
  "OGM": {"en": "O-guruma", "zh": "大車", "jp": "大車", "group": "投技:立技:足技"},
  "OGO": {"en": "O-goshi", "zh": "大腰", "jp": "大腰", "group": "投技:立技:腰技"},
  "OSA": {"en": "Osaekomi", "zh": "壓制", "jp": "抑え込み", "group": "固技:抑技"},
  "OSG": {"en": "O-soto-gari", "zh": "大外刈", "jp": "大外刈り", "group": "投技:立技:足技"},
  "OSM": {"en": "O-soto-makikomi", "zh": "大外巻込", "jp": "大外巻き込み", "group": "投技:捨身技:橫捨身技"},
  "OSO": {"en": "O-soto-otoshi", "zh": "大外落", "jp": "大外落とし", "group": "投技:立技:手技"},
  "OSU": {"en": "O-soto-guruma", "zh": "大外車", "jp": "大外車", "group": "投技:立技:足技"},
  "OTG": {"en": "Obi-tori-gaeshi", "zh": "帶取返", "jp": "帯取返し", "group": "投技:捨身技:前捨身技"},
  "OUC": {"en": "O-uchi-gaeshi", "zh": "大內返", "jp": "大内返し", "group": "投技:立技:不分群"},
  "OUG": {"en": "O-uchi-gari", "zh": "大內刈", "jp": "大内刈り", "group": "投技:立技:足技"},
  "SAJ": {"en": "Sankaku-jime", "zh": "三角絞", "jp": "三角絞め", "group": "固技:絞技"},
  "SEI": {"en": "Seoi-nage", "zh": "背負投", "jp": "背負い投げ", "group": "投技:立技:手技"},
  "SGJ": {"en": "Sode-guruma-jime", "zh": "袖車絞", "jp": "袖車絞め", "group": "固技:絞技"},
  "SGT": {"en": "Ude-hishigi-sankaku-gatame", "zh": "腕挫三角固", "jp": "腕挫三角固め", "group": "固技:関節技"},
  "SKG": {"en": "Sankaku-gatame", "zh": "三角固", "jp": "三角固め", "group": "固技:抑技"},
  "SMK": {"en": "Soto-makikomi", "zh": "外巻込", "jp": "外巻き込み", "group": "投技:立技:不分群"},
  "SON": {"en": "Seoi-nage", "zh": "背負投", "jp": "背負い投げ", "group": "投技:立技:手技"},
  "SOO": {"en": "Seoi-otoshi", "zh": "背負落", "jp": "背負い落とし", "group": "投技:立技:手技"},
  "SOT": {"en": "Sumi-otoshi", "zh": "隅落", "jp": "隅落とし", "group": "投技:立技:手技"},
  "STA": {"en": "Sasae-tsurikomi-ashi", "zh": "支釣込足", "jp": "支え釣り込み足", "group": "投技:立技:足技"},
  "STG": {"en": "Sode-tsurikomi-goshi", "zh": "袖釣込腰", "jp": "袖釣り込み腰", "group": "投技:立技:腰技"},
  "SUG": {"en": "Sumi-gaeshi", "zh": "隅返", "jp": "隅返し", "group": "投技:捨身技:前捨身技"},
  "SUK": {"en": "Sukui-nage", "zh": "掬投", "jp": "掬い投げ", "group": "投技:立技:手技"},
  "TGO": {"en": "Tsuri-goshi", "zh": "釣腰", "jp": "釣り腰", "group": "投技:立技:腰技"},
  "TGT": {"en": "Ude-hishigi-te-gatame", "zh": "腕挫手固", "jp": "腕挫手固め", "group": "固技:抑技"},
  "TKG": {"en": "Tsurikomi-goshi", "zh": "釣込腰", "jp": "釣り込み腰", "group": "投技:立技:腰技"},
  "TNG": {"en": "Tomoe-nage", "zh": "巴投", "jp": "巴投げ", "group": "投技:捨身技:前捨身技"},
  "TNO": {"en": "Tani-otoshi", "zh": "谷落", "jp": "谷落とし", "group": "投技:捨身技:前捨身技"},
  "TOS": {"en": "Tai-otoshi", "zh": "體落", "jp": "体落とし", "group": "投技:立技:手技"},
  "TSG": {"en": "Tate-shiho-gatame", "zh": "縱四方固", "jp": "縦四方固め", "group": "固技:抑技"},
  "TSU": {"en": "Tsubame-gaeshi", "zh": "燕返", "jp": "燕返し", "group": "投技:立技:不分群"},
  "TWG": {"en": "Tawara-gaeshi", "zh": "俵返", "jp": "俵返し", "group": "投技:捨身技:前捨身技"},
  "UDG": {"en": "Ude-gatame", "zh": "腕固", "jp": "腕固め", "group": "固技:抑技"},
  "UGA": {"en": "Ude-hishigi-ude-gatame", "zh": "腕挫腕固", "jp": "腕挫腕固め", "group": "固技:関節技"},
  "UGR": {"en": "Ude-garami", "zh": "腕緘", "jp": "腕緘", "group": "固技:関節技"},
  "UGT": {"en": "Uki-gatame", "zh": "浮固", "jp": "浮固め", "group": "固技:抑技"},
  "UKG": {"en": "Ushiro-kesa-gatame", "zh": "後袈裟固", "jp": "後ろ袈裟固め", "group": "固技:抑技"},
  "UKI": {"en": "Uki-goshi", "zh": "浮腰", "jp": "浮腰", "group": "投技:立技:腰技"},
  "USG": {"en": "Ushiro-goshi", "zh": "後腰", "jp": "後腰", "group": "投技:捨身技:後捨身技"},
  "UMA": {"en": "Uchi-mata", "zh": "內股", "jp": "内股", "group": "投技:立技:不分群"},
  "UMG": {"en": "Uchi-mata-gaeshi", "zh": "內股返", "jp": "内股返し", "group": "投技:捨身技:前捨身技"},
  "UMK": {"en": "Uchi-makikomi", "zh": "內巻込", "jp": "内巻き込み", "group": "投技:捨身技:橫捨身技"},
  "UMM": {"en": "Uchi-mata-makikomi", "zh": "內股巻込", "jp": "内股巻き込み", "group": "投技:捨身技:橫捨身技"},
  "UMS": {"en": "Uchi-mata-sukashi", "zh": "內股透", "jp": "内股透かし", "group": "投技:立技:不分群"},
  "UNA": {"en": "Ura-nage", "zh": "裏投", "jp": "裏投げ", "group": "投技:捨身技:前捨身技"},
  "UNK": {"en": "Undetermined Katame-waza", "zh": "未定固技", "jp": "未定固め技", "group": "未分群"},
  "UOT": {"en": "Uki-otoshi", "zh": "浮落", "jp": "浮落とし", "group": "投技:立技:手技"},
  "URG": {"en": "Ura-gatame", "zh": "裏固", "jp": "裏固め", "group": "固技:抑技"},
  "UTG": {"en": "Utsuri-goshi", "zh": "移腰", "jp": "移腰", "group": "投技:立技:腰技"},
  "UWA": {"en": "Uki-waza", "zh": "浮技", "jp": "浮技", "group": "投技:立技:不分群"},
  "YGA": {"en": "Yoko-gake", "zh": "橫掛", "jp": "横掛け", "group": "投技:捨身技:橫捨身技"},
  "YGU": {"en": "Yoko-guruma", "zh": "橫車", "jp": "横車", "group": "投技:捨身技:橫捨身技"},
  "YOT": {"en": "Yoko-otoshi", "zh": "橫落", "jp": "横落とし", "group": "投技:捨身技:橫捨身技"},
  "YSG": {"en": "Yoko-shiho-gatame", "zh": "橫四方固", "jp": "横四方固め", "group": "固技:抑技"},
  "WKG": {"en": "Waki-gatame", "zh": "腋固", "jp": "脇固め", "group": "固技:抑技"},
}

IPPON_DROPDOWN_MAP_1 = {
    "全部": ["-"],
    "固技": ["-", "抑技", "絞技", "関節技"],
    "投技": ["-", "立技", "捨身技"],
    "未分群": ["-"],
    "無資料": ["-"],
}

IPPON_DROPDOWN_MAP_2 = {
    "-": ["-"],
    "全部": ["-"],
    "抑技": ["-"],
    "絞技": ["-"],
    "関節技": ["-"],
    "立技": ["-", "手技", "腰技", "足技", "不分群"],
    "捨身技": ["-", "前捨身技", "橫捨身技", "橫捨身技"],
}

IPPONTECH_DROPDOWN_MAP = []

for key, value in JUDO_TECHNIQUE.items():
    IPPONTECH_DROPDOWN_MAP.append(f"{key}:{value['group'].replace(':', '>')}")

from urllib.parse import quote  # 對中文 sheet 名稱進行 URL 編碼

SHEET_GID_MAPPING = {
 '勝者國家>Ippon技術分類地圖>全部Ippon比賽': '1298109612',
 '勝者國家>Ippon技術分類地圖>男子有Ippon比賽': '28792196',
 '勝者國家>Ippon技術分類地圖>女子有Ippon比賽': '942645638',
 '勝者國家>Ippon技術分類地圖>全部Ippon比賽-1': '638546443',
 '勝者國家>Ippon技術分類地圖>男子有Ippon比賽-1': '1071718401',
 '勝者國家>Ippon技術分類地圖>女子有Ippon比賽-1': '1104268805',
 '勝者國家>Ippon技術分類地圖>全部Ippon比賽-2': '1946909308',
 '勝者國家>Ippon技術分類地圖>男子有Ippon比賽-2': '1435903933',
 '勝者國家>Ippon技術分類地圖>女子有Ippon比賽-2': '1484551104',
 '勝者國家>Ippon技術分類地圖>全部Ippon比賽-3': '572016594',
 '勝者國家>Ippon技術分類地圖>男子有Ippon比賽-3': '595503184',
 '勝者國家>Ippon技術分類地圖>女子有Ippon比賽-3': '1859043650',
 '勝者國家>Ippon技術地圖>全部Ippon比賽': '627767754',
 '勝者國家>Ippon技術地圖>男子有Ippon比賽': '1675385436',
 '勝者國家>Ippon技術地圖>女子有Ippon比賽': '1230658937'}

def loadData_bySheetName(label: str, source_sheet_url: str, sheet_name: str):

    # ✅ 擷取試算表 ID
    try:
        sheet_id = source_sheet_url.split("/d/")[1].split("/")[0]
    except IndexError:
        print("❌ 無法解析 Google Sheet 連結，請確認格式正確。")
        return None, None, None

    # ✅ 對工作表名稱做 URL 編碼
    sheet_name_encoded = quote(sheet_name)

    # ✅ 組出 CSV 匯出網址
    csv_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name_encoded}"

    # ✅ 嘗試讀取工作表內容
    try:
        df = pd.read_csv(csv_url)
    except Exception as e:
        print(f"❌ 無法讀取工作表：'{sheet_name}'，錯誤原因：{e}")
        return None, None, None

    # ✅ 篩選該 label 的資料
    df_filtered = df[df["label"] == label].copy()

    # ✅ 取得該工作表對應的 gid（預設為 0，如果沒找到）
    gid = SHEET_GID_MAPPING.get(sheet_name, "0")

    # ✅ 組出直接連結（含 gid）
    sheet_direct_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/edit#gid={gid}"

    # ✅ 回傳說明資訊與資料
    return_info_1 = f"資料來源｜試算表 ID：{sheet_id}｜工作表：{sheet_name}"
    return_info_2 = f"詳細資料：{sheet_direct_url}"

    return df_filtered, return_info_1, return_info_2

import matplotlib.pyplot as plt
import pandas as pd

import folium  # 用於地圖繪製
import math  # 數學運算
import pandas as pd  # 資料處理
import seaborn as sns  # 色彩選擇
from matplotlib.colors import to_hex  # 將 RGB 顏色轉為 HEX 格式

def drawData_winnerCountry_map(grouped_df: pd.DataFrame,
                               df_olympic_countries: pd.DataFrame,
                               label: str,
                               top_n: int = 100,
                               title: str = "",
                               legend_mapping: dict = None,
                               ippon_group_name: str = None,
                               is_gradio: bool = False):  # ✅ 傳入 "投技:立技:足技" 這類格式

    fig_width_px = 1000  # 地圖寬度
    fig_height_px = 800  # 地圖高度
    twn_color = 'Crimson'  # 特別顯示台灣
    min_radius = 2  # 最小圓形半徑
    max_radius = 60  # 最大圓形半徑
    scale_factor = 1.0  # 縮放因子

    # ✅ 建立國家代碼對應經緯度座標
    coord = {row["code"]: (row["latitude"], row["longitude"]) for _, row in df_olympic_countries.iterrows()}

    # ✅ 建立洲別顏色對應字典
    unique_continents = df_olympic_countries['continent'].unique()
    palette_rgb = sns.color_palette('tab10', len(unique_continents))
    palette_hex = [to_hex(c) for c in palette_rgb]
    continent_colors = dict(zip(unique_continents, palette_hex))

    # 🔍 過濾指定 label 的資料
    df = grouped_df.copy()
    df = df[df["label"] == label].copy()

    # ✅ 根據 ippon_group_name 參數決定用哪個欄位計算數量
    if ippon_group_name is None or str(ippon_group_name).lower() == "none":
        df["total"] = pd.to_numeric(df["total"], errors="coerce").fillna(0).astype(int)
    else:
        # ✅ 從所有欄位中找出「= 之後為 ippon_group_name」的欄位（不限定前綴）
        match_cols = [
            col for col in df.columns
            if "=" in col and col.split("=", 1)[-1] == ippon_group_name
        ]
        if not match_cols:
            raise ValueError(f"❌ 無法對應到欄位：*= {ippon_group_name}")
        col_name = match_cols[0]  # ✅ 正確欄位名稱
        df["total"] = pd.to_numeric(df[col_name], errors="coerce").fillna(0).astype(int)

    # 🔢 取前 top_n 的國家
    df = df.sort_values(by="total", ascending=False).head(top_n).copy()
    top_countries = df["winner_country"].tolist()
    if "TWN" not in top_countries and "TWN" in grouped_df["winner_country"].unique():
        top_countries.append("TWN")

    # ✅ 建立地圖
    m = folium.Map(
        location=[20, 0],  # 初始中心點
        zoom_start=2,  # 初始縮放
        control_scale=True,
        tiles='CartoDB PositronNoLabels',  # 背景圖層
        width=fig_width_px,
        height=fig_height_px
    )

    # ✅ 計算數量的平方根範圍（用於圓形半徑正規化）
    min_count = df["total"].min()
    max_count = df["total"].max()
    min_sqrt = math.sqrt(min_count) if min_count > 0 else 0
    max_sqrt = math.sqrt(max_count) if max_count > 0 else 1
    radius_range = max_radius - min_radius

    # ✅ 加入圓形與標籤
    for _, row in df.iterrows():
        code = row["winner_country"]
        count = row["total"]
        if code not in coord or count == 0:
            continue  # ⛔ 國家無座標或數量為 0，就略過

        # ✅ 計算圓形半徑（依據數量平方根正規化）
        radius = min_radius + ((math.sqrt(count) - min_sqrt) / (max_sqrt - min_sqrt)) * radius_range * scale_factor

        # ✅ 設定填色與字色
        if code == "TWN":
            fill_color = twn_color
            text_color = twn_color
        else:
            continent = df_olympic_countries.set_index("code").get("continent", {}).get(code, "Other")
            fill_color = continent_colors.get(continent, "gray")
            text_color = "black"

        # ✅ Tooltip 顯示文字（可轉換成 legend 名）
        label_text = legend_mapping.get(code, code) if legend_mapping else code
        tooltip_text = f"{label_text}: {count}"

        # ✅ 畫圓形標記
        folium.CircleMarker(
            location=coord[code],  # 圓心位置
            radius=radius,  # 半徑
            fill=True,
            color=None,
            fill_opacity=0.4,
            fill_color=fill_color,
            tooltip=tooltip_text
        ).add_to(m)

        # ✅ 顯示國家代碼與數值文字標籤
        folium.Marker(
            location=coord[code],
            tooltip=tooltip_text,
            icon=folium.DivIcon(html=f'''
                <div style="
                    font-size: 14px;
                    color: {text_color};
                    text-align: center;
                    position: absolute;
                    top: 50%;
                    left: 50%;
                    transform: translate(-50%, -50%);
                    white-space: nowrap;
                    line-height: 1.2;">
                    <b>{code}</b><br>{count}
                </div>
            ''')
        ).add_to(m)

    # ✅ 顯示地圖（根據 is_gradio 方式不同）
    html_output = f'<div style="width: {fig_width_px}px; height: {fig_height_px}px">{m._repr_html_()}</div>'

    if is_gradio:
        return html_output
    else:
        html_widget = widgets.HTML(
            value=html_output,
            placeholder='地圖載入中...',
            description=''
        )
        display(html_widget)

from matplotlib import pyplot as plt
import io, base64

def executeDrawData_2(year_data, selected_function, selected_function_text, output,
                      secondary_value=None, ippon_main=None, ippon_sub=None, ippon_child=None, ippon_tech=None):

    img_base64 = None  # 預設為空

    if selected_function_text == "勝者國家>Ippon技術分類地圖":

        if ippon_main == "全部":

            df, info1, info2 = loadData_bySheetName(year_data["label"], SHEET_URL_VIZ, f"{selected_function}>{secondary_value}")

            img_base64 = drawData_winnerCountry_map(df, df_olympic_countries, label=year_data["label"],
                                                    title=f"{secondary_value}的{selected_function_text.split('>')[0]}",
                                                    is_gradio=True)

        else: #elif ippon_main != "全部":

            ippon_group_name = None

            if ippon_sub == "-" and ippon_child == "-":

                df, info1, info2 = loadData_bySheetName(year_data["label"], SHEET_URL_VIZ, f"{selected_function}>{secondary_value}-1")
                ippon_group_name = f"{ippon_main}"

            elif ippon_child == "-":

                df, info1, info2 = loadData_bySheetName(year_data["label"], SHEET_URL_VIZ, f"{selected_function}>{secondary_value}-2")
                ippon_group_name = f"{ippon_main}:{ippon_sub}"

            else:

                df, info1, info2 = loadData_bySheetName(year_data["label"], SHEET_URL_VIZ, f"{selected_function}>{secondary_value}-3")
                ippon_group_name = f"{ippon_main}:{ippon_sub}:{ippon_child}"

            img_base64 = drawData_winnerCountry_map(df, df_olympic_countries, label=year_data["label"],
                                                    title=f"{secondary_value}的{selected_function_text.split('>')[0]}",
                                                    ippon_group_name=ippon_group_name,
                                                    is_gradio=True)

    elif selected_function_text == "勝者國家>Ippon技術地圖":

        df, info1, info2 = loadData_bySheetName(year_data["label"], SHEET_URL_VIZ, f"{selected_function}>{secondary_value}")

        img_base64 = drawData_winnerCountry_map(df, df_olympic_countries, label=year_data["label"],
                                                title=f"{secondary_value}的{selected_function_text.split('>')[0]}",
                                                ippon_group_name=ippon_tech,
                                                is_gradio=True)

    return img_base64 if img_base64 else "<p>⚠️ 無圖表資料。</p>"

# ✅ 匯入必要模組
import streamlit as st

# ===== 主 UI 函式（已移除比賽預測）=====
def build_streamlit_ui():
    st.set_page_config(layout="wide")
    st.title("📊 柔道資料視覺化 UI")

    tab_names = list(DROPDOWN_OPTIONS.keys())
    tabs = st.tabs(tab_names)

    for i, tab_name in enumerate(tab_names):
        option_list = DROPDOWN_OPTIONS[tab_name]
        with tabs[i]:
            if not option_list:
                st.markdown("🏅 尚無屬性選項")
                continue

            # ✅ 主屬性下拉選單
            attribute_choices = [item[0] for item in option_list]
            default_attr = attribute_choices[0]
            attr = st.selectbox("選擇屬性", attribute_choices, key=f"{tab_name}_attr")

            # ✅ 副屬性選單（若有）
            has_sub = attr in SECONDARY_DROPDOWN_MAP
            sub = None
            if has_sub:
                sub_choices = SECONDARY_DROPDOWN_MAP[attr]
                sub = st.selectbox("選擇屬性分類", sub_choices, key=f"{tab_name}_sub")

            # ✅ Ippon 技術分類（僅當屬性為 Ippon 分類地圖時顯示）
            ippon_main = ippon_sub = ippon_child = None
            if attr == "勝者國家>Ippon技術分類地圖":
                col1, col2, col3 = st.columns([1, 1, 1])
                with col1:
                    ippon_main = st.selectbox("主分類", list(IPPON_DROPDOWN_MAP_1.keys()), key=f"{tab_name}_ippon_main")
                with col2:
                    ippon_sub_choices = IPPON_DROPDOWN_MAP_1.get(ippon_main, ["-"])
                    ippon_sub = st.selectbox("次分類", ippon_sub_choices, key=f"{tab_name}_ippon_sub")
                with col3:
                    ippon_child_choices = IPPON_DROPDOWN_MAP_2.get(ippon_sub, ["-"])
                    ippon_child = st.selectbox("子分類", ippon_child_choices, key=f"{tab_name}_ippon_child")

            # ✅ Ippon 技術單選欄（僅當屬性為 Ippon 技術地圖時顯示）
            ippon_tech = None
            if attr == "勝者國家>Ippon技術地圖":
                ippon_tech = st.selectbox("選擇技術", IPPONTECH_DROPDOWN_MAP, key=f"{tab_name}_ippon_tech")

            # ✅ 年份選擇（奧運 → 世錦排序）
            olympic_labels = [y["label"] for y in YEARS_DATA if y["game"] == "olympics"]
            championship_labels = [y["label"] for y in YEARS_DATA if y["game"] == "championships"]
            year_labels = olympic_labels + championship_labels
            year_label = st.radio("選擇賽事", year_labels, horizontal=True, key=f"{tab_name}_year")

            # ✅ 從年份標籤找出 year_data
            year = year_label[:2]
            game = "olympics" if "奧運" in year_label else "championships"
            year_data = next((y for y in YEARS_DATA if y["year"] == year and y["game"] == game), None)

            # ✅ 對應處理函式
            selected_function = next(v for k, v in option_list if k == attr)
            selected_function_text = attr

            # ✅ 呼叫圖表函式
            html = executeDrawData_2(
                year_data,
                selected_function,
                selected_function_text,
                output=None,
                secondary_value=sub,
                ippon_main=ippon_main,
                ippon_sub=ippon_sub,
                ippon_child=ippon_child,
                ippon_tech=ippon_tech  # ✅ 傳入技術值參數
            )

            # ✅ 顯示圖表
            st.components.v1.html(html, height=600, scrolling=True)

            # ✅ 除錯資訊
            debug = f'''year_data: {year_data}
selected_function: {selected_function}
selected_function_text: {selected_function_text}
secondary_value: {sub}
ippon_main: {ippon_main}
ippon_sub: {ippon_sub}
ippon_child: {ippon_child}
ippon_tech: {ippon_tech}'''
            st.text_area("📌 DEBUG 傳入參數", debug, height=160)

# ===== 執行應用 =====
if __name__ == "__main__":
    build_streamlit_ui()