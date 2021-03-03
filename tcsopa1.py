
passengers = []

class Passenger:
	def __init__ (self,passengerName,passengerAge,distanceTraveled):
		self.passengerName = passengerName
		self.passengerAge = passengerAge
		self.distanceTraveled = distanceTraveled
		
	

	def calculateTicketFare(passengers,fareperkm):
		TotalFare = 0
		for passen in passengers:
			if passen.passengerAge >= 60 | passen.passengerAge < 12:
				Ticketfare = passen.distanceTraveled * fareperkm
				TotalFare += Ticketfare

			elif passen.passengerAge >= 21 & passen.passengerAge < 59:
				Ticketfare = (passen.distanceTraveled * fareperkm) + ((passen.distanceTraveled*fareperkm)*0.12)
				TotalFare += Ticketfare

			elif passen.passengerAge >= 12 & passen.passengerAge < 20:
				Ticketfare = (passen.distanceTraveled * fareperkm) + ((passen.distanceTraveled * fareperkm)* 0.10)
				TotalFare += Ticketfare
		return TotalFare

	def countSeniorJuniorPassengers(passengers):
		count = 0 
		for passen in passengers:
			if passen.passengerAge >= 60 or passen.passengerAge<12:
				count += 1
		return count

if __name__ == "__main__":
	n = int(input())
	
	for i in range(n):
		passengerName = input()
		passengerAge = int(input())
		distanceTraveled = int(input())

		passengers.append(Passenger(passengerName,passengerAge,distanceTraveled))
	

	fareperkm = int(input())

	print(calculateTicketFare(passengers,fareperkm))
	print(count(passengers))
