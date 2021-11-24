def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Carryaway, obj[17]: Restaurantlessthan20, obj[18]: Restaurant20to50, obj[19]: Direction_same, obj[20]: Distance
	# {"feature": "Age", "instances": 20, "metric_value": 0.9928, "depth": 1}
	if obj[8]>0:
		# {"feature": "Temperature", "instances": 16, "metric_value": 0.9887, "depth": 2}
		if obj[3]>55:
			# {"feature": "Restaurantlessthan20", "instances": 9, "metric_value": 0.9183, "depth": 3}
			if obj[17]>1.0:
				return 'True'
			elif obj[17]<=1.0:
				# {"feature": "Occupation", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[12]>0:
					return 'False'
				elif obj[12]<=0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[3]<=55:
			# {"feature": "Time", "instances": 7, "metric_value": 0.5917, "depth": 3}
			if obj[4]>0:
				return 'False'
			elif obj[4]<=0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[8]<=0:
		return 'True'
	else: return 'True'
