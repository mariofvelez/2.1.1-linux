x = "#  #" # String; 
y = 0 #int;
z = 20 #int;
a = "" #String
for y in range(z):
    while(z>y):
        a = a + " ";
        z = z - 1;
    print(a + x);
    x = "#" + x + "#";
    a = "";
    z = 20;
    y = y + 1;
    
