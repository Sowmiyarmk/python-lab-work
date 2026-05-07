lang = ("java", "c", "cpp", "sql", "SQL")

# Ascending order
l1 = tuple(sorted(lang))
print("THE SORTED TUPLE L1 (ascending):", l1)

# Descending order
l2 = tuple(sorted(lang, reverse=True))
print("THE SORTED TUPLE L2 (descending):", l2)

# Original tuple remains unchanged
print("THE ORIGINAL TUPLE lang:", lang)
