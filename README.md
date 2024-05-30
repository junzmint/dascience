# Run the application
```docker-compose up --build```
# Turn off all the docker components
```docker-compose down```
# API documentation
```http://localhost:8000/category/?category=abc&type=positive```
type = negative or positive

# Viết tiếp các get cho các category khác

mỗi category mn tạo 1 file (ten category).py (vd: Pet.py) rồi đọc file processed của nó, làm tương tự như trong category Pet,

trong các function getInsightInNegativeComment, getInsightInPositiveComment, ta cần lấy keyword từ mỗi product_category nên từ 1 dataframe category lớn, ta phải tách thành các dataframe của các product_category
vd : trong pet có 4 product_category là food, accessories, drug, fashion nếu ms cần 4 dataframe con.
các product_category trg các category:
Sức-khỏe:
      "q-tip" 
      "heathcare"
      "condoms"
      "mask"
      "self-hygiene"
      "massage"
      "contact-lens"
      "vitamins"
      "drugs"
      "accessories"

thời-trang-nam:
      t-shirt       
      shirt         
      sport          
      polo           
      jeans          
      shorts         
      jacket         
      belt           
      pants           
      underwear       
      hoodie          
      sock            
      footwear         
      accessories      
      hat              
 