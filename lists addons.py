gs= ["Lord Caitanya", "Lord Nitai", "Prabhupada"]

for x in gs:
    print ("Hello "+ x+ " please come have dinner with me!");


absentee= gs.pop(0);
print ("\nUnfortunatly " + absentee + "can not make it tonight \n");


for y in gs:
    print ("Hello "+ y+ " please come have dinner with me!");

print ("\nHari Hari, I found a bigger table! More people can come!!!!\n");

gs.insert(0, "Srila Bhaktisiddhanta");
gs.insert(2, "Bhaktivinoda Thakur");
gs.append("Mahatma prabhu")

for z in gs:
    print ("Hello "+ z+ " please come have dinner with me!");

print ("there will be " + str(len(gs))+ " people at the party tonight");







'''
ls= ["mom", "dad", "sister", "cat"];

ls.insert(2, "rocky ");


print (ls[1]);

print (ls[0]);
'''