class player:
  def play(self):
    print("The player is playing cricket.")
class batsman:
  def play(self):
    print("The bats is batting.")
class Bowler( player):
  def play(self):
    print("The bowler is bowling.")
Batsman=batsman()
bowler=Bowler()
Batsman.play()
bowler.play()
    