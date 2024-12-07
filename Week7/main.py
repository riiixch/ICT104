from bigtree import list_to_tree, print_tree

course_list = "sompop ieamsombat"
path_list = ["s/o/m/p/o/p", "s/i/e/a/m/s/o/m/b/a/t", "s/i"]

root = list_to_tree(path_list)
print(course_list)
print("********************")
print_tree(root)
