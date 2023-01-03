siteNum, visitSiteNum = map(int, input().split())
sites = {}

for _ in range(siteNum):
    site, password = input().split()
    sites[site] = password

for _ in range(visitSiteNum):
    visitSite = input()
    print(sites[visitSite])