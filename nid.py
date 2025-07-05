def nid(name,nid_number,DOB,gender,prenent_address,permanent_address):
  info=f"Name:{name}\n Nid Number: {nid_number}\n Date of Birth: {DOB}\n Gender: {gender}\n prenent address: {prenent_address}\n permanent address: {permanent_address}\n "
  return info
nid_info=nid("Tasnova","37864386","26 june 2001","Female", "Ctg ,BD","Ctg ,BD")
print(nid_info)