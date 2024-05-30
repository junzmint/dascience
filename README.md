# Run the application
```docker-compose up --build```
# Turn off all the docker components
```docker-compose down```
# API documentation
```http://localhost:8000/category/?category=[]&type=[]]```
category in [pet, health, man_fashion]
type in [negative, positive]

# Each category have smaller categories

Chăm-Sóc-Thú-Cưng:
      food
      accessories
      drug
      fashion

Sức-khỏe:
      q-tip
      heathcare
      condoms
      mask
      self-hygiene
      massage
      contact-lens
      vitamins
      drugs
      accessories

Thời-trang-nam:
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
 