def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Education", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[11]<=2:
		# {"feature": "Restaurant20to50", "instances": 18, "metric_value": 0.9641, "depth": 2}
		if obj[17]<=1.0:
			# {"feature": "Income", "instances": 12, "metric_value": 0.65, "depth": 3}
			if obj[13]<=6:
				# {"feature": "Passanger", "instances": 11, "metric_value": 0.4395, "depth": 4}
				if obj[1]<=2:
					return 'False'
				elif obj[1]>2:
					# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[4]>2:
						return 'True'
					elif obj[4]<=2:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[13]>6:
				return 'True'
			else: return 'True'
		elif obj[17]>1.0:
			# {"feature": "Driving_to", "instances": 6, "metric_value": 0.65, "depth": 3}
			if obj[0]<=1:
				return 'True'
			elif obj[0]>1:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[11]>2:
		return 'True'
	else: return 'True'
