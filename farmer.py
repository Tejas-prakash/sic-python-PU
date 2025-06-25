
total_land = 80
segments = 5
segment_area = total_land / segments  
tomato_area = segment_area
tomato_yield_30 = 10  
tomato_yield_70 = 12  
tomato_price_per_kg = 7
potato_yield = 10  
potato_price_per_kg = 20

cabbage_yield = 14  
cabbage_price_per_kg = 24

sunflower_yield = 0.7  
sunflower_price_per_kg = 200

sugarcane_yield = 45  
sugarcane_price_per_tonne = 4000

tomato_tonnes = (0.3 * tomato_area * tomato_yield_30) + (0.7 * tomato_area * tomato_yield_70)
tomato_sales = tomato_tonnes * 1000 * tomato_price_per_kg

potato_tonnes = segment_area * potato_yield
potato_sales = potato_tonnes * 1000 * potato_price_per_kg

cabbage_tonnes = segment_area * cabbage_yield
cabbage_sales = cabbage_tonnes * 1000 * cabbage_price_per_kg

sunflower_tonnes = segment_area * sunflower_yield
sunflower_sales = sunflower_tonnes * 1000 * sunflower_price_per_kg

sugarcane_tonnes = segment_area * sugarcane_yield
sugarcane_sales = sugarcane_tonnes * sugarcane_price_per_tonne

overall_sales = tomato_sales + potato_sales + cabbage_sales + sunflower_sales + sugarcane_sales
print(f"Overall sales from 80 acres: Rs. {overall_sales}")

chemical_free_sales = tomato_sales + potato_sales + cabbage_sales + sunflower_sales
print(f"Sales from chemical-free farming at 11 months: Rs. {chemical_free_sales}")
