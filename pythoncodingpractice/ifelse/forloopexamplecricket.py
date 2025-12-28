Team=input()

Target=int(input())
Balls=int(input())
total_runs=0
for i in range(1, Balls + 1):
    run=int(input(f"batsman run in {i} ball: "))
    total_runs +=run

    if total_runs>Target:
        print(f"Match over and asusual {Team} won the match")
        break

if total_runs<Target:
    print(f"Match over and {Team} lost the match")