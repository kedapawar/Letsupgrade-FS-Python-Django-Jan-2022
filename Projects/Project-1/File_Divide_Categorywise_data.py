fo=open("Category.txt","r",encoding="UTF-8")
for each in fo:
    #a,b=each.split(":",1)
    with open("books.txt","w") as f1,open("clothing and accessories.txt","w") as f2,open("watches and jwellery.txt","w") as f3,open("Home and Kitchen.txt","w") as f4,open("mobiles and tablets.txt","w") as f5,open("sports fitness.txt","w") as f6,open("beauty health.txt","w") as f7,open("handbags and luggage.txt","w") as f8,open("shoe and belt.txt","w") as f9,open("toys and baby products.txt","w") as f10,open("computer and accessories.txt","w") as f11,open("camera audio video.txt","w") as f12,open("pet supplies.txt","w") as f13,open("movies and video games.txt","w") as f14:
        for line in fo:
           if "books" in line:
             f1.write(line)
           elif "clothing and accessories" in line: 
             f2.write(line)
           elif "watches and jwellery"  in line:
             f3.write(line) 
           elif "Home and Kitchen"  in line:
             f4.write(line) 
           elif "mobiles and tablets"  in line:
             f5.write(line)
           elif "sports fitness"  in line:
             f6.write(line)  
           elif "beauty health"  in line:
             f7.write(line)
           elif "handbags and luggage"  in line:
             f8.write(line)
           elif "shoe and belt"  in line:
             f9.write(line)
           elif "toys and baby products"  in line:
             f10.write(line)
           elif "computer and accessories"  in line:
             f11.write(line)
           elif "camera audio video"  in line:
             f12.write(line)
           elif "pet supplies"  in line:
             f13.write(line)
           elif "movies and video games"  in line:
             f14.write(line)                
fo.close()                    