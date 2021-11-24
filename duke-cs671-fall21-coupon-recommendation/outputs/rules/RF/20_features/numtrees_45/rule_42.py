def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Bar", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[14]<=1.0:
		# {"feature": "Driving_to", "instances": 19, "metric_value": 0.8315, "depth": 2}
		if obj[0]>0:
			# {"feature": "Temperature", "instances": 11, "metric_value": 0.994, "depth": 3}
			if obj[3]>30:
				# {"feature": "Time", "instances": 8, "metric_value": 0.9544, "depth": 4}
				if obj[4]>0:
					# {"feature": "Occupation", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[12]<=14:
						return 'False'
					elif obj[12]>14:
						return 'True'
					else: return 'True'
				elif obj[4]<=0:
					return 'True'
				else: return 'True'
			elif obj[3]<=30:
				return 'True'
			else: return 'True'
		elif obj[0]<=0:
			return 'True'
		else: return 'True'
	elif obj[14]>1.0:
		return 'False'
	else: return 'False'
