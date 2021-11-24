def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Carryaway, obj[17]: Restaurantlessthan20, obj[18]: Restaurant20to50, obj[19]: Direction_same, obj[20]: Distance
	# {"feature": "Coupon", "instances": 20, "metric_value": 0.9928, "depth": 1}
	if obj[5]>1:
		# {"feature": "Distance", "instances": 16, "metric_value": 0.896, "depth": 2}
		if obj[20]<=1:
			# {"feature": "Time", "instances": 9, "metric_value": 0.9911, "depth": 3}
			if obj[4]<=2:
				# {"feature": "Income", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[13]<=7:
					return 'False'
				elif obj[13]>7:
					return 'True'
				else: return 'True'
			elif obj[4]>2:
				return 'True'
			else: return 'True'
		elif obj[20]>1:
			return 'True'
		else: return 'True'
	elif obj[5]<=1:
		return 'False'
	else: return 'False'
