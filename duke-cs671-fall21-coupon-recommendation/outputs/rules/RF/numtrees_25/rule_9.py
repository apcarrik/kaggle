def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Carryaway, obj[17]: Restaurantlessthan20, obj[18]: Restaurant20to50, obj[19]: Direction_same, obj[20]: Distance
	# {"feature": "Coupon_validity", "instances": 41, "metric_value": 0.9789, "depth": 1}
	if obj[6]>0:
		# {"feature": "Age", "instances": 25, "metric_value": 0.9896, "depth": 2}
		if obj[8]<=5:
			# {"feature": "Occupation", "instances": 21, "metric_value": 0.9183, "depth": 3}
			if obj[12]<=7:
				# {"feature": "Time", "instances": 16, "metric_value": 0.6962, "depth": 4}
				if obj[4]>0:
					return 'False'
				elif obj[4]<=0:
					# {"feature": "Carryaway", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[16]<=2.0:
						return 'False'
					elif obj[16]>2.0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[12]>7:
				# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[1]>0:
					return 'True'
				elif obj[1]<=0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[8]>5:
			return 'True'
		else: return 'True'
	elif obj[6]<=0:
		# {"feature": "Temperature", "instances": 16, "metric_value": 0.6962, "depth": 2}
		if obj[3]>55:
			return 'True'
		elif obj[3]<=55:
			# {"feature": "Income", "instances": 6, "metric_value": 1.0, "depth": 3}
			if obj[13]>5:
				return 'True'
			elif obj[13]<=5:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'True'
