# function input
my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}
#function output
[("Speros", "(555) 555-5555"), ("Michael", "(999) 999-9999"), ("Jay", "(777) 777-7777")]

empty_list=[]
for key,values in my_dict.iteritems():
    newtuple = key,values
    empty_list.append(newtuple)
print empty_list