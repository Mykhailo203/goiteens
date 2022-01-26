class footbalclub:
    title = ''
    city = ''
    points = ''


class championship:
    country = ''
    title_championship = ''
    teams = list()

    def add_club(self, new_club):
        self.teams.append(new_club)
    

    def worst_team(self):
        worst_team = self.teams[0]
        for worst in self.teams:
            if worst.points < worst_team.points:
                worst_team = worst
        return worst_team

    def print(self):
        print('Комада з найменшою кількістю очок - ', self.worst_team)

    

Liverpool = footbalclub()
Liverpool.title = 'Liverpool'
Liverpool.city = 'Liverpool'
Liverpool.points = 16

mu = footbalclub()
mu.title = 'Manchester United'
mu.points = 19
mu.city = 'Manchester'

mc = footbalclub()
mc.title = 'Manchester City'
mc.points = 10
mc.city = 'Manchester'

Chelsea = footbalclub()
Chelsea.title = 'Chelsea'
Chelsea.points = 21
Chelsea.city = 'London'

PremierLeague = championship()
PremierLeague.country = 'England'
PremierLeague.title_championship = 'PremierLeague'
PremierLeague.add_club(Chelsea)
PremierLeague.add_club(Liverpool)
PremierLeague.add_club(mc)
PremierLeague.add_club(mu)

worstteam = PremierLeague.worst_team()
print('Комада з найменшою кількістю очок - ', worstteam.title)