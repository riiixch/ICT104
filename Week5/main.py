import collections

link_list = collections.deque()

link_list.append('500')
link_list.append('600')
link_list.append('700')

print("Link list:", link_list)

link_list.remove('600')

print("Link list:", link_list)

link_list.insert(0, '100')
link_list.insert(1, '200')
link_list.insert(3, '300')

print("Link list:", link_list)

link_list.pop()

print("Link list:", link_list)

link_list.append('150')
link_list.append('250')
link_list.append('350')

print("Link list:", link_list)

link_list.remove('500')
link_list.remove('200')
link_list.remove('250')
link_list.remove('300')

print("Link list:", link_list)

link_list.append('65064435')
link_list.append('สมภพ เอี่ยมสมบัติ')

print("Link list:", link_list)