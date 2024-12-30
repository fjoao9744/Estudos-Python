def maior(*args):
    print("analisando valores passados...")
    if len(args) > 0 and not args[0] == 0:
        maior = args[0]
        print(f"{args} foram informados {len(args)} valores")
        for c in args:
            if c >= maior:
                maior = c
        print(f"e o maior foi {maior}")
        
    else:
        print("foram informados nenhum valor")

print("-=" * 20)
maior(1, 4, 3, 10, 29, 24, 1, 4, 2, 1, 9, 4, 7, 17, 20)
print("-=" * 20)
maior(5, 2, 3, 8, 2, 3, 5, 9, 1)
print("-=" * 20)
maior(10, 32, 4, 10)
print("-=" * 20)
maior(0)
print("-=" * 20)
